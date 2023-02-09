import pkg_resources
pkg_resources.require("flask==2.0.3")
pkg_resources.require("pymongo==4.1.1")
from flask import Flask, jsonify, request, render_template
from check_repo import check
from communication.notifications import update_status
import config
from server.history import History
from json import loads, dumps

# Application:
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    """
    Handler to display the landing page. 
    """
    return render_template('index.html')

@app.route('/documentation', methods=['GET'])
def show_documentation():
    return render_template('documentation.html')

@app.route('/builds', methods=['GET'])
def show_builds():
    """
    Handler to display the build history. Tries to fetch all entries but displays an empty list if something is wrong with the fetched data. 
    """
    try:
        return render_template('history.html', buildlist=history.fetch_all())
    except:
        return render_template('history.html')

@app.route('/builds/<id>', methods=['GET'])
def show_build(id):
    """
    Handler to display a specific build as a html page. 
    """
    try:
        return render_template('build.html', build=history.fetch(id))
    except:
        return render_template('build.html')

@app.route('/', methods=['POST'])
def handle_post():
    """
    Handler for post requests from GitHub repo. Outputs the request statuses to the console running the application. If something goes wrong it sends the landing page instead. 
    """
    try:
        data = loads(request.form['payload'])
        # extract relevant data
        id = data['head_commit']['id']
        status_url = data['repository']['statuses_url']
        clone_url = data['repository']['clone_url']
        repo_NAME = data['repository']['name']
        # sha = data['ref'].split('/')[-1]
        sha = id
        commit_id = id
        timestamp = data['head_commit']['timestamp']
        commit_url = data['head_commit']['url']
        # set update status to pending
        print("calling update_status(",id, status_url, "'pending', <token>)")
        update_status(id, status_url, 'pending', config.api_token)
        print("status updated")
        print("running check(...)")
        result = check(clone_url, repo_NAME, sha)
        # update status based on result
        status = 'success' if result.returncode == 0 else 'failure'
        print("check finished with result "+status)
        print("calling update_status(",id, status_url, status, "<token>)")
        update_status(id, status_url, status, config.api_token)
        print("status updated")
        # insert into database
        build = history.serialize(commit_id, timestamp, status, commit_url, result.stderr if result.stderr is not None else '')
        print("calling insert_build("+dumps(build)+")")
        try:
            history.insert_build(build)
        except:
            return 'Duplicate key'
        print("build inserted")
        return 'POST REQUEST PROCESSED SUCCESSFULLY'
    except:
        return render_template('index.html')

# main driver function
if __name__ == '__main__':
    global history
    config.init('ci.ini')
    history = History(config.mongo_database_name, config.mongo_url)
    app.run(debug=True, port=8017)

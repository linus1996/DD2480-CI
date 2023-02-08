import pkg_resources
pkg_resources.require("flask==2.0.3")
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
    return jsonify('GET REQUEST RECEIVED')
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    data = loads(request.form['payload'])
    # extract relevant data
    id = data['head_commit']['id']
    status_url = data['repository']['statuses_url']
    clone_url = data['repository']['clone_url']
    repo_NAME = data['repository']['name']
    sha = data['ref'].split('/')[-1]
    commit_id = data['head_commit']['id']
    timestamp = data['head_commit']['timestamp']
    commit_url = data['head_commit']['url']
    # set update status to pending
    update_status(id, status_url, 'pending', config.api_token)
    result = check(clone_url, repo_NAME, sha)
    # update status based on result
    status = 'success' if result.returncode == 0 else 'failure'
    update_status(id, status_url, status, config.api_token)
    # insert into database
    build = history.serialize(commit_id, timestamp, status, commit_url, result.stderr if result.stderr is not None else '')
    print("calling insert_build("+dumps(build)+")")
    history.insert_build(build)
    print("build iserted")
    return 'POST REQUEST PROCESSED SUCCESSFULLY'
    # return render_template('index.html')

# main driver function
if __name__ == '__main__':
    global history
    config.init('ci.ini')
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)
    app.run(debug=True, port=8017)

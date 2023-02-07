import pkg_resources
pkg_resources.require("flask==2.0.3")
from flask import Flask, jsonify, request, render_template
from check_repo import check
from communication.notifications import update_status
import config
from server.history import History

# Application:
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return jsonify('GET REQUEST RECEIVED')
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    data = request.form
    # set update status to pending
    update_status(data, 'pending', config.api_token)
    # run compile script and test script
    result = check(data['clone_url'], data['url'], data['ref'].split('/')[-1])
    # update status based on result
    status = 'success' if result.returncode == 0 else 'failure'
    update_status(data, status, config.api_token)
    # insert into database
    build = history.serialize(data['commit_id'], data['commits'][0]['timestamp'], status, data['commits'][0]['url'], result.stderr if result.stderr is not None else '') # TODO: check whether or not the commit extraction is correct
    history.insert_build(build)
    return 'POST REQUEST PROCESSED SUCCESSFULLY'
    # return render_template('index.html')

# main driver function
if __name__ == '__main__':
    global history
    config.init('ci.ini')
    history = History(config.mongo_database_name, config.mongo_ip, config.mongo_port, config.mongo_user, config.mongo_pass)
    app.run(debug=True, port=8017)

from flask import Flask, jsonify, request, render_template
from check_repo import check
from communication.notifications import update_status
from src import config
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    data = request.form
    # set update status to pending
    update_status(data, 'pending', config.api_token)
    # extract the relevant data
    clone_url = data['clone_url']
    repo_url = data['url']
    branch_name = data['ref'].split('/')[-1]
    # run compile script and test script
    result = check(clone_url, repo_url, branch_name)
    # update status based on result
    status = 'success' if result == 0 else 'failure'
    update_status(data, status, config.api_token)
    # insert into database
    
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)

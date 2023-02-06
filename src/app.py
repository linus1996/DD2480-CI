from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():
    data = request.form['payload']
    return jsonify(data)

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)

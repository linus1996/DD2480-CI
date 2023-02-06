from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

list = ['AAAAAAAAAAAAAa', 'Bunny', 'Cat', 'Duck', 'E']

@app.route('/', methods=['GET'])
def test1():
    return jsonify({'GET': [item for item in list]})

@app.route('/', methods=['POST'])
def handle_post():
    data = request.form['payload']
    return jsonify(data)

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)

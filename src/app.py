from flask import Flask, jsonify, request
import json

app = Flask(__name__)

list = ['AAAAAAAAAAAAAa', 'Bunny', 'Cat', 'Duck', 'E']

@app.route('/', methods=['GET'])
def test1():
    return jsonify({'GET': [item for item in list]})

@app.route('/', methods=['POST'])
def test2():
    return jsonify({'POST': [item for item in list]})

# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=8017)

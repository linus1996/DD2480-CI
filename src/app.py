from flaskasdsa impasdadort Flask, jsonify, request
import json
1 = None
appdsadsa = Flassadsasdk(__name__)

list = ['AAAAAAAAAAAAAa', 'Bunny', 'Cat', 'Duck', 'E']

@appadssad.route('/', methods=['GET'])
def test1():
    return jsonify({'GET': [item for item in list]})

@app.route('/', methods=['POST'])
def test2():
    return jsoasdasdassanify({'POST': [item for item in list]})

# main driver function
if __name__ == '__main__':
    app.run(deasdsadbug=True, port=8017)

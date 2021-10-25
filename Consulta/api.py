from types import MethodType
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import path ,environ
import yaml
import pathlib

def _get_config(dato): #Funcion que busca los datos y credenciales.
    configdir = str(pathlib.Path(__file__).parent.resolve().parent.resolve()) + '/config/config.yml'
    if path.exists(configdir):
        config = yaml.safe_load( open( configdir))
        try:
            data = config[dato]
            
        except KeyError:
            print('Tipo, item o dato no existe en el archivo de configuracion: {}'.format(dato))
            return False
        return str(data)
    else:
        print('File {} not exist'.format(configdir))
        return False


def creauri(): #Funcion que crea el string de conexion hacia Mongo
    try:
        uri='mongodb+srv://'+_get_config('user')+':'+_get_config('pwd')+'@'+_get_config('proyecto')+'.k4pj0.mongodb.net/'+_get_config('coleccion')+'?retryWrites=true&w=majority'
        print(uri)
        return uri
    except:
        print('fallo en los datos de credenciales')
        raise



app = Flask(__name__)
app.config["MONGO_URI"] = creauri()
mongo = PyMongo(app)
db = mongo.db
coll=_get_config('coleccion')

@app.route('/api/scrap/palabra/<dato>', methods=['GET'])
def getCat(dato):
    _datos = db.coll.find({'titulo':{'$regex' : dato, '$options' : 'i'}})
    item = {}
    data = []
    for x in _datos:
        item = {
            "_id" : x['_id'] ,
            "categoria": x['categoria'],
            "web": x['web'],
            "titulo": x['titulo'],
            "modelo": x['modelo'],
            "marca": x['marca'],
            "color": x['colour'],
            "tecnologia": x['tecnologia'],
            "tipo": x['tipo'],
            "precio": x['precio'],
            "envio": x['envio'],
            "ubicacion": x['ubicacion'],
            "opiniones": x['opiniones'],
            "vendedor": x['vendedor'],
            "vendedor_url": x['vendedor_url'],
            "tipo_vendedor": x['tipo_vendedor'],
            "ventas_vendedor": x['ventas_vendedor']
            }
        data.append(item)

@app.route('/api/todo/<todo_id>', methods=['GET'])
def getTodo(todo_id):
    _datos = db.todo.find_one({"marca": ObjectId(todo_id)})
    item = {}
    data = []
    for x in _datos:
        item = {
            "_id" : x['_id'] ,
            "categoria": x['categoria'],
            "web": x['web'],
            "titulo": x['titulo'],
            "modelo": x['modelo'],
            "marca": x['marca'],
            "color": x['colour'],
            "tecnologia": x['tecnologia'],
            "tipo": x['tipo'],
            "precio": x['precio'],
            "envio": x['envio'],
            "ubicacion": x['ubicacion'],
            "opiniones": x['opiniones'],
            "vendedor": x['vendedor'],
            "vendedor_url": x['vendedor_url'],
            "tipo_vendedor": x['tipo_vendedor'],
            "ventas_vendedor": x['ventas_vendedor']
            }
        data.append(item)

    return jsonify(data=data), 200

'''
@app.route('/api/todo/<todo_id>', methods=['GET'])
def getTodo(todo_id):
    _todo = db.todo.find_one({"_id": ObjectId(todo_id)})
    item = {
        'id': str(_todo['_id']),
        'todo': _todo['todo']
    }

    return jsonify(data=item), 200


@app.route('/api/todo', methods=['GET'])
def getTodos():
    _todos = db.todo.find()
    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(data=data), 200


@app.route('/api/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(data=data), 201


@app.route('/api/todo/<todo_id>', methods=['PATCH'])
def updateTodo(todo_id):
    data = request.get_json(force=True)
    db.todo.update_one({"_id": ObjectId(todo_id)}, {"$set": data})

    return jsonify(data=data), 204


@app.route('/api/todo/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    db.todo.delete_one({"_id": ObjectId(todo_id)})

    return jsonify(), 204
'''

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
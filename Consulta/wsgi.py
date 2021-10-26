from types import MethodType
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import path ,environ
import yaml
import pathlib
import pymongo
app = Flask(__name__)

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

def qryMongo(qry, index=False):
    MONGO_URI =creauri()
    MONGODB = _get_config('database')
    MONGOCOL=_get_config('coleccion')
    conexion = pymongo.MongoClient(MONGO_URI)
    database = conexion[MONGODB]
    coleccion = database[MONGOCOL]
    if index:
        coleccion.create_index([('$**', 'text')])
    myquery = (qry)
    #myquery = ({'categoria':{'$regex' : PalCla, '$options' : 'i'}})
    mydoc = coleccion.find(myquery)
    #print(myquery)
    #for x in mydoc:
    #    print(x)


    conexion.close()
    return mydoc


@app.route("/Categoria/contiene/<Clave>")
def categoriaContiene(Clave):
    qry = ({'categoria': {'$regex' : Clave, '$options' : 'i'}})
    _datos = qryMongo(qry)
    data = []
    b=0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO PARA LA CATEGORIA {}</p>'.format(Clave)

@app.route("/Categoria/exacta/<Clave>")
def categoriaExacta(Clave):
    qry = ({'categoria': Clave})
    _datos = qryMongo(qry)
    data = []
    b=0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO PARA LA CATEGORIA {}</p>'.format(Clave)


@app.route("/palabraclave/<Clave>")
def palabraClave(Clave, index=True):
    qry = ({ '$text' : { '$search': Clave, '$caseSensitive': False } })
    
    _datos = qryMongo(qry)
    data = []
    b=0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO CON LA PALABRA CLAVE {}</p>'.format(Clave)



@app.route("/precio/menorque/<Clave>")
def precioMenor(Clave):
    qry = ({'categoria':{'$lt' : Clave}})
    _datos = qryMongo(qry)
    data = []
    b = 0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO MENOR QUE {}</p>'.format(Clave), 200


@app.route("/precio/mayorque/<Clave>")
def precioMayor(Clave):
    qry = ({'precio':{'$gt' : int(Clave)}})
    _datos = qryMongo(qry)
    data = []
    b=0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO MAYOR QUE {}</p>'.format(Clave)


@app.route("/precio/entre/<Clave>/<Clave1>")
def precioEntre(Clave,Clave1):
    if Clave>Clave1:
        Mayor=Clave
        Menor=Clave1
    else:
        Mayor=Clave1
        Menor=Clave

    qry = ({'precio':{'$gt' : int(Menor),'$lt' : int(Mayor)}})
    _datos = qryMongo(qry)
    data = []
    b=0
    for x in _datos:
        b =+1
        item = {
            "_id" : str(x['_id']) ,
            "categoria Primera": x['categoria'][0],
            "categoria Segunda": x['categoria'][1],
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

        print(item)
        data.append(item)
        print(data)
    if b>0:
        return jsonify(data=data), 200
    else: 
        return '<p>LA CONSULTA NO ARROJO NINGUN RESULTADO ENTRE {} Y {}</p>'.format(Menor,Mayor),200
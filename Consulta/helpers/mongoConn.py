from typing import Text
import pymongo
import pathlib
import yaml
import os

def _get_config(dato): #Funcion que busca los datos y credenciales.
    configdir = str(pathlib.Path(__file__).parent.resolve().parent.resolve().parent.resolve()) + '/config/config.yml'
    if os.path.exists(configdir):
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
    
    

def qryMongo():
    MONGO_URI =creauri()
    MONGODB = _get_config('database')
    MONGOCOL=_get_config('coleccion')

    conexion = pymongo.MongoClient(MONGO_URI)
    print('lista database')
    print(conexion.list_database_names())
    database = conexion[MONGODB]
    print ('MONGODB')
    print (MONGODB)
    print('lista coleccion')
    print(database.list_collection_names())
    coleccion = database[MONGOCOL]
    print('MONGO COL')
    print(MONGOCOL)
    #myquery = ({'modelo':{ '$regex': '^/s/' :'i'} })
    myquery = ({'categoria':{'$regex' : 'cel', '$options' : 'i'}})
    mydoc = coleccion.find(myquery)
    print(myquery)
    for x in mydoc:
        print(x)

qryMongo()


    

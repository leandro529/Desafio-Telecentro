from pandas.core.frame import DataFrame
import pymongo
import pandas
from os import path
import pathlib
import pandas as pd
def qryMongo(qry):
    MONGO_URI ='mongodb+srv://DesafioTele:Tele123Tele@desafiotele.k4pj0.mongodb.net/scrapMeli?retryWrites=true&w=majority'
    #MONGO_URI = mongodb+srv://<username>:<password>@desafiotele.k4pj0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    conexion = pymongo.MongoClient(MONGO_URI)
    database = conexion['scrapMeli']
    coleccion = database['scrapMeli']
    mydoc = coleccion.find()
    conexion.close()
    return mydoc


qry=qryMongo('')
data=[]
for x in qry:
    data.append(x)
"""     item = {
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
        } """
    #data.append(item)
    

        
df=pd.DataFrame(data)

print (df.head(10))
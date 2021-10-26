# Librerias usadas
pandas==1.2.4
pymongo==3.12.1
PyYAML==5.4.1
requests 
Scrapy==2.5.1
seaborn @ file:///tmp/build/80754af9/seaborn_1608578541026/work
xmltodict==0.12.0

# Documentacion de la libreria
https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Referencia de codigo base
https://github.com/luisramirez-m/mercadolibre-scrapy

# Pagina ayuda con xpath

https://www.scientecheasy.com/2019/08/xpath-axes.html/

# Credenciales
las credenciales se encuentran en ./mercado/config/config.yml

# Como correrlo 
ir hasta el directorio ./Desafio/mercado/spiders
correr el comando 'scrapy crawl mercado'

# Como Correr la API
ir hasta el directorio ./Telecentro/Desafio/Consulta
ejecutar comando 'flask run'

Las consultas generadas son:
    *http://localhost:5000/precio/entre/<Valor1>/<Valor2>
    *http://localhost:5000/precio/mayorque/<Valor>
    *http://localhost:5000/precio/menorque/<Valor>
    *http://localhost:5000/palabraclave/<PalabraClave>
    *http://localhost:5000/Categoria/contiene/<Clave>
    *http://localhost:5000/Categoria/exacta/<Clave>"
    
Referencia API: https://flask.palletsprojects.com/en/2.0.x/
Referencia Consultas Mongo: https://docs.mongodb.com/manual/

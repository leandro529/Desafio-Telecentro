from os import close
from bs4 import BeautifulSoup as bs4
import requests
import csv
import json
import os
import pymongo

#from DatabaseConn.mongocon import _getConf

def urlCat():
    url='https://www.mercadolibre.com.ar/categorias#menu=categories'
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = 'utf-8'
        html = html.text
        dom =bs4(html, features='html.parser')
        subcat=dom.find_all('a',class_='categories__subtitle') #MODULO PARA FILTRAR LAS CATEGORIAS 
        
        if os.path.exists('categorias.json'):
            os.remove('categorias.json')


        f=open('categorias.csv', 'w')
        for sub in subcat:
            print(sub['href'])
            f.write(str(sub['href'])+';\n')
        f.close() 
    else:
        print('Fallo Conexion a Pagina Categorias error {}'.format(html.status_code))        



urlCat()
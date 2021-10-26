# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):#Se Definen los items a Scrapear
    categoria=scrapy.Field()
    web= scrapy.Field()
    titulo= scrapy.Field()
    modelo= scrapy.Field()
    marca= scrapy.Field()
    colour= scrapy.Field()
    tecnologia= scrapy.Field()
    tipo= scrapy.Field()
    precio= scrapy.Field()
    envio= scrapy.Field()
    ubicacion= scrapy.Field()
    opiniones= scrapy.Field()
    publicacion= scrapy.Field()
    vendedor= scrapy.Field()
    vendedor_url= scrapy.Field()
    tipo_vendedor= scrapy.Field()
    ventas_vendedor= scrapy.Field()
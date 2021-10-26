# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy import item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.mx']
	start_urls = ['https://listado.mercadolibre.com.ar/belleza-y-cuidado-personal/barberia/']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__button andes-pagination__button--next"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[@class="ui-search-result__image"]//a[@class="ui-search-link"]')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		# Cada elemento extrae desde el codigo los valores buscados por xpath, en el caso de las tablas se puede usar 
		# "///th[text() = "Modelo"]/following-sibling::td/span/text()" cambiando el valor Modelo por el requerido.
		ml_item['categoria'] = response.xpath('//ul[@class="andes-breadcrumb"]/li/a/text()').extract()
		ml_item['web']= response.url
		ml_item['titulo'] = str(response.xpath('normalize-space(//h1[@class="ui-pdp-title"]/text())').extract_first())
		ml_item['modelo'] = str(response.xpath('//th[text() = "Modelo"]/following-sibling::td/span/text()').extract_first())
		ml_item['marca'] = str(response.xpath('//th[text() = "Marca"]/following-sibling::td/span/text()').extract_first())
		ml_item['colour'] = str(response.xpath('//th[text() = "Color"]/following-sibling::td/span/text()').extract_first())
		ml_item['tecnologia'] = str(response.xpath('//th[text() = "Tecnologia"]/following-sibling::td/span/text()').extract_first())
		ml_item['tipo'] = response.xpath('//th[text() = "Tipo"]/following-sibling::td/span/text()').extract_first()
		ml_item['precio'] = int(response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract_first().replace('.',''))
		ml_item['envio'] = str(response.xpath('normalize-space(//p[contains(@id, "DEFAULT_SELF_SERVICE_ZONES")]/text())').extract_first())
		ml_item['ubicacion'] = str(response.xpath('normalize-space(//p[contains(text(),"Ubicación")]//following-sibling::p)').extract_first()) #//p[contains(text(),"Ubicación")]//following-sibling::p
		ml_item['opiniones'] = str(response.xpath('normalize-space(//p[@class="ui-pdp-reviews__rating__summary__average"]/text())').extract_first())
		#info de la tienda o vendedor
		ml_item['vendedor'] = str(response.xpath('normalize-space(//div[@class="ui-pdp-seller__header__title"]/text())').extract_first())
		ml_item['vendedor_url'] = str(response.xpath('//a[@class="carousel__link--view-more"]/@href').extract_first())
		ml_item['tipo_vendedor'] = str(response.xpath('normalize-space(//p[@class="ui-seller-info__status-info__title ui-pdp-seller__status-title"]/text())').extract_first())
		ml_item['ventas_vendedor'] = int(response.xpath('normalize-space(//strong[@class="ui-pdp-seller__sales-description"]/text())').extract_first())
		
		#Se limita la cantidad de solicitudes para evitar el baneo
		self.item_count += 1
		print(self.item_count)
		if self.item_count > 60:
			raise CloseSpider('item_exceeded')
		yield ml_item

import scrapy
from ..items import CuisineItem

class CuisineSpider(scrapy.Spider):
    name = 'web'
    start_urls = [ 'https://www.allrecipes.com/recipes/86/world-cuisine/' ]
    
    def parse(self, response):
        items = CuisineItem()
        world = response.css('span.link__wrapper::text').extract()
        items['word'] = []
        for i in world:
            items['world'].append(i)
        yield items
        
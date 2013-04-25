import pymongo

from scrapy.conf import settings
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from gosugamersapi.items import GosugamersapiItem
from urlparse import urlparse

class GosuGamersSpider(CrawlSpider):

    name = 'gosugamer'
    rules = (
            Rule(SgmlLinkExtractor(allow=('\/gosubet\/\d+', ), 
            restrict_xpaths=('//div[@id="box_latest_gosubets_upcoming_matches"]')), 
            callback='parse_item'),
        )
    
    
    def __init__(self, game=None):
        super(GosuGamersSpider, self).__init__()
        self.start_urls = ['http://www.gosugamers.net/%s' % game]
        
        # delete old records
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        collection = connection[settings['MONGODB_DB']][settings['MONGODB_COLLECTION']]
        collection.remove( { "game" : game } )
        
        
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)

        item = GosugamersapiItem()
        urlPathSplit = urlparse(response.url).path[1:].split('/')
        item['game'] = urlPathSplit[0]
        
        
        players = hxs.select('//div[@class="cont_middle"]//table//font//a/text()').extract()
        item['playerOne'] = players[0]
        item['playerTwo'] = players[1]
        
        countries = hxs.select('//div[@class="cont_middle"]//table//td[@class="cont_middle_alt"]//img/@title').extract()
        
        # starcraft2 page is a little special
        if item['game'] == 'starcraft2' and len(countries) > 2 :
            item['playerOneCountry'] = countries[1]
            item['playerTwoCountry'] = countries[3]
        else:
            item['playerOneCountry'] = countries[0]
            item['playerTwoCountry'] = countries[1]
        
        item['tournament'] = hxs.select('//div[@class="cont_middle"]//table//b//a/text()').extract()

        item['time'] = hxs.select('//div[@class="cont_middle"]//table//span/@title').extract()
        
        return item

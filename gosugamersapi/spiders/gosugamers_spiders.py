from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from gosugamersapi.items import GosugamersapiItem

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
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)

        item = GosugamersapiItem()
                
        players = hxs.select('//div[@class="cont_middle"]//table//font//a/text()').extract()
        item['playerOne'] = players[0]
        item['playerTwo'] = players[1]
        
        countries = hxs.select('//div[@class="cont_middle"]//table//td[@class="cont_middle_alt"]//img/@title').extract()
        item['playerOneCountry'] = countries[0]
        item['playerTwoCountry'] = countries[1]
        
        item['tournament'] = hxs.select('//div[@class="cont_middle"]//table//b//a/text()').extract()

        item['time'] = hxs.select('//div[@class="cont_middle"]//table//span/@title').extract()
        
        return item

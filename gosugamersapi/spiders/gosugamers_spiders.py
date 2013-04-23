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
        
        #links = hxs.select('//div[@id="box_latest_gosubets_upcoming_matches"]')
        
        #print links.select('.//a/@href')
        players = hxs.select('//div[@class="cont_middle"]//table//font//a/text()').extract()
        print players[0] + " VS " + players[1]

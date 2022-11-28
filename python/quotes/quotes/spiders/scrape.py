import scrapy


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    allowed_domains = ['x.com']
    start_urls = ['http://x.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import TutorialItem
class MovieSpider(scrapy.Spider):
    name = "Movie"
    allowed_domains = ["ygdy8.net"]
    start_urls = []

    def start_requests(self):

        for x in xrange(1,154):
            MovieListUlr="http://www.ygdy8.net/html/gndy/dyzz/list_23_%d.html" % x
            self.start_urls.append(MovieListUlr)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)



    def parse(self, response):
        movie_links = response.selector.xpath('//a[@class="ulink"]/@href').extract()
        for movie_link in movie_links:
            movie_link = "http://www.ygdy8.net/"+movie_link
            yield Request(movie_link,callback=self.parse_item)
    def parse_item(self, response):
        item = TutorialItem()
        item['movie_name']= response.selector.xpath('//div[@class="title_all"]/h1/font/text()').extract()[0]
        item['download_link'] = response.selector.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').extract()[0]
        yield item
        

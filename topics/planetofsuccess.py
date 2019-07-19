import scrapy
import logging
import colorer
from scrapy.crawler import CrawlerProcess

# motivational
# class PsSpider(scrapy.Spider):
#     name='psspider'
#     start_urls = [
#         'http://www.planetofsuccess.com/blog/2015/the-75-most-motivational-quotes-ever-spoken/',
#     ]

#     def parse(self,response):
#         for quote in response.css('blockquote'):
#             logging.warning(quote.css('p::text').get())
#             logging.info(quote.css('strong::text').get())
#             yield {
#                 'quote': quote.css('p::text').get(),
#                 'author':quote.css('strong::text').get(),
#                 'categories': ['motivational']
#             }

#attitude
# class AtSpider(scrapy.Spider):
#     name='atspider'
#     start_urls = [
#         'http://www.wiseoldsayings.com/attitude-quotes/',
#     ]

#     def parse(self,response):
#         for quote in response.css('.quote'):
#             logging.warning(quote.css('p:nth-child(2) b::text').get())
#             logging.info(quote.css('p.author i::text').get())
#             yield {
#                 'quote': quote.css('p:nth-child(2) b::text').get(),
#                 'author':quote.css('p.author i::text').get(),
#                 'categories': ['attitude']
#             }
# life
# class LiSpider(scrapy.Spider):
#     name='Lispider'
#     start_urls = [
#         'https://www.curatedquotes.com/life-quotes/',
#     ]

#     def parse(self,response):
#         for quote in response.css('blockquote'):   
#             yield {
#                 'quote': quote.css('p::text').get(),
#                 'author':quote.css('cite::text').get(),
#                 'categories': ['life','lessons']
#             }
# 

# process = CrawlerProcess()
# process.crawl(PsSpider)
# process.crawl(AtSpider)
# process.start()
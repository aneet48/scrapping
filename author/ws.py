import scrapy
import logging
import colorer

# william shakespear
class WsSpider(scrapy.Spider):
    name='wsspider'
    start_urls = [
        'https://www.brainyquote.com/authors/william_shakespeare',
        'https://www.brainyquote.com/authors/abraham_lincoln',
        'https://www.brainyquote.com/authors/albert_einstein',
        'https://www.brainyquote.com/authors/anne_frank',
        'https://www.brainyquote.com/authors/bruce_lee',
        'https://www.brainyquote.com/authors/chanakya',
        'https://www.brainyquote.com/authors/dalai_lama',
        'https://www.brainyquote.com/authors/elvis_presley',
        'https://www.brainyquote.com/authors/galileo_galilei',
        'https://www.brainyquote.com/authors/helen_keller',
        'https://www.brainyquote.com/authors/henry_ford',
        'https://www.brainyquote.com/authors/j_k_rowling',
        'https://www.brainyquote.com/authors/jane_austen',
        'https://www.brainyquote.com/authors/leo_tolstoy',
        'https://www.brainyquote.com/authors/leonardo_da_vinci',
        'https://www.brainyquote.com/authors/marie_curie',
        'https://www.brainyquote.com/authors/mark_twain',
        'https://www.brainyquote.com/authors/oscar_wilde',
        'https://www.brainyquote.com/authors/pablo_picasso',
        'https://www.brainyquote.com/authors/paulo_coelho',
        'https://www.brainyquote.com/authors/rabindranath_tagore',
        'https://www.brainyquote.com/authors/robert_frost',
        'https://www.brainyquote.com/authors/stephen_hawking',
        'https://www.brainyquote.com/authors/steve_jobs',
        'https://www.brainyquote.com/authors/william_wordsworth',
    ]

    def parse(self,response):
        for quote in response.css('#quotesList .m-brick'):
            yield {
                'quote': quote.css('a.b-qt::text').get(),
                'author':quote.css('a.bq-aut::text').get(),
                'categories': quote.css('a.oncl_list_kc::text').getall()
            }

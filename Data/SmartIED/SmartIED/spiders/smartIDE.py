# -*- coding: utf-8 -*-
import scrapy
from SmartIDE.items import PullRequests

class SmartideSpider(scrapy.Spider):
    name = 'smartIDE'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/microsoft/vscode/pulls']

    def parse(self, response):
        prs = PullRequests()
        prs['PR_titles'] = []
        prs['PR_titles'] += response.css('div a.d-block::attr(aria-label)').getall()
        
        next_page = 'https://github.com/' + response.css('a.next_page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

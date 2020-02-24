# -*- coding: utf-8 -*-
import scrapy
from jiankang.items import JiankangItem

class AskSpider(scrapy.Spider):
    name = 'ask'
    allowed_domains = ['ask.39.net']
    start_urls = ['http://ask.39.net/news/3166-1.html']

    def parse(self, response):
        lis = response.xpath("//ul[@class='list_ask list_ask2']/li")
        for li in lis:
            href = li.xpath('.//p[@class="p1"]/a/@href').extract_first()
            url = "http://ask.39.net" + href
            yield scrapy.Request(url, callback=self.parse_detail)
        next_href = response.xpath('//div[@class="wrap_area clearfix"]/span[@class="pages"]//a[@class="next"]/@href').extract_first()
        if next_href is not None:
            next_url = "http://ask.39.net" + next_href
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item = JiankangItem()
        item['title'] = response.xpath('//div[@class="ask_cont"]/p[@class="ask_tit"]/text()').extract_first().strip()
        item['sex'] = response.xpath('//div[@class="ask_cont"]/p[@class="mation"]/span[1]/text()').extract_first()
        item['age'] = response.xpath('//div[@class="ask_cont"]/p[@class="mation"]/span[2]/text()').extract_first().strip()
        item['occur_time'] = response.xpath('//div[@class="ask_cont"]/p[@class="mation"]/span[3]/text()').extract_first().lstrip("发病时间：")
        item['ask'] = response.xpath('//div[@class="ask_cont"]//p[@class="txt_ms"]/text()').extract_first().strip()
        item['ask_time'] = response.xpath('//div[@class="ask_cont"]/p[@class="txt_nametime"]/span[2]/text()').extract_first()
        item['flags'] = response.xpath('//div[@class="ask_cont"]/p[@class="txt_label"]/span[not(@style="display: none")]/a/text()').extract()
        item['doctor'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]//div[@class="doc_txt"]/p[@class="doc_xinx"]/span[@class="doc_name"]/text()').extract_first()
        item['position'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]//div[@class="doc_txt"]/p[@class="doc_xinx"]/span[@class="doc_yshi"][1]/text()').extract_first()
        item['hospital'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]//div[@class="doc_txt"]/p[@class="doc_xinx"]/span[@class="doc_yshi"][2]/text()').extract_first()
        item['category'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]//div[@class="doc_txt"]/p[@class="doc_sc"]/span/text()').extract_first()
        item['answer'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]/p[@class="sele_txt"]/text()').extract_first()
        item['answer_time'] = response.xpath('//div[@class="selected"][1]/div[@class="sele_all marg_top"]/div[@class="doc_t_strip"]//p[@class="doc_time"]/text()').extract_first()
        yield item
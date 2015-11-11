# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import Request
from getgifs.items import GetgifsItem

import scrapy
import re

class ForgifsSpider(scrapy.Spider):
    name = "forgifs"
    allowed_domains = ["forgifs.com"]
    start_urls = (
        'http://forgifs.com/gallery/v/Funny/',
        'http://forgifs.com/gallery/v/Cats/',
        'http://forgifs.com/gallery/v/Dogs/',
        'http://forgifs.com/gallery/v/Cool/',
        'http://forgifs.com/gallery/v/Animals/',
        'http://forgifs.com/gallery/v/Sports/',
    )

    #获取Gif页的数据
    def parse_item(self, response):
        item = GetgifsItem()

        sel = response.xpath("//*[@id='gsContent']")

        item['gifs_name'] = sel.xpath("//h2/text()").extract()
        item['descript'] = sel.xpath("//p/text()").extract()
        # item['facebook_share'] =
        # item['tweet_share'] =
        # item['google_share'] =
        # item['total_share'] =
        item['img_src'] = sel.xpath("//img/@src").extract()
        item['keywords'] = sel.xpath("//*[@class='block-keyalbum-KeywordLinks']/a/text()").extract()
        # item.append()
        return item

    #主函数
    def parse(self, response):
        items = []

        url = "http://forgifs.com"
        img_urls = response.xpath("//td[@class='giItemCell']/div/a/@href").extract()
        for img_url in img_urls:
            img_url_all = url + str(img_url)
            yield Request(img_url_all, callback=self.parse_item)

        #下一页
        next_page = response.xpath("//a[@class='next']/@href").extract()[0]
        end_page = response.xpath("//a[@class='last']/@href").extract()[0]
        end_page_num = re.sub(r'[a-z]|[A-Z]|\/|\?.*page=|', "", str(end_page))

        if re.sub(r'[a-z]|[A-Z]|\/|\?.*page=|', "", str(next_page)) == end_page_num:
            return
        else:
            yield Request(url + next_page, callback=self.parse)


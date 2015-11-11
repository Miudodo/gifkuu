# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetgifsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gifs_name = scrapy.Field()
    descript = scrapy.Field()
    # facebook_share = scrapy.Field()
    # tweet_share = scrapy.Field()
    # google_share = scrapy.Field()
    # total_share = scrapy.Field()
    img_src = scrapy.Field()
    keywords = scrapy.Field()
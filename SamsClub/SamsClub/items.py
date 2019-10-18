# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    product_id = scrapy.Field()
    description = scrapy.Field()

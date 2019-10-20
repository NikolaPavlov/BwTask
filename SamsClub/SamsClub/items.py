import scrapy


class Product(scrapy.Item):
    product_id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()

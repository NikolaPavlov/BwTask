import scrapy


class Product(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    product_id = scrapy.Field()
    description = scrapy.Field()

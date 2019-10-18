import scrapy
from scrapy_splash import SplashRequest

from ..items import Product
from ..text_formaters import format_price


class EnergyDrinksSpider(scrapy.Spider):
    name = 'energy_drinks_spider'
    allowed_domains = ['www.samsclub.com']
    start_urls = ['https://www.samsclub.com/b/energy-drinks/1504']

    def parse(self, response):
        product_links = response.css( 'a.sc-product-card-pdp-link::attr(href)').getall()

        for product_link in product_links:
            link = 'https://www.samsclub.com' + product_link
            yield SplashRequest(url=link,
                                callback=self.parse_product,
                                endpoint='render.html',
                                args={"wait": 2})




        # follow pagination logic

        next_button = response.css('li.sc-pagination-next')
        if next_button is not None:
            next_page_url = 'https://www.samsclub.com/b/energy-drinks/1504?clubId=undefined&offset=48&searchCategoryId=1504&selectedFilter=all&sortKey=relevance&sortOrder=1'
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_title = response.css('title::text').get()

        product_price = response.css('span.Price-group::attr(title)').get()
        if product_price is None:
            product_price = 'not available'



        product_image_urls = []
        for img in response.css('.sc-image-viewer-thumb::attr(src)').getall():
            product_image_urls.append(img)
        print('---> start product ' + product_title + '<---')
        print(product_image_urls)
        print('---> finish product <---')



        product_id = response.css('.sc-product-header-item-number::text').re(r'Item # (.*)')
        if product_id:
            product_id = product_id[0]
        else:
            product_id = 'not available'

        product_description = response.css('.sc-full-description-long p::text').get()


        product = Product()
        product['title'] = product_title
        product['price'] = product_price
        product['image_urls'] = product_image_urls
        product['product_id'] = product_id
        product['description'] = product_description

        yield product

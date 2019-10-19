import scrapy
from scrapy_splash import SplashRequest

from ..items import Product
from ..text_formaters import format_price


MAIN_URL = 'https://www.samsclub.com'
SPLASH_WAIT_TIME = 2
NOT_AVAILABLE_MSG = 'not available'

class EnergyDrinksSpider(scrapy.Spider):
    name = 'energy_drinks_spider'
    allowed_domains = ['www.samsclub.com']
    start_urls = ['https://www.samsclub.com/b/energy-drinks/1504']

    products_offset = 0

    def parse(self, response):
        product_links = response.css( 'a.sc-product-card-pdp-link::attr(href)').getall()

        for product_link in product_links:
            link = MAIN_URL + product_link
            yield SplashRequest(url=link,
                                callback=self.parse_product,
                                endpoint='render.html',
                                args={"wait": SPLASH_WAIT_TIME})


        # follow pagination logic
        next_button = response.css('li.sc-pagination-next')
        if next_button:
            next_page_url = 'https://www.samsclub.com/b/energy-drinks/1504?clubId=undefined&offset={0}&searchCategoryId=1504&selectedFilter=all&sortKey=relevance&sortOrder=1'.format(str(self.products_offset))
            self.products_offset += 48
            yield SplashRequest(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_title = response.css('title::text').get() or NOT_AVAILABLE_MSG

        product_price_span = response.css('span.Price-group::attr(title)').get()
        product_price_formated = format_price(product_price_span) or NOT_AVAILABLE_MSG

        product_image_urls = []
        for img_url in response.css('.sc-image-viewer-thumb::attr(src)').getall():
            product_image_urls.append(img_url.replace('$DT_Thumbnail$', ''))

        product_id = response.css('.sc-product-header-item-number::text').re(r'Item # (.*)')
        product_id = int(product_id[0]) or NOT_AVAILABLE_MSG

        product_description = response.css('.sc-full-description-long p::text').get() or NOT_AVAILABLE_MSG

        product = Product()
        product['title'] = product_title
        product['price'] = product_price_formated
        product['image_urls'] = product_image_urls
        product['product_id'] = product_id
        product['description'] = product_description

        yield product

import scrapy
import re
from scrapy_splash import SplashRequest

from ..items import Product
from ..text_formaters import format_price
import SamsClub.user_settings as user_settings



class EnergyDrinksSpider(scrapy.Spider):
    name = 'energy_drinks_spider'
    allowed_domains = ['www.samsclub.com']
    start_urls = [user_settings.CATEGORY_TO_SCRAP_URL]

    products_offset = 0

    def parse(self, response):
        product_links = response.css( 'a.sc-product-card-pdp-link::attr(href)').getall()

        for product_link in product_links:
            link = 'https://' + self.allowed_domains[0] + product_link
            yield SplashRequest(url=link,
                                callback=self.parse_product,
                                args={"wait": user_settings.SPLASH_WAIT_TIME})

        # follow pagination logic
        next_button = response.css('li.sc-pagination-next')
        if next_button:
            # next_page_url = 'https://www.samsclub.com/b/energy-drinks/1504?clubId=undefined&offset={0}&searchCategoryId=1504&selectedFilter=all&sortKey=relevance&sortOrder=1'
            next_page_url = re.sub(r'offset=(\d+)', 'offset={0}', user_settings.NEXT_PAGE_URL)
            next_page_url = next_page_url.format(str(self.products_offset))
            self.products_offset += 48
            yield SplashRequest(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_title = response.css('title::text').get() or \
            user_settings.NOT_AVAILABLE_MSG

        product_price_span = response.css('span.Price-group::attr(title)').get()
        product_price_formated = format_price(product_price_span) or \
            user_settings.NOT_AVAILABLE_MSG

        product_image_urls = []
        for img_url in response.css('.sc-image-viewer-thumb::attr(src)').getall():
            product_image_urls.append(img_url.replace('$DT_Thumbnail$', ''))

        product_id = response.css('.sc-product-header-item-number::text').re(r'Item # (.*)')
        try:
            product_id_int = int(product_id[0])
        except:
            product_id = user_settings.NOT_AVAILABLE_MSG

        product_description = response.css('.sc-full-description-long p::text').get() or \
            user_settings.NOT_AVAILABLE_MSG

        product = Product()
        product['title'] = product_title
        product['price'] = product_price_formated
        product['image_urls'] = product_image_urls
        product['product_id'] = product_id
        product['description'] = product_description

        yield product
        self.logger.info('Yield: ' + product['title'])

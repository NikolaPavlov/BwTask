import re
import scrapy

from scrapy_splash import SplashRequest

from ..items import Product
from ..text_formaters import format_price
import SamsClub.user_settings as user_settings


class CategorySpider(scrapy.Spider):
    name = 'category_spider'
    allowed_domains = ['www.samsclub.com']
    start_urls = [user_settings.CATEGORY_TO_SCRAP_URL]

    # increase this counter by 48 in URL to go to the next page
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
            next_page_url = re.sub(r'offset=(\d+)', 'offset={0}', user_settings.NEXT_PAGE_URL)
            next_page_url = next_page_url.format(str(self.products_offset))
            self.products_offset += 48
            yield SplashRequest(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        # get product id
        product_id = response.css('.sc-product-header-item-number::text').re(r'Item # (.*)')
        try:
            product_id_int = int(product_id[0])
        except:
            product_id = user_settings.NOT_AVAILABLE_MSG

        # get product title
        product_title = \
            response.css('.sc-product-header-title-container::text').get() or \
            user_settings.NOT_AVAILABLE_MSG

        # get product price
        product_price_string = \
            response.xpath("//div[@class='sc-channel-container-channels']/div/div[1]/div/div/span/span/span[1]/text()").extract_first()
        product_price_formated = format_price(product_price_string) or \
            user_settings.NOT_AVAILABLE_MSG

        # get product description
        product_description = \
            response.css('.sc-full-description-long p::text').get() or \
            response.css('.sc-full-description-long::text').get() or \
            user_settings.NOT_AVAILABLE_MSG

        # get product images from the gallery
        product_image_urls = []
        for img_url in response.css('.sc-image-viewer-thumb::attr(src)').getall():
            product_image_urls.append(img_url.replace('$DT_Thumbnail$', ''))

        product = Product()
        product['product_id'] = product_id_int
        product['title'] = product_title
        product['price'] = product_price_formated
        product['description'] = product_description
        product['image_urls'] = product_image_urls

        yield product
        self.logger.info('Scraping ---> ' + product['title'])

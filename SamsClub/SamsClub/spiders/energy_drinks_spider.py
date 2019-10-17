import scrapy


class EnergyDrinksSpider(scrapy.Spider):
    name = 'energy_drinks_spider'
    allowed_domains = ['www.samsclub.com']
    start_urls = ['https://www.samsclub.com/b/energy-drinks/1504']

    def parse(self, response):
        product_links = response.css('a.sc-product-card-pdp-link::attr(href)').getall()

        for product_link in product_links:
            # yield {'link': 'https://www.samsclub.com' + product_link}
            link = 'https://www.samsclub.com' + product_link
            yield scrapy.Request(link, callback=self.parse_product)




        # follow pagination logic

        next_button = response.css('li.sc-pagination-next')
        if next_button is not None:
            print('debuging')
            next_page_url = 'https://www.samsclub.com/b/energy-drinks/1504?clubId=undefined&offset=48&searchCategoryId=1504&selectedFilter=all&sortKey=relevance&sortOrder=1'
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_title = response.css('div.sc-product-header-title-container::text').get()
        # product_price = response.css('span.Price-group::attr(title)').get()
        product_pictures = response.css('.sc-image-viewer-thumb::attr(src)').getall()
        # product_id = response.css('.sc-product-header-item-number::text').re(r'Item # (.*)')
        # product_description = response.css('.sc-full-description-long p::text').get()

        yield {
            'product': product_title,
            # 'price': product_price,
            'pictures': product_pictures,
            # 'id': product_id[0],
            # 'description': product_description.strip(),
        }

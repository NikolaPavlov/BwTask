from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

from slugify import slugify


class SamsclubPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # return [Request(x, meta={'product_name': slugify(item.get('title')) + '/'}) for x in item.get(self.images_urls_field, [])]
        print('DEBUGGGGG')
        print('item: ' + item['title'] + '***')
        # print('info: ' + str(info))

    def file_path(self, request, response=None, info=None):
        return 'full/%s.jpg' % (request.meta['product_name'])

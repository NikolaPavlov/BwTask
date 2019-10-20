# import os
from scrapy import Request
# from urllib.parse import urlparse
from scrapy.pipelines.images import ImagesPipeline

from slugify import slugify


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [
            Request(x, meta={'title': slugify(item['title'] + x)})
                for x in item.get('image_urls', [])
        ]

    def file_path(self, request, response=None, info=None):
        return '%s.jpg' % request.meta['title']



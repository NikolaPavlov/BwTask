import re

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from slugify import slugify


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [
            Request(x, meta= {'title': slugify(item['title'] + \
                get_image_number_from_url(x))}) \
                for x in item.get('image_urls', [])
        ]

    def file_path(self, request, response=None, info=None):
        return '%s.jpg' % request.meta['title']


def get_image_number_from_url(url):
    '''
    extract the number of the img from its url
    '''
    regex = '(\d+_\w)'
    image_num = re.findall(regex, url)
    if image_num:
        return '-' + image_num[0]

"""Bathak posts Spider"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PostSpider(CrawlSpider):
    """
    Fetching post data
    scrapy crawl posts_express -o posts.json -t json
    """
    name = "posts_express"
    start_urls = ['https://www.express.pk']
    allowed_domains = ["www.express.pk"]

    rules = [Rule(LinkExtractor(restrict_css='a[href*="/story/"]'), callback="parse_post")]

    def parse_post(self, response):
        """
        Parsing bathak Post data
        Args:
            response:

        Returns:

        """

        yield {
            'url': response.url,
            'data': response.css('div.story-content ::text').extract()
        }


"""Bathak posts Spider"""

import scrapy


class PostUrlSpider(scrapy.Spider):
    """
    Fetching Bathak Post by json urls list
    Command : scrapy crawl json_urls -o posts.json -t json
    """

    name = "urdupoint_urls"
    allowed_domains = ["www.urdupoint.com"]

    def start_requests(self):
        """

        Returns:

        """
        for number in range(6000, 1844104):
            url = f'https://www.urdupoint.com/daily/livenews/2019-02-28/news-{number}.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parsing bathak Post data
        Args:
            response:

        Returns:

        """

        yield {
            'url': response.url,
            'data': response.css('div.detail_txt ::text').extract()
        }

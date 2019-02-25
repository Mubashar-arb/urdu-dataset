"""Bathak posts Spider"""

from scrapy.spiders import SitemapSpider


class PostSpider(SitemapSpider):
    """
    Fetching post data
    scrapy crawl sitemaps_url -o posts.json -t json
    """
    name = "sitemaps_url"
    sitemap_urls = ['https://urdu.arynews.tv/sitemap.xml']
    allowed_domains = ["urdu.arynews.tv"]

    def parse(self, response):
        """
        Parsing bathak Post data
        Args:
            response:

        Returns:

        """
        yield {
            'url': response.url,
            'data': response.css('div.single-post-content ::text').extract()
        }

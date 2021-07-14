# pylint: disable=no-self-use
"""Module for news scraping from nawaiwaqt.com.pk"""

import datetime
import scrapy


class NewsSpider(scrapy.Spider):
    """News scraping spider for nawaiwaqt.com.pk/archives

    Run:
        scrapy crawl news -L ERROR
    """

    name = "news"
    allowed_domains = ["www.nawaiwaqt.com.pk"]
    date = datetime.date(2008, 11, 29)

    def start_requests(self):
        """Generate Starting Requests."""

        url = f"https://www.nawaiwaqt.com.pk/archives/{self.date.strftime('%d-%b-%Y')}"
        yield scrapy.Request(url, callback=self.parse, errback=self.error_cb)

    def error_cb(self, failure):
        """Callback for HTTP error.

        Args:
            failure: Failure object
        """

        response = failure.value.response
        raise Exception(f"Error Code {response.status} for {response.url}")

    def parse(self, response, **kwargs):
        """Parse response from nawaiwaqt archives.
        Args:
            response: HTML Response
        """

        available_categories = []
        for column in response.css("div.col-md-6.col-sm-12"):
            divs = column.xpath("div")
            i = 0
            while i < len(divs):
                # Skip categories which have no content for that date.
                # These categories have the following div above them. So, increment i twice.
                if divs[i].attrib["class"] == "alert-box secondary":
                    i += 1
                # Pass the divs with margin lines.
                elif divs[i].attrib["class"] != "gn-line mrgt-20":
                    available_categories.append(divs[i])
                i += 1

        available_categories_special = []
        column = response.css("div.sidebar-widget-1")
        divs = column.xpath("div")
        i = 3
        while i < len(divs)-1:
            # Skip categories which have no content for that date.
            # These categories have the following div above them. So, increment i twice.
            if divs[i].attrib["class"] == "alert-box secondary":
                i += 1
            else:
                available_categories_special.append(divs[i])
            i += 1

        # Extracting news item from each available category.
        for div in available_categories:
            category = div.css("div.section-title a::text").get()
            for item_url in div.css("article a"):
                yield response.follow(item_url,
                                      callback=self.parse_item,
                                      errback=self.error_cb,
                                      cb_kwargs={"category": category})

        # Extracting news item from each available special category.
        for div in available_categories_special:
            category = div.css("h5.widget-title a::text").get()
            for item_url in div.css("li div.content a"):
                yield response.follow(item_url,
                                      callback=self.parse_item,
                                      errback=self.error_cb,
                                      cb_kwargs={"category": category})

        print(self.date)
        if self.date < datetime.date.today():
            self.date += datetime.timedelta(days=1)

        url = f"https://www.nawaiwaqt.com.pk/archives/{self.date.strftime('%d-%b-%Y')}"
        yield scrapy.Request(url, callback=self.parse, errback=self.error_cb)

    def parse_item(self, response, category):
        """Extract news item content from the response page.
        Args:
            response: HTML Response
            category: news item category
        """

        item = {}
        item["category"] = category
        item["title"] = response.xpath(
            "//div[@class='head-post']/h2/text()").get()

        # Some pages have the content wrapped in p tags.
        # While some do not have p tags.
        # Whle some have both.
        # So, extracting all and joining it.
        description = [response.xpath(
            "//div[@class='entry-post mrgn-top']/text()"
        ).get()]
        description.extend(response.xpath(
            "//div[@class='entry-post mrgn-top']/p/text()"
        ).getall())
        item["description"] = " ".join(description)
        yield {
            "date": response.url.split('/')[-2],
            "id": response.url.split('/')[-1],
            "item": item
        }

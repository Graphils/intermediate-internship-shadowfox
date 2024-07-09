# first download scrapy
# Create a new project
# navigate your project directory on your terminal
# generate a spider for your scrapy to extract the code
# define the spider by extracting libraries

import  scrapy
from scrapy.http import Response

from typing import Any


class GoogleSider(scrapy.Spider):
    name = "google"
    start_urls = [
        "http://www.google.com"
    ]


    def parse(self, response):
        for result in response.css("div.g"):
            yield {
                "title": result.css("h3::text").get(),
                "link": result.css("a::attr(href)").get(),
                "snippet": result.css("span.aC0pRe::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not  None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse())
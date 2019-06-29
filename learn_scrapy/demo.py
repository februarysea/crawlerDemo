import scrapy


class adsSpider(scrapy.Spider):
    name = 'adsspider'
    start_urls = ['https://www.gumtree.com/flats-houses/london']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

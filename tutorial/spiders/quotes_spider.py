import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [ "http://quotes.toscrape.com/" ]

    def parse_old(self, response):
        self.logger.info('This is my first spider')
        quotes = response.xpath("//div[@class='quote']")
        quote = quotes[0].css(".text::text").getall()
        author = quotes[0].css(".author::text").getall()
        tags = quotes[0].css(".tag::text").getall()
        self.logger.info(quote)
        self.logger.info(author)
        self.logger.info(tags)

    def parse(self, response):
        self.logger.info('hello this is my first spider')
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        
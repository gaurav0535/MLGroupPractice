#Scrapy provides a powerful framework for extracting the data, processing it and then save it.
#can be installed using pip install scrapy

import scrapy
from scrapy.crawler import CrawlerProcess

#class here will have Spider object from scrapy passed here as argument to class
class MySpider(scrapy.Spider):
    #assign any name to your spider class and name variable
    name = "my_spider"

    #in start_requests function, specify the url of web site you want to scrape,can be multiple site also
    def start_requests(self):

        urls = ["http://quotes.toscrape.com/page/1"]
        #scrapy.Request will get the html code of the website and return in a response object which will be passed to
        #parser function using callback.callback points to parser3 function where we would extract desired info
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parser2)
    #response variable contains html code of the url
    def parser2(self, response):
        #get all the div elements having class as quote
        quotes = response.css("div.quote")
        #for each selector element extract the text
        for quote in quotes:
            text = quote.css('spam.text::text').extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("a.tag::text").extract()
        #for each quote return quote,it's author and tags
            yield {
                "quote": text,
                "author": author,
                "tags": tags
            }
        #extracx=t next page link from the html tags
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parser2)
    #
    # the below function can be ignored.
    def parser(self, response):
        page_id = response.url.split('/')[-2]
        filename = "quotes-%s.html" % page_id
        print(response.css("span::text").extract_first())
        autor_tag_dict = {}
        authors = response.css("small.author::text").extract()
        containers = response.css("div.quote")
        for container in containers:
            autor_tag_dict[container.css("small.author::text").extract()] = list(container.css("a.tag::text").extract())
        print(autor_tag_dict)
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log("saved file %s" % filename)

#initiate crawler process
process=CrawlerProcess()
process.crawl(MySpider)
process.start()


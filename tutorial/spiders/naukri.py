import scrapy


class NaukriSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.naukri.com/jobs-by-category',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        filename = 'urls.txt'
        urls = response.css('.multiColumn > a').xpath('@href').extract()
        f = open(filename, 'w+')
        for url in urls:
            # print(str(url))
            f.write(url + '\r\n')
        f.close()
        self.log('Saved file ')
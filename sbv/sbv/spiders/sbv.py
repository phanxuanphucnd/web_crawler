import scrapy
from scrapy import Request
from scrapy.selector import Selector
from ..items import SbvItem

class Sbv(scrapy.Spider):

    name = "sbv"
    allowed_domains = ["www.sbv.gov.vn"]

    start_urls = [
        "https://www.sbv.gov.vn/webcenter/portal/vi/menu/trangchu/ttsk"
    ]

    count = 0
    MAX_COUNT = 300

    def parse(self, response):
        urls = response.css("div.x29m a.xfu::attr(href)").getall()

        next_page = response.xpath('//*[@id="T:oc_9259810424region:gl5"]/@href').get()
        # next_page = [self.start_urls[0] + i for i in next_page]

        # next_page = ''.join(map(str, next_page))

        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        for url in urls:
            if self.count < self.MAX_COUNT:
                connect_to_url = response.urljoin(url)

                print(f"{'*'*100}\nURL: {connect_to_url}\n{'*'*100}")
                yield Request(connect_to_url, callback=self.parse_content)

            else:
                break

        if next_page and self.count < self.MAX_COUNT:
            next_url = response.urljoin(next_page)

            print(f"\n-----\nNEXT PAGE: {next_url}\n")

            yield Request(next_url, callback=self.parse)

    def parse_content(self, response):
        self.count += 1
        item = SbvItem()

        category = "Banking group"
        title = response.xpath('//*[@id="T:oc_7115552043region:pbl6"]/text()').get()
        create_date = response.xpath('//*[@id="T:oc_7115552043region:j_id__ctru16pc8"]/label/text()').get()
        berief_content = response.xpath('//*[@id="pbl20"]/text()').get()
        content = response.xpath('//*[@id="pbl21"]/div/p/span/text()').getall()

        # if title:
        item['title'] = title
        item['category'] = category
        item['create_date'] = create_date
        item['berief_content'] = berief_content
        item['content'] = content

        yield item
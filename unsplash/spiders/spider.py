from scrapy import Spider
from scrapy import Request
from unsplash.items import PicItem

total_page = 48
base_url = 'http://unsplash.com/?page='
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}


class UnSplashSpider(Spider):
    name = 'unsplash'
    allowed_domains = ["unsplash.com"]
    start_urls = []

    def start_requests(self):
        for page in range(1, total_page+1):
            request_url = base_url + str(page)
            self.start_urls.append(request_url)

        for url in self.start_urls:
            yield Request(url=url, headers=headers)

    def parse(self, response):
        pics = response.xpath('//div[@class="photo"]')
        items = []
        for pic in pics:
            pic_item = PicItem()
            pic_item['title'] = pic.xpath('a/@title').extract()
            pic_item['image_urls'] = pic.xpath('a/img/@src').extract()
            items.append(pic_item)
        return items

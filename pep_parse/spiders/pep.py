import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css(
            'section#numerical-index').css('tbody').css('tr')
        for pep_link in all_peps:
            href = pep_link.css('a::attr(href)').get()
            if href is not None:
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get().strip()
        data = {
            'number': name.split('–')[0].replace('PEP', '').strip(),
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS


class CSSSelector:
    TBODY = 'tbody'
    INDEX = 'section#numerical-index'
    TR = 'tr'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        all_peps = response.css(
            CSSSelector.INDEX).css(CSSSelector.TBODY).css(CSSSelector.TR)
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

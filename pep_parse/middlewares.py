from scrapy import signals
from typing import Iterable, Union, Optional, Type
from scrapy.http import Response, Request
from scrapy.spiders import Spider
from scrapy.crawler import Crawler


class PepParseSpiderMiddleware:
    '''Not all methods need to be defined. If a method is not defined,
    scrapy acts as if the spider middleware does not modify the
    passed objects.'''

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Type[Spider]:
        '''This method is used by Scrapy to create your spiders.'''
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response: Response, spider: Spider) -> None:
        ''' Called for each response that goes through the spider
        middleware and into the spider.'''
        return None

    def process_spider_output(self, response: Response,
                              result: Iterable[Union[Request, Item]],
                              spider: Spider
                              ) -> Iterable[Union[Request, Item]]:
        '''Called with the results returned from the Spider, after
        it has processed the response.
        Must return an iterable of Request, or item objects.'''
        for i in result:
            yield i

    def process_spider_exception(self, response: Response,
                                 exception: Exception, spider: Spider) -> None:
        '''Called when a spider or process_spider_input() method
        (from other spider middleware) raises an exception.'''
        pass

    def process_start_requests(self, start_requests: Request, spider: Spider):
        '''Called with the start requests of the spider, and works
        similarly to the process_spider_output() method, except
        that it doesn’t have a response associated.'''
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    '''Not all methods need to be defined. If a method is not defined,
    scrapy acts as if the downloader middleware does not modify the
    passed objects.'''

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Type[Spider]:
        '''This method is used by Scrapy to create your spiders.'''
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request,
                        spider: Spider) -> Optional[Request]:
        '''Called for each request that goes through the downloader
        middleware.'''
        return None

    def process_response(self, request: Request,
                         response: Response, spider: Spider) -> Response:
        '''Called with the response returned from the downloader.'''
        return response

    def process_exception(self, request: Request,
                          exception: Exception, spider: Spider) -> None:
        '''Called when a download handler or a process_request()
        (from other downloader middleware) raises an exception.'''
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)

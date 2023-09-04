from scrapy import signals


class PepParseSpiderMiddleware:
    '''Not all methods need to be defined. If a method is not defined,
    scrapy acts as if the spider middleware does not modify the
    passed objects.'''

    @classmethod
    def from_crawler(cls, crawler: any):
        '''This method is used by Scrapy to create your spiders.'''
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response: any, spider: any) -> None:
        ''' Called for each response that goes through the spider
        middleware and into the spider.'''
        return None

    def process_spider_output(self, response: any, result: any, spider: any):
        '''Called with the results returned from the Spider, after
        it has processed the response.
        Must return an iterable of Request, or item objects.'''
        for i in result:
            yield i

    def process_spider_exception(self, response: any,
                                 exception: any, spider: any) -> None:
        '''Called when a spider or process_spider_input() method
        (from other spider middleware) raises an exception.'''
        pass

    def process_start_requests(self, start_requests: any, spider: any):
        '''Called with the start requests of the spider, and works
        similarly to the process_spider_output() method, except
        that it doesn’t have a response associated.'''
        for r in start_requests:
            yield r

    def spider_opened(self, spider: any) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    '''Not all methods need to be defined. If a method is not defined,
    scrapy acts as if the downloader middleware does not modify the
    passed objects.'''

    @classmethod
    def from_crawler(cls, crawler: any):
        '''This method is used by Scrapy to create your spiders.'''
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: any, spider: any) -> None:
        '''Called for each request that goes through the downloader
        middleware.'''
        return None

    def process_response(self, request: any, response: any, spider: any):
        '''Called with the response returned from the downloader.'''
        return response

    def process_exception(self, request: any,
                          exception: any, spider: any) -> None:
        '''Called when a download handler or a process_request()
        (from other downloader middleware) raises an exception.'''
        pass

    def spider_opened(self, spider: any) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)

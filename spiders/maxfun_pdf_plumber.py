import scrapy
from scrapy.crawler import CrawlerProcess
import io
import re
import pdfplumber

maxfun_data = []

class MaxFunSpider(scrapy.Spider):
    name = 'Max_Fun_spider'
    
    def start_requests(self):
        url = 'https://maximumfun.org/transcripts/?_paged='
        for i in range(3):
            link = url + str(i)
            yield scrapy.Request(url=link,
                                 callback=self.parse_episode)
        
    def parse_episode(self, response):
        ep_links = response.xpath('//div[@class="search-page-loop-item-image"]/a/@href').extract()
        # print([link for link in ep_links]) # done, work
        for ep_link in ep_links:
            yield response.follow(url=ep_link,
                                  callback=self.parse_transcript)

    def parse_transcript(self, response):
        current_ep = []
        
        podcast = response.xpath('//div[@id="transcript-title"]/h1/text()').extract()[0].split(':')
        
        pod_ep = podcast[0]
        current_ep.append(pod_ep)
        
        pod_title = podcast[-1]
        current_ep.append(pod_title)
        
        text = response.xpath('//div[@class="container"]//div[@class="line"]/*//text()').extract()
        if len(text) == 0:
            pdf_link = response.xpath('//a[contains(@class,"btn-transcript-download")]/@href').re(r'https.*pdf')[0]
            yield response.follow(url=pdf_link, 
                                 callback=self.parse_pdf)
        else:
            current_ep.append(text)
            
        maxfun_data.append(current_ep)        
        
    
    def parse_pdf(self, response):
        path = 'current_pdf.pdf'
        print(response)
        # self.logger.info('Saving PDF %s', path)
        # with open(path, 'wb') as f:
        #    f.write(response.body)

        # pdf = pdfplumber.open(path)
        # page = pdf.pages[0]
        # print(page)

process = CrawlerProcess()
process.crawl(MaxFunSpider)
process.start()

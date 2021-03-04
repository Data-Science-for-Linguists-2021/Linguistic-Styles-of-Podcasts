import scrapy
from scrapy.crawler import CrawlerProcess
import re

freakonomics_data = []

# parses transcript links
class Freakonomics(scrapy.Spider):
    name = 'Freakonomics'
    
    def start_requests(self):
        url = 'https://freakonomics.com/archive/'
        yield scrapy.Request(url=url, callback=self.parse_episode)
        
    def parse_episode(self, response):
        transcript_links = response.xpath('//tr//span[@class="green-title"]/a/@href').extract() 
        # print([l for l in transcript_links])
        for link in transcript_links:
            yield scrapy.Request(url=link, 
                                  callback =self.parse_transcript)
    
    def parse_transcript(self, response):
        # Title - needes regex'd
        title = str(response.xpath('//h1[@class="single_title"]/text()').extract())
        clean_title = title[2:-3].split(' (Ep. ')
        ep_title = clean_title[0]
        ep_number = clean_title[1]
        
        # Text - NEEDS CLEANED!
        text = (response.css(' div.podcast_intro p > *::text').extract())[2:]
        freakonomics_data.append((ep_number, ep_title, text))

process = CrawlerProcess()
process.crawl(Freakonomics)
process.start()

print(freakonomics_data[0][0])

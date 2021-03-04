import scrapy
from scrapy.crawler import CrawlerProcess

# !!! Need to save podcast name (i.e. Mbmbam, tAZ, Sawbones)
# McElroy podcasts have embedded PDF transcripts, all others are plaintext

# parses transcript links

maxfun_data = []
mcelroy_data = []

class MaxFunSpider(scrapy.Spider):
    name = 'Max_Fun_spider'
    
    def start_requests(self):
        url = 'https://maximumfun.org/transcripts/?_paged='
        for i in range(60):
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
        title = response.xpath('//div[@id="transcript-title"]/h1/text()').extract()
        title = title[0].replace('TRANSCRIPT ','')
        print(title)
        print(type(title))

        text = ''
        while text == '':            
            text = response.xpath('//div[@class="line"]/*/text()').extract()
            # add more or else inifinite loop
        print(text)
        print(type(text))
process = CrawlerProcess()
process.crawl(MaxFunSpider)
process.start()

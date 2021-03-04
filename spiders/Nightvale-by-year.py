import scrapy
from scrapy.crawler import CrawlerProcess

W2NV_data = []

class W2NVspider(scrapy.Spider):
    name = 'Welcome-to-Nightvale'
    
    def start_requests(self):
        url = 'http://www.nightvalepresents.com/transcripts'
        yield scrapy.Request(url=url, callback=self.parse_year)

    # follow archive link to year
    def parse_year(self, response):
 
        archive_links = response.xpath('//li[@class="archive-group"]/a/@href').extract()
        
        baseurl = 'http://www.nightvalepresents.com'
        archive_links = [baseurl+l for l in archive_links if 'year=' in l]
        
        for link in archive_links:       # now follow the year-based links
            yield response.follow(url=link, callback=self.parse_episode)

        
    def parse_episode(self, response):
        transcript_links = response.xpath('//h1[@class="entry-title"]/a/@href').extract()
        for link in transcript_links:
            yield response.follow(url=link, 
                                  callback =self.parse_transcript)
    
    def parse_transcript(self, response):
        title = str(response.xpath('//h1[@itemprop="headline"]/a/@href').extract())
        # get string after last "/"
        title_clean = title.split('/')[-1].split('-')
        ep_number = title_clean[0]
        ep_title = ' '.join(title_clean[1:])[:-2]

        text = (response.css(' p::text').extract())[2:]
        # print(title)
        
        W2NV_data.append((ep_number, ep_title, text))   # append data
        
process = CrawlerProcess()
process.crawl(W2NVspider)
process.start()

print(len(W2NV_data))       # how many?
print(W2NV_data[0])         # first ep
print(list(zip(*ep_data))[0])   # look at ep numbers only 



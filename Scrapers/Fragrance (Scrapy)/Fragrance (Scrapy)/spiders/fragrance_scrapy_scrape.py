import scrapy
from fragrance_scrapy.items import fragrance_scrapyItem
from datetime import datetime
import re
#from scrapy.spider import Spider



class fragrance_scrapy(scrapy.Spider):
    name = "my_scraper_fragrance_scrapy"
    rotate_user_agent = True

    # First Start Url
    start_urls = ["XXXXX"]

    #npages = 5

    # This mimics getting the pages using the next button.
    #for i in range(5, npages + 5):
    #	start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")

    def parse(self, response):
        for href in response.xpath("//h3/a//@href"):
            # add the scheme, eg http://
            url  = "XXXXX" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = fragrance_scrapyItem()

        item['designer'] = response.xpath("//span[contains(@itemprop, 'brand')]/descendant::text()").extract()

        item['perfumeName'] = response.xpath("//span[contains(@itemprop, 'name')]/descendant::text()").extract()
        if item['designer'] in item['perfumeName']:
            item['perfumeName'].strip(item['designer'])

        item['sex'] = response.xpath("//span[contains(@itemprop, 'name')]/descendant::text()").extract().split('for ')[1]

        item['mainAccord1'] = response.xpath("//span[contains(@style, 'position: relative; font-weight: bold; z-index: 60;')]/descendant::text()").extract()
        item['mainAccord2'] = response.xpath("//span[contains(@style, 'position: relative; font-weight: bold; z-index: 60;')]/descendant::text()").extract()
        item['mainAccord3'] = response.xpath("//span[contains(@style, 'position: relative; font-weight: bold; z-index: 60;')]/descendant::text()").extract()
        item['mainAccord4'] = response.xpath("//span[contains(@style, 'position: relative; font-weight: bold; z-index: 60;')]/descendant::text()").extract()
        item['mainAccord5'] = response.xpath("//span[contains(@style, 'position: relative; font-weight: bold; z-index: 60;')]/descendant::text()").extract()

        item['haveRating'] = response.xpath("//span[contains(@style, 'font-sizeL 10px;')]/descendant::text()").extract().split('I have it:&nbsp;')[1].lstrip().split(' ')[0]
        item['hadRating'] = response.xpath("//span[contains(@style, 'font-sizeL 10px;')]/descendant::text()").extract().split('I had it:&nbsp;')[1].lstrip().split(' ')[0]
        item['wantRating'] = response.xpath("//span[contains(@style, 'font-sizeL 10px;')]/descendant::text()").extract().split('I want it:&nbsp;')[1].lstrip().split(' ')[0]
        item['signatureRating'] = response.xpath("//span[contains(@style, 'font-sizeL 10px;')]/descendant::text()").extract().split('My signature:&nbsp;')[1].lstrip().split(' ')[0]

        item['perfumeRating'] = response.xpath("//span[contains(@itemprop, 'ratingValue')]//descendant::text()").extract()
        item['numberVotes'] = response.xpath("//span[contains(@itemprop, 'ratingCount')]/descendant::text()").extract()

        item['longevityPoor'] = response.xpath("//tr/td[contains(@style, 'width: 20px')]/descendant::text()").extract()
        item['longevityWeak'] = response.xpath("//tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()
        item['longevityModerate'] = response.xpath("//tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()
        item['longevityLong'] = response.xpath("//tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()
        item['longevityVeryLong'] = response.xpath("//tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()

        item['sillageSoft'] = response.xpath("//table[contains(@class, 'voteLS sil')]/tr/td[contains(@style, 'width: 20px')]/descendant::text()").extract()
        item['sillageModerate'] = response.xpath("//table[contains(@class, 'voteLS sil')]/tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()
        item['sillageHeavy'] = response.xpath("//table[contains(@class, 'voteLS sil')]/tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()
        item['sillageEnormous'] = response.xpath("//table[contains(@class, 'voteLS sil')]/tr/td[contains(@class, 'ndSum')]/descendant::text()").extract()

        item['consumerMainNoteType1'] = response.xpath("//div[contains(@id, 'userMainNotes')]/@title").extract()


        # Getting Campaign Title
        #item['campaignTitle'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[0].strip()

        # Getting Amount Raised
        #item['amountRaised']= response.xpath("//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()

        # Goal
        #item['goal'] = " ".join(response.xpath("//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()

        # Currency Type (US Dollar Etc)
        #item['currencyType'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()

        # Campaign End (Month year etc)
        #item['endDate'] = "".join(response.xpath("//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()

        # Number of contributors
        #item['numberContributors'] = response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()

        # Getting Story
        #story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
        #story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
        #item['story']  = " ".join(story_list)

        # Url (The link to the page)
        #item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

        yield item

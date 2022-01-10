# encoding:utf-8

# scrapy crawl 98_scrapy -o movies.csv

import scrapy
import pandas as pd
import datetime
video_data=pd.read_csv("video_data.csv")

class v_spider(scrapy.Spider):
    name = 'v_spider'
    start_urls=['https://rewrfsrewr.xyz/forum-103-1.html']
    def parse(self, response):
        for next_page in [a.attrib["href"] for a in response.css("a.s.xst")]:
            next_page=response.urljoin(next_page)
            #print(next_page) 
            yield scrapy.Request(next_page,callback= self.prase_thread)
    def prase_thread(self,response):
        global video_data
        title=response.css("h1.ts span#thread_subject::text").get()
        mag_url=response.css("div.blockcode li::text").get()
        time=datetime.datetime.now()
        upload=""
        print(title)
        print(mag_url)
        #s="你好"
        #u=s.decode('utf-8')

        
        if not title in video_data['title'].values and mag_url:
            new_video=pd.DataFrame({
                'title':title,
                'mag_url':mag_url,
                'add_date':time,
                'upload':upload
            },index=[0])
            print(new_video)
            video_data= video_data.append(new_video,ignore_index=True)
            video_data.to_csv("video_data.csv",index=False)
        
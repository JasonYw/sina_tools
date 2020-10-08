# -*- coding: utf-8 -*-
import scrapy
import json
import re
import time

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['weibo.com']
    # start_urls = ['https://weibo.com',]


    # def start_requests(self):
    #     DEFAULT_REQUEST_HEADERS = {
    #         'authority': 'weibo.com',
    #         'path': '/lw15801367721/home?wvr=5',
    #         'method': 'GET',
    #         'scheme': 'https',
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'accept-language': 'zh-CN,zh;q=0.9',
    #         'cookie': 'wb_view_log=1920*12001; SINAGLOBAL=4128908716926.8135.1602076873682; SUHB=05i7VbbHM_Lu1b; wvr=6; wb_view_log_1842371671=1920*12001; ALF=1633614556; SSOLoginState=1602078557; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1Haoo0hGhy0XgiP4UKIAP5EOiI2hxL2fx85U_LXpKLVm7U.; SUB=_2A25yebcNDeRhGedG71AS9y_KzD2IHXVRDq_FrDV8PUJbmtAKLVmnkW9NUSDQUTz78Wt3-IKT0V-zXRW1peQfuZyO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5K-hUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; UOR=,,www.sina.com.cn; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; webim_unReadCount=%7B%22time%22%3A1602079303068%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
    #         'sec-fetch-dest': 'document',
    #         'sec-fetch-mode': 'navigate',
    #         'sec-fetch-site': 'same-origin',
    #         'sec-fetch-user': '?1',
    #         'upgrade-insecure-requests':'1',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    #     }   
    #     yield scrapy.Request(
    #         url='https://weibo.com/lw15801367721/home?wvr=5',
    #         callback=self.parse,
    #         headers=DEFAULT_REQUEST_HEADERS,
    #     )

    def start_requests(self):
        cookie_ ={}
        cookie_source ='SINAGLOBAL=4128908716926.8135.1602076873682; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1HaAYyKy0TPe0is8LuzbncnWmsceFisemirroErBdzo4XE.; login_sid_t=ad45a5773be646500a6674b8c5919239; cross_origin_proto=SSL; WBStorage=70753a84f86f85ff|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SSOLoginState=1602086286; SUB=_2A25yeZXMDeRhGedG71AS9y_KzD2IHXVRDoAErDV8PUNbmtAKLUT6kW9NUSDQUU3lw9W21MI_I55IBIu8F8TmHs8I; SUHB=0sqA4K-2aIaVAQ; ALF=1633622300; wvr=6; webim_unReadCount=%7B%22time%22%3A1602086305224%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
        for i in cookie_source.split(";"):
            key_ =i.split("=")[0]
            value_=i.split("=")[1]
            cookie_[key_] =value_
        headers = {
            'authority': 'weibo.com',
            'method': 'GET',
            'scheme': 'https',
            #'cookie': 'wb_view_log=1920*12001; SINAGLOBAL=4128908716926.8135.1602076873682; SUHB=05i7VbbHM_Lu1b; wvr=6; wb_view_log_1842371671=1920*12001; ALF=1633614556; SSOLoginState=1602078557; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1Haoo0hGhy0XgiP4UKIAP5EOiI2hxL2fx85U_LXpKLVm7U.; SUB=_2A25yebcNDeRhGedG71AS9y_KzD2IHXVRDq_FrDV8PUJbmtAKLVmnkW9NUSDQUTz78Wt3-IKT0V-zXRW1peQfuZyO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5K-hUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; UOR=,,www.sina.com.cn; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; webim_unReadCount=%7B%22time%22%3A1602079303068%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        yield scrapy.Request(
            url="https://weibo.com/lw15801367721/profile?rightmod=1&wvr=6&mod=personnumber",
            callback=self.parse,
            headers=headers,
            cookies=cookie_,
            meta={'page_type':"article"}

        )

    def parse(self, response):
        if response.meta.get("page_type") == "article":
            mid_list =re.findall(r'fmid=\\"(\d+)\\',response.text)
            print(mid_list)
            # mid_list =[4557518854955716', '4557518833714147', '4557518824539817', '4557518812751125', '4557518804617208', '4557518791775718', '4557518788100945', '4557518779713570', '4557518767136811', '4557518754551355', '4557518745635708', '4557518737776686', '4557518729387567', '4557518724399183', '4557518716013485']
            for mid in mid_list:
                data={
                    'mid':mid
                }
                yield scrapy.FormRequest(
                    url='https://weibo.com/aj/mblog/del?ajwvr=6',
                    method='POST',
                    formdata=data,
                    callback=self.parse
                )
        else:
            print(response.text)

    
        
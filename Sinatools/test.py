import requests
import re
import time
import socket
import json
socket.setdefaulttimeout(2)

def set_time(headers_):
    uid =str(time.time()).replace(".","")[:13]
    a =re.findall(r'time%22%3A(\d+)',headers_['cookie'])[0] #time%22%3A
    headers_['cookie'] =headers_['cookie'].replace(a,uid)
    return headers_

def rf_time(data_str=None,data_str_list=None):
    if data_str != None:
        a =re.findall(r'=(\d{13})$',data_str)
        if  a != []:
            print(a)
            uid =str(time.time()).replace(".","")[:13]
            data_str =data_str.replace(a[0],uid)
            return data_str
        return data_str
    if data_str_list != None:
        uid =str(time.time()).replace(".","")[:13]
        new_data_str_list =[]
        for data_ in data_str_list:
            a =re.findall(r'=(\d{13})$',data_)
            if a==[]:
                new_data_str_list.append(data_)
                continue
            else:
                data_ =data_.replace(a[0],uid)
                new_data_str_list.append(data_)
        return new_data_str_list


def parse_follow(url):
    headers={
        'authority': 'weibo.com',
        'method': 'GET',
        'path':'/1842371671/follow?rightmod=1&wvr=6',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; SUHB=0sqA4K-2aIaVAQ; wvr=6; UOR=,,www.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KMhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; ALF=1633791844; SSOLoginState=1602255846; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1Han_-CFyK_MVxbO7J4mKf4j_uHz1v6B9JqnQPMdtUEa4k.; SUB=_2A25yhAu2DeRhGedG71AS9y_KzD2IHXVR8Hp-rDV8PUNbmtAKLUHxkW9NUSDQUQv4jWaucoUrIlo3KnvfDl86fj7D; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=8700353511096.788.1602255850926; ULV=1602255850951:6:6:6:8700353511096.788.1602255850926:1602146230082; webim_unReadCount=%7B%22time%22%3A1602256166566%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        'referer': 'https://www.sina.com.cn/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    headers['path'] =url.replace('https://weibo.com','')
    headers['cookie'] =rf_time(data_str=headers['cookie'])
    response =requests.get(url=url,headers=headers)
    name =re.findall(r'action-data=."uid=(\d+)&nick=([\w_-]+).">',response.text)
    for i in name:
        print(i)
        dict_={}
        dict_['uid'] =i[0]
        dict_['nick'] =i[1]
        f =open('follow_profil.json','a',encoding='utf-8',errors='ignore')
        f.write(json.dumps(dict_,ensure_ascii='false')+'\n')    


def parse_comment(url):
    headers={
        'authority': 'weibo.com',
        'path': '/comment/outbox?wvr=6',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1HaAYyKy0TPe0is8LuzbncnWmsceFisemirroErBdzo4XE.; login_sid_t=ad45a5773be646500a6674b8c5919239; cross_origin_proto=SSL; WBStorage=70753a84f86f85ff|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SSOLoginState=1602086286; SUB=_2A25yeZXMDeRhGedG71AS9y_KzD2IHXVRDoAErDV8PUNbmtAKLUT6kW9NUSDQUU3lw9W21MI_I55IBIu8F8TmHs8I; SUHB=0sqA4K-2aIaVAQ; ALF=1633622300; wvr=6; webim_unReadCount=%7B%22time%22%3A1602086305224%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        # 'sec-fetch-dest': 'document',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-user': '?1',
        # 'upgrade-insecure-requests':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    while True:
        print(url)
        headers['cookie'] =rf_time(data_str=headers['cookie'])
        response =requests.get(url,headers=headers)
        cid_list =re.findall(r'action-data=\\"cid=(\d+)\\"',response.text)
        if cid_list !=[]:
            print(cid_list)
            delete_comment(cid_list)
            time.sleep(1)
        if cid_list ==[]:
            url[-1] =str(int(url[-1])+1)
            break

def parse_delweibo(url):
    headers={
        'authority': 'weibo.com',
        'path': '/lw15801367721/home?wvr=5',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1HaAYyKy0TPe0is8LuzbncnWmsceFisemirroErBdzo4XE.; login_sid_t=ad45a5773be646500a6674b8c5919239; cross_origin_proto=SSL; WBStorage=70753a84f86f85ff|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SSOLoginState=1602086286; SUB=_2A25yeZXMDeRhGedG71AS9y_KzD2IHXVRDoAErDV8PUNbmtAKLUT6kW9NUSDQUU3lw9W21MI_I55IBIu8F8TmHs8I; SUHB=0sqA4K-2aIaVAQ; ALF=1633622300; wvr=6; webim_unReadCount=%7B%22time%22%3A1602086305224%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        # 'sec-fetch-dest': 'document',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-user': '?1',
        # 'upgrade-insecure-requests':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    while True:
        url =rf_time(url)
        print(url)
        headers =set_time(headers)
        response =requests.get(url=url,headers=headers)
        mid =re.findall(r'mid=\\"(\d+)\\',response.text)
        if mid ==[]:
            break
        else:
            delete_weibo(mid)
        time.sleep(1)

def parse_dellikestatue(url):
    headers={
        'authority': 'weibo.com',
        'path': '/1842371671/like?from=page_100505_profile&wvr=6&mod=like',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1HaAYyKy0TPe0is8LuzbncnWmsceFisemirroErBdzo4XE.; login_sid_t=ad45a5773be646500a6674b8c5919239; cross_origin_proto=SSL; WBStorage=70753a84f86f85ff|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SSOLoginState=1602086286; SUB=_2A25yeZXMDeRhGedG71AS9y_KzD2IHXVRDoAErDV8PUNbmtAKLUT6kW9NUSDQUU3lw9W21MI_I55IBIu8F8TmHs8I; SUHB=0sqA4K-2aIaVAQ; ALF=1633622300; wvr=6; webim_unReadCount=%7B%22time%22%3A1602086305224%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        # 'sec-fetch-dest': 'document',
        # 'sec-fetch-mode': 'navigate',
        # 'sec-fetch-site': 'same-origin',
        # 'sec-fetch-user': '?1',
        # 'upgrade-insecure-requests':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    while True:
        print(url)
        headers =set_time(headers)
        response =requests.get(url,headers=headers)
        mid_list =re.findall(r'version=mini&qid=heart&mid=(\d+)&loc=(page_\d+_home)&cuslike=1',response.text)
        mid =re.findall(r'version=mini&qid=heart&mid=(\d+)',response.text)
        if mid != []:
            print(mid)
            delete_pastlike(mid)
        if mid_list !=[]:
            print(mid_list)
            delete_like(mid_list)
        if mid_list ==[] and mid==[]:
            if 'https://weibo.com/1842371671/like?page=' in url:
                page =re.findall(r'page=(\d+)#',url)[0]
                nextpage =str(int(page)+1)
                url =url.replace('page='+page,'page='+nextpage)
                headers['path'] =url.replace('https://weibo.com','')
            else:
                url ='https://weibo.com/1842371671/like?page=2#_rnd1602159634835'
                url =rf_time(data_str=url)
                headers['path'] =url.replace('https://weibo.com','')
        time.sleep(1)


def delete_pastlike(mid_list):
    for mid in mid_list:
        headers_={
            'authority':'weibo.com',
            'method': 'POST',
            'path': '/aj/like/del?ajwvr=6',
            'scheme': 'https',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '20',
            'content-type':'application/x-www-form-urlencoded',
            'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; SUHB=0sqA4K-2aIaVAQ; wvr=6; wb_view_log_1842371671=1920*12001; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5K2hUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; ALF=1633679219; SSOLoginState=1602143225; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1Ha4vl2Ak1mj9kBIjiXn91YITGxx8dML6I839EUxxHUCpQ.; SUB=_2A25yerOpDeRhGedG71AS9y_KzD2IHXVR8aJhrDV8PUNbmtAKLRCmkW9NUSDQUZNKfjL6GCgBIgbGg3e9mBpBM0QQ; _s_tentry=www.sina.com.cn; UOR=,,www.sina.com.cn; Apache=4707611519632.659.1602143242096; ULV=1602143242116:3:3:3:4707611519632.659.1602143242096:1602079278645; webim_unReadCount=%7B%22time%22%3A1602143242136%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
            'origin':'https://weibo.com',
            'referer': 'https://weibo.com/lw15801367721/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data ={
                'mid':mid,
        }
        headers_['cookie'] =rf_time(data_str=headers_['cookie'])
        response =requests.post(url='https://weibo.com/aj/like/del?ajwvr=6',headers=headers_,data=data)
        print(response.text)
        # time.sleep(1) 



def delete_weibo(mid_list):
    '''
        删除自己的微博用的cookie
        需注意时间戳
    '''
    for mid in mid_list:
        headers_={
            'authority':'weibo.com',
            'method': 'POST',
            'path': '/aj/mblog/del?ajwvr=6',
            'scheme': 'https',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '20',
            'content-type':'application/x-www-form-urlencoded',
            'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; SUHB=0sqA4K-2aIaVAQ; wvr=6; wb_view_log_1842371671=1920*12001; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5K2hUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; ALF=1633679219; SSOLoginState=1602143225; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1Ha4vl2Ak1mj9kBIjiXn91YITGxx8dML6I839EUxxHUCpQ.; SUB=_2A25yerOpDeRhGedG71AS9y_KzD2IHXVR8aJhrDV8PUNbmtAKLRCmkW9NUSDQUZNKfjL6GCgBIgbGg3e9mBpBM0QQ; _s_tentry=www.sina.com.cn; UOR=,,www.sina.com.cn; Apache=4707611519632.659.1602143242096; ULV=1602143242116:3:3:3:4707611519632.659.1602143242096:1602079278645; webim_unReadCount=%7B%22time%22%3A1602143242136%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
            'origin':'https://weibo.com',
            'referer': 'https://weibo.com/lw15801367721/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data ={
            'mid':mid,
        }
        headers_['cookie'] =rf_time(data_str=headers_['cookie'])
        response =requests.post(url='https://weibo.com/aj/mblog/del?ajwvr=6',headers=headers_,data=data)
        print(response.text)
        # time.sleep(1) 


def delete_like(mid_list):
    url ='https://weibo.com/aj/v6/like/add?ajwvr=6&__rnd=1602154325679'
    headers ={
        'authority':'weibo.com',
        'method': 'POST',
        'path': '/aj/v6/like/add?ajwvr=6&__rnd=1602152773532',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'login_sid_t=37005e95852b3ba6eb4864c19fef56c0; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=8606351777135.461.1602145365072; SINAGLOBAL=8606351777135.461.1602145365072; ULV=1602145366076:1:1:1:8606351777135.461.1602145365072:; wb_view_log=1920*12001; SUB=_2A25yeqbBDeRhGedG71AS9y_KzD2IHXVR8Z8JrDV8PUNbmtAKLU2skW9NUSDQURUW48X3ewVTLsScNokE7HIfXehm; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SUHB=079iifT505sEVw; ALF=1633683985; SSOLoginState=1602147985; wvr=6; wb_view_log_1842371671=1920*12001; webim_unReadCount=%7B%22time%22%3A1602152762859%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        'origin': 'https://weibo.com',
        'referer': 'https://weibo.com/1842371671/like?from=page_100505_profile&wvr=6&mod=like',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
        'x-requested-with': 'XMLHttpRequest',
    }
    for mid in mid_list:
        data={
            'version':'mini',
            'qid':'heart',
            'mid':mid[0],
            'loc':mid[1],
            'cuslike':'1',
        }
        d_header =rf_time(data_str_list=[headers['cookie'],headers['path'],url])
        headers['cookie']=d_header[0]
        headers['path']=d_header[1]
        url=d_header[2]
        response =requests.post(url,headers=headers,data=data)
        print(response.text)
        # time.sleep(1)

def delete_comment(cid_list):
    headers ={
        'authority':'weibo.com',
        'method': 'POST',
        'path': '/aj/comment/del?ajwvr=6&__rnd=1602164584296',
        'scheme': 'https',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'login_sid_t=37005e95852b3ba6eb4864c19fef56c0; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=8606351777135.461.1602145365072; SINAGLOBAL=8606351777135.461.1602145365072; ULV=1602145366076:1:1:1:8606351777135.461.1602145365072:; wb_view_log=1920*12001; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SUHB=079iifT505sEVw; ALF=1633683985; SSOLoginState=1602147985; wvr=6; wb_view_log_1842371671=1920*12001; SUB=_2A25ye3-fDeRhGedG71AS9y_KzD2IHXVR8dZXrDV8PUNbn9AKLUrwkW9NUSDQUTUohjcIBQz1DlQqpUt4eOiM0m3l; webim_unReadCount=%7B%22time%22%3A1602165302918%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
        'origin': 'https://weibo.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
        'x-requested-with': 'XMLHttpRequest',
    }
    url ='https://weibo.com/aj/comment/del?ajwvr=6&__rnd=1602164584296'
    for cid in cid_list:
        data ={
            'cid': cid,
            '_t': '0',
        }
        d_header =rf_time(data_str_list=[url,headers['cookie']])
        url =d_header[0]
        headers['path'] =d_header[0].replace("https://weibo.com","")
        headers['cookie'] =d_header[1]
        response =requests.post(url,headers=headers,data=data)
        print(response.text)


# def run():
#     '''
#         登录从cookie
#     '''
#     headers={
#         'authority': 'weibo.com',
#         'path': '/lw15801367721/home?wvr=5',
#         'method': 'GET',
#         'scheme': 'https',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'cookie': 'SINAGLOBAL=4128908716926.8135.1602076873682; wb_view_log_1842371671=1920*12001; _s_tentry=www.sina.com.cn; Apache=3160177508868.458.1602079278635; ULV=1602079278645:2:2:2:3160177508868.458.1602079278635:1602076873687; SCF=Apaw2tMwErdlFxptmHvBkH071Hh-B-tf-_2fGAvcU1HaAYyKy0TPe0is8LuzbncnWmsceFisemirroErBdzo4XE.; login_sid_t=ad45a5773be646500a6674b8c5919239; cross_origin_proto=SSL; WBStorage=70753a84f86f85ff|undefined; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFCiCXXUA6zymn5OA4l3Ge5JpX5KzhUgL.Fo2RShz0S02cS022dJLoIEnLxK-L1KnLB.qLxK-L1KnLB.qLxK-L1KeL1hnLxK-L1KeL1hykUcvN; SSOLoginState=1602086286; SUB=_2A25yeZXMDeRhGedG71AS9y_KzD2IHXVRDoAErDV8PUNbmtAKLUT6kW9NUSDQUU3lw9W21MI_I55IBIu8F8TmHs8I; SUHB=0sqA4K-2aIaVAQ; ALF=1633622300; wvr=6; webim_unReadCount=%7B%22time%22%3A1602086305224%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
#         # 'sec-fetch-dest': 'document',
#         # 'sec-fetch-mode': 'navigate',
#         # 'sec-fetch-site': 'same-origin',
#         # 'sec-fetch-user': '?1',
#         # 'upgrade-insecure-requests':'1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     urls_weibo =['https://weibo.com/lw15801367721/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1',]


def test():
    urls =[
        f'https://weibo.com/p/1005051842371671/myfollow?t=1&cfs=&Pl_Official_RelationMyfollow__93_page={page}#Pl_Official_RelationMyfollow__93'
        for page in range(1,7)
    ]
    for url in urls:
        parse_follow(url)
    # url ='https://weibo.com/comment/outbox?page=1'
    # parse_comment(url)
if __name__ == "__main__":
    test()
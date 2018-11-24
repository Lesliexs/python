import urllib.request
from bs4 import BeautifulSoup
import re
import os
import asyncio
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

content_url='http://www.biqukan.com/3_3876/'

url=content_url[:re.search('.com',content_url).span()[1]]
'网站链接,使用re.search匹配.com的位置，会返回一个tuple(18,22)即这个字符串开始和结束的位置'
def get_link():
    req=urllib.request.Request(content_url,headers=headers)
    html=urllib.request.urlopen(req)
    soup=BeautifulSoup(html.read(),'lxml')
    dl=soup.find('dl')
    start_tag=False
    start=time.time()
    threads=[]
    loop = asyncio.get_event_loop()
    for item in dl.contents: #获取dl下所有的标签信息
        if item=='\n': #当有换行时，跳出本次循环，到下次循环
            continue
        if item.string==u'《亵渎》正文卷': #这里使用string 和 text都可以
            start_tag=True
        elif start_tag: #使用异步io
            print(item)
            print(item.string+':'+url+item.a['href'])
            threads.append(get_contene(item.string,url+item.a['href']))
    loop.run_until_complete(asyncio.wait(threads,timeout=0.000001))
    loop.close()
    end=time.time()
    print('Cost time is:%d'%(end-start))
    #使用标准的爬虫方法爬取小说 self.get_contene(item.string,url+item.a['href'])

async def get_contene(title,text_url):

    chapter_req=urllib.request.Request(text_url,headers=headers)
    html=urllib.request.urlopen(chapter_req)
    soup=BeautifulSoup(html.read(),'lxml')
    detail=soup.find(attrs={'class':'showtxt','id':'content'})

    path='e:/workspace/book2'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths=path+'/'
    with open(paths+title+'.txt','w',encoding='utf-8') as f:
        lines= re.sub('[\xa0]+','\r\n\r\n',detail.text) #将'\xa0'(空格)替换成换行符
        lines= lines[:re.search(';?\[[笔趣看]?',lines).span()[0]] #去掉末尾不需要的内容
        f.write(lines)


if __name__=='__main__':
    get_link()
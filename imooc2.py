import urllib.request
from bs4 import BeautifulSoup

url='http://www.imooc.com'

req=urllib.request.Request(url)

response=urllib.request.urlopen(req)

soup=BeautifulSoup(response.read(),"lxml")

course_div=soup.find('div',{'class':'container-types clearfix'})

course_names=course_div.find_all('h3',{'class':'course-card-name'})

#过滤掉获取内容中的标签信息
for course_name in course_names:
    print(course_name.text)
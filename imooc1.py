import urllib.request
from bs4 import BeautifulSoup

req=urllib.request.Request('http://www.imooc.com')

response=urllib.request.urlopen(req)

soup=BeautifulSoup(response.read(),"lxml")

course_div=soup.find('div',{'class':'clearfix types-content'})

course_names=course_div.find_all('h3',{'class':'course-card-name'})

print(course_names)
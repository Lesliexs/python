import urllib.request
from bs4 import BeautifulSoup

req=urllib.request.Request('http://imooc.com')

response=urllib.request.urlopen(req)

soup=BeautifulSoup(response.read(),"lxml")
course_names=soup.find_all('h3',{'class':'course-card-name'})
print(course_names)
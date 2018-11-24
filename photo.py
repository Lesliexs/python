import urllib.request
import re
import os
from bs4 import BeautifulSoup
import lxml


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('utf-8')

reg = r'src="(.+?\.jpg)" width' #非贪心法正则表达式
reg_img = re.compile(reg)
url='http://tieba.baidu.com/p/1753935195'

img_reason=reg_img.findall(get_html(url))

reg1=urllib.request.Request(url)
response1= urllib.request.urlopen(reg1)


soup=BeautifulSoup(response1.read(),'lxml')

soup_reason=soup.find('div',{'id':'post_content_35999670126'})
soup_reason1=soup_reason.find_all('img',pic_type='0') #爬取标签内部所有的属性

with open('/Users/xs/Desktop.爬图片.txt','w') as f:
    for reason in img_reason:
        f.write(reason+'\n')
    for reason1 in soup_reason1:
        f.write(reason1['src']+'\n') #只写入爬取的src内容

path='e:/workspace/img'
if not os.path.isdir(path):
    os.makedirs(path)
paths=path+'/'


# with open('/Users/xs/Desktop.爬图片.txt','r') as f:
#     lines=f.readlines()
#     i=0
#     for line in lines:
#         urllib.request.urlretrieve(line.strip(),'{}{}.jpg'.format(paths,i)) #urlretrieve实现下载,urlretrieve方法下(url,filename=None,reporthook=None,data=None)
#         #其中filename和reporthook是一个元组,data为到服务器的数据，返回一个包含两个元素的(filename,headers)的元组
#         i+=1






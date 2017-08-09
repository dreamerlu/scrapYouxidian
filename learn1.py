# input=input('what is your name')
# print(type(input))
# str='123'
# print(int(str))
# int_num=int(str)
# print(type(int_num))
# input=input('Enter your name: ')
# print('Hello ',input)
# hours=35
# rate=2.7522
# result=hours*rate
# result=round(result,2)
# print(result)
# a=17
# print(1/3)
# a=10
# b=10
# print(a is b)
# a='ww'
# b='ww'
# print(a is b)
# input=input('please input the integer number:\n')
# try:
#     temp_float=float(input)
#     print(temp_float)
# except:
#     print('input must be integer!\n')
# print(len(11))
# print(range(10))
# list=range(10)
# print(type(list))
import random
# for i in range(10):
#     x=random.random()
#     print(x)

# print(random.randint(5,10))
# t=[1,2,3,4,5]
# print(random.choice(t))
# total=0
# count=0
# average=0
# while True:
#     inp=input('Enter a number:')
#     if inp == 'done':
#         break
#     try:
#         inp = int(inp)
#     except:
#         print('Invalid input\n')
#         continue
#     total+=inp
#     count=count+1
# average=total/count
# print(total,count,average)

# # 能够正常运行
# input=input('Input something')
# #不能改正常运行,第二次循环会使得input函数被input字符串覆盖！
# for i in range(5):
#     input=input('Input please:')
# fruit='apple'
# print(fruit[:])
# print('In %d years, I have spotted %g %s' % (3,0.1,'dogs'))
# str='X-DSPAM-Confidence:0.8475'
# temp=str[str.find(':')+1:]
# result=float(temp)
# print(result,type(result))
# file=open('J:\mbox.txt')
# print(file)
# file = open('J:\mbox.txt')
# count=0
# for line in file:
#     if line.startswith('From:'):
#         line=line.rstrip()
#         print(line)
# file=open('J:/test.txt','w')
# str='write in the file\n'
# str1='write again!'
# file.write(str)
# file.write(str1)
# file.close()
# str='Hello world\n'
# print(repr(str))
# filepath='J:/mbox-short.txt'
# file=open(filepath)
# for line in file:
#     print(line.rstrip().upper())
# file.close()

# filepath='J:/mbox.txt'
# sum,count=0.0,0
# file=open(filepath)
# for line in file:
#     if line.startswith('X-DSPAM-Confidence'):
#         line=line.rstrip()
#         str=line.find(':')+1
#         str=line[str:]
#         number=float(str)
#         count=count+1
#         sum=sum+number
# file.close()
# print(count,sum)
# print('confidence:',sum/count)
# s='weilu'
# print(list(s))
# str='weilu is very happy'
# t=str.split()
# print(t)
# list=['weilu','is','lucky','haha']
# # list.pop(len(list)-1)
# del list[3]
# print(list)
# list='weilu-is-very-happy'
# delimit='-'
# print(list.split(delimit))
# t=[1,2,3,4,5]
# t.append(6)
# t+=[7]
# print(t)
# t=[1,2,3,4,5]
# def test_del(t):
#     list=t[1:]
# test_del(t)
# print(t)
# filepath='J:/romeo.txt'
# wordList=[]
# file=open(filepath)
# for line in file:
#     words=line.split()
#     for word in words:
#         if not wordList.__contains__(word):
#             wordList.append(word)
# wordList.sort()
# print(wordList)

# filePath='J:/mbox-short.txt'
# file=open(filePath)
# contactList=[]
# for line in file:
#     if line.startswith('From'):
#         temp=line.split()
#         contactList.append(temp[1])
# print(contactList)
# outputList=[]
# while True:
#     userInput=input()
#     if userInput == 'done':
#         break
#     try:
#         num=int(userInput)
#         outputList.append(num)
#     except:
#         continue
# print('max:',max(outputList),',min:',min(outputList))
# en2sp={'weilu':'love','something':'unknown'}
# print(en2sp)
# print(en2sp['weilu'])
# print('weilu' in en2sp)
# print('love' in en2sp.values())
# print(en2sp.get('weilu','nothing'))
# d={}
# word='brontosaurus'
# for alpha in word:
    # d[alpha]=d.get(alpha,0)+1
#     d[alpha]=d[alpha]+1
# print(d)
# filepath='J:/romeo.txt'
# dictionary=dict()
# try:
#     file=open(filepath)
#     for line in file:
#         line=line.split()
#         for word in line:
#             if word not in dictionary.keys():
#                 dictionary[word]=1
#             else:
#                 dictionary[word]+=1
#     print(dictionary)
# except:
#     print('File Error!')
#
# print(type(dictionary.keys()))
# import string
# filePath='J:/romeo-full.txt'
# dictionary={}
# try:
#     file=open(filePath)
#     for line in file:
#         line=line.rstrip()
#         line=line.translate(line.maketrans('', '', string.punctuation))
#         line=line.split()
#         for word in line:
#             if word not in dictionary:
#                 dictionary[word]=1
#             else:
#                 dictionary[word]+=1
# except:
#     print('File Exception')
# finally:
#     file.close()
#     print(dictionary)
#     print(dictionary['romeo'])
# filePath='J:/mbox-short.txt'
# dictionary=dict()
# # try:
# file=open(filePath)
# for line in file:
#     if line.startswith('From') and not line.startswith('From:'):
#         line=line.strip()
#         word=line.split()
#         word=word[2]
#         # print(word)
#         if word not in dictionary.keys():
#             dictionary[word]=1
#         else:
#             dictionary[word]+=1
# #
# file.close()
# print(dictionary)
# filePath='J:/mbox.txt'
# dictionary=dict()
# try:
#     file=open(filePath)
#     for line in file:
#         # print('success')
#         if line.startswith('From '):
#             line=line.rstrip()
#             line=line.split()
#             word=line[1]
#             if word not in dictionary:
#                 dictionary[word]=1
#             else:
#                 dictionary[word]+=1
# except:
#     print('fileException')
# finally:
#     file.close()
# print(dictionary)
# maxCount=0
# maxIndex=''
# for key in dictionary.keys():
#     if dictionary[key] > maxCount:
#         maxIndex=key
#         maxCount=dictionary[key]
# print(maxIndex,dictionary[maxIndex])
# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# print(type(words))
# print(words)
# words.sort(reverse=True)
# print(words)
# (a,b)=['weilu','haha']
# a,b=['weilu',['very','happy']]
# print(a,b)
# d={'weilu':56,'yangyan':11}
# t=list(d.items())
# print(t)
# for key,val in t:
#     print(key,val)
# import string
# filePath='J:/romeo-full.txt'
# dictionary=dict()
# try:
#     file=open(filePath)
#     for line in file:
#         line=line.translate(line.maketrans('','',string.punctuation))
#         line=line.strip()
#         line=line.lower()
#         line=line.split()
#         for word in line:
#             if word  not in dictionary:
#                 dictionary[word]=1
#             else:
#                 dictionary[word]+=1
#     words=list()
#     for key,value in list(dictionary.items()):
#         words.append((value,key))
#     words.sort(reverse=True)
#     for key,value in words[:10]:
#         print(key,value)
# except:
#     print('exception!!!')

# filePath='J:/mbox.txt'
# dictionary=dict()
# try:
#     file=open(filePath)
#     for line in file:
#         if line.startswith('From '):
#             line=line.split()
#             email=line[1]
#             if email not in dictionary:
#                 dictionary[email]=1
#             else:
#                 dictionary[email]+=1
# except:
#     print('file exception')
# finally:
#     file.close()
# mailList=list()
# for key,value in list(dictionary.items()):
#     mailList.append((value,key))
# mailList.sort(reverse=True)
# print(mailList[0])

# filePath='J:/mbox-short.txt'
# dictionary=dict()
# try:
#     file=open(filePath)
#     for line in file:
#         if line.startswith('From '):
#             line=line.rstrip()
#             line=line.split()
#             time=line[-2]
#             time=time.split(':')
#             hour=time[0]
#             if hour not in dictionary:
#                 dictionary[hour]=1
#             else:
#                 dictionary[hour]+=1
# except:
#     print('Exception')
# finally:
#     file.close()
# hourList=list(dictionary.items())
# hourList.sort()
# print(hourList)
# import re
# hand = open('J:/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x=re.findall('\S+@\S+',line)
#     if len(x)>0:
#         print(x,type(x))

# import re
# line='abcdddef3fas2f'
# # x=re.findall('[d,e,f,1,3]+',line)
# x=re.search('[d,e,f,1,3]+',line)
# print(x.group())

# import re
# hand = open('J:/mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.search('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)
# import re
# filePath='J:/mbox.txt'
# file=open(filePath)
# count=0
# for line in file:
#     line=line.strip()
#     x=re.findall('^Author',line)
#     # if x is not None:
#     #     print(x.group())
#     #     count=count+1
#     if x!= []:
#         print(x)
#         count=count+1
# print(count)

# import re
# filePath='J:/mbox.txt'
# file=open(filePath)
# count=0
# sum=0.0
# for line in file:
#     if line.startswith('New Revision'):
#         line=line.strip()
#         x=re.findall('[0-9]+',line)
#         sum+=int(x[0])
#         count=count+1
# print(sum/count)

# import socket
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data=mysock.recv(512)
#     if len(data)<1:
#         break;
#     print(data.decode())
# mysock.close()

# import socket
# import time
# HOST='data.pr4e.org'
# PORT=80
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect((HOST,PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""
#
# while True:
#     data=mysock.recv(5120)
#     if len(data)<1:
#         break
#     count=count+len(data)
#     picture=picture+data
# mysock.close()
# pos=picture.find(b'\r\n\r\n')
# print(picture[:pos].decode())
# picture=picture[pos+4:]
# fhand=open('J:/chyh.jpg','wb')
# fhand.write(picture)
# fhand.close()
# import urllib.request
# fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# import re
# test='<a href="http://www.dr-chuck.com/page2.htm">'
# x=re.findall('http://.*?',test)
# print(x)
# import urllib.request, urllib.parse, urllib.error
# import re
# # url = 'http://www.py4e.com/book.htm'
# url='https://www.hao123.com/?tn=99169695_s_hao_pg'
# html = urllib.request.urlopen(url).read()
# # print(html.decode())
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
#     print(link.decode())
# file=open('J:/try.txt','wb')
# file.write(links[-1])
# from bs4 import BeautifulSoup

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url='https://www.hao123.com/?tn=99169695_s_hao_pg'
# html = urllib.request.urlopen(url, context=ctx).read()
# # html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

# import urllib.request, urllib.parse, urllib.error
# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
# fhand = open('J:/cover3.jpg', 'wb')
# size = 0
# while True:
#     info = img.read(100000)
#     if len(info) < 1: break
#     size = size + len(info)
#     fhand.write(info)
# print(size, 'characters copied.')
# fhand.close()

# import xml.etree.ElementTree as ET
# data = '''
# <person>
# <name>Chuck</name>
# <phone type="intl">
# +1 734 303 4456
# </phone>
# <email hide="yes"/>
# </person>'''
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
# <users>
# <user x="2">
# <id>001</id>
# <name>Chuck</name>
# </user>
# <user x="7">
# <id>009</id>
# <name>Brent</name>
# </user>
# </users>
# </stuff>
# '''
# stuff=ET.fromstring(input)
# lst=stuff.findall('users/user')
# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get("x"))

# import json
# data = '''
# [
# { "id" : "001",
# "x" : "2",
# "name" : "Chuck"
# } ,
# { "id" : "009",
# "x" : "7",
# "name" : "Chuck"
# }
# ]
# '''
# info=json.loads(data)
# for item in info:
#     print('name',item['name'])
#     print('id',item['id'])
#     print('Attribute',item['x'])

# import urllib.request, urllib.parse, urllib.error
# import json
# # Note that Google is increasingly requiring keys
# # for this API
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#     print(json.dumps(js, indent=4))
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)

# import urllib
# import socket
# mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysocket.connect(('ws.webxml.com.cn',80))
# cmd='GET /WebServices/MobileCodeWS.asmx/getMobileCodeInfo?mobileCode=13865120771&userID= HTTP/1.1'.encode()
# mysocket.send(cmd)
# while True:
#     data = mysocket.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysocket.close()

#

# from xml.dom import minidom
# xmldoc = minidom.parse('J:/xmlfile.xml')
# itemlist = xmldoc.getElementsByTagName('string')
# print(len(itemlist))
# # print(itemlist[0].attributes['name'].value)
# # for s in itemlist:
# #     print(s.attributes['name'].value)
# # open('J:/test.txt','w').write(''.join(str(e)+'   ' for e in dir(itemlist[0])))
# test=itemlist[0]
# print(test._get_attributes())

#

# import xml.etree.ElementTree as ET
# # data = '''
# # <person>
# # <string>Chuck</string>
# #
# # </person>
# # '''
# data='''
# <ArrayOfString id='fuck'>
# <string>Chuck</string>
# </ArrayOfString>
# '''
# tree = ET.fromstring(data)
# print('Name:', tree.find('string').text)
# # print('Attr:', tree.find('email').get('hide'))

# import re
# filePath='J:/xmlfile.xml'
# file=open(filePath,encoding='utf-8')
# toFile=open('J:')
# for line in file:
#     result=re.findall('<string>(.+)</string>',line)
#     if len(result)>0:
#         print(result[0])

# import urllib.request
# import json
# url='https://api.douban.com/v2/book/1220562'
# content=urllib.request.urlopen(url)
# data=content.read().decode()
# # print(data)
# data=json.loads(data)
# print(data['rating'])
# print(data['tags'][0]['name'])

# from urllib.parse import quote
# import urllib.request
# import  string
#
# url = r'http://baike.baidu.com/item/人民的名义/17545218'
# url = quote(url, safe = string.printable)   # safe表示可以忽略的字符
# web=urllib.request.urlopen(url)
# data=web.read().decode()
# print(data)

# import urllib.request
# from bs4 import BeautifulSoup
# import re
#
# url=r'http://www.youxidian.com/goods/search.html?keyword=%E7%94%9F%E6%AD%BB%E7%8B%99%E5%87%BB&server_id=0&game_id=0&cat_id=0&extra=&page=1'
# web=urllib.request.urlopen(url)
# data=web.read().decode()
# data=data.strip()
# soup=BeautifulSoup(data,'html.parser')
# test=soup.select('.intro_bx')
# file=open('J:/youxidiandata2.txt','w')
# for content in test:
#     soup1 = BeautifulSoup(str(content), 'html.parser')
#     test1 = soup1.select('a')
#     file.write(str(test1)+'\n-----------------------------------------\n')
#     print(test1)
# print(test)
# tags=soup('a')
# for tag in tags:
#     print(tag)
# result=re.findall('<li class="list_item">(.*)</li>',data)
# result=re.findall('<img src="(.*)"',data)
# result=re.findall('<script>(.*)</script>"',data,re.M)
# for url in result:
#     print(result)
# print(len(result))

# import re
# data='''
# <a href="/goods/1064765.html" target="_blank">
# <img src="http://yxd.flashgame163.com/images/bill.png"/>
#                         双线1和电信1低价卖了
#                                                 <img src="../images/pic_num.jpg" style="height:auto;width:auto;margin-left:5px;/">
# </img></a>
# '''
# test=re.findall('/>(.*)<img',data,re.S)
# print(type(test))
# print(str(test[0]).strip())

# import re
# data='<li class="price top">&yen; 330.00                                                        </li>'
# result=re.findall('.([0-9]+.[0-9]+)',data)
# print(float(str(result[0])))

# import re
# data='<li class="price top">¥ 165.00                                                        </li>'
# # data='<li class="price top">¥165.00 </li>'
# result=re.findall('<li class="price top">¥.(\d+\.\d+).*</li>',data)
# print(result)

# import re
# data='''
# <li class="price top">¥ 288.00                                                            <p>上架时间：</p>
# <p>08-08 11:19:48</p>
# </li>
# '''
# result=re.findall('<li class="price top">¥.(\d+\.\d+).*',data)
# print(result)

# import urllib.request
# from bs4 import BeautifulSoup
# import re
#
# url=r'http://www.youxidian.com/goods/search.html?keyword=%E7%94%9F%E6%AD%BB%E7%8B%99%E5%87%BB&server_id=0&game_id=0&cat_id=0&extra=&page=1'
# web=urllib.request.urlopen(url)
# data=web.read().decode().strip()
# soup=BeautifulSoup(data,'html.parser')
# test=soup.select('.price')
# for content in test:
#     # print('part:',str(content))
#     content=str(content).strip()
#     # price=re.findall('<li class="price top">.([0-9]+.[0-9]+)\s.*</li>',content)
#     if content.__contains__('上架时间'):
#         result= re.findall('<li class="price top">¥.(\d+\.\d+).*', content)
#         print(result)
#         continue
#     result = re.findall('<li class="price top">¥.(\d+\.\d+).*</li>', content)
#     print(str(result))

# import re
# data='''
# </img></p>
#                                         库存：1<p>
# '''
# data='''
# <li class="stock">
#                                         正在交易中<p>
#
# '''
# data='''
#
#                         浏览次数：35</p>
# '''
# data='''
# <span class="info">生死狙击 / 电信三区</span>
# '''
# data='''
# <img src="http://yxd.flashgame163.com/images/bill.png"/>
#                         黄金加特林夺命双镰荣耀沙鹰弹弓
#                                             </a></h3>
# '''
# data='''
# <a href="/goods/1065573.html" target="_blank">
# <img src="http://yxd.flashgame163.com/images/bill.png"/>
#                         黄金砖块！恶灵末日，小鸡高爆！
#                                                 <img src="../images/pic_num.jpg" style="height:auto;width:auto;margin-left:5px;/"/>
# </a>
# '''
# data='''
# <a target="_blank" href="/goods/1065619.html">
#                         <img src="http://yxd.flashgame163.com/images/bill.png"/>
#                         黄金加特林夺命双镰荣耀沙鹰弹弓
#                                             </a></h3>
# '''
# result=re.findall('/>(.*?)<',data,re.S)
# result=str(result[0]).strip()
# print(result)
# result=result[-result.find('\r\n'):]
# result=result[1]
# result=str(result[0]).strip()

from bs4 import BeautifulSoup
import re
data='''
<div class="detail_msg mt15">
                                                                <p>
                                    卖号不易，且行且珍惜！                                </p>
                            </div>
                        </div>
                                                <div class="detail_goods_cont left" style="margin-top: 30px">
                            <div class="goods_des">
                                <h3>游戏店客服备注</h3>
                            </div>
                            <div class="detail_msg mt15">
                                <p>
                                    封禁两次                                </p>
                            </div>
                        </div>                    </div>
'''
# soup=BeautifulSoup(data,'html.parser')
# content=soup.select('.detail_msg')
# content=str(content)
# soup=BeautifulSoup(content,'html.parser')
# tags=soup('p')
# for tag in tags:
#     print(tag.text.strip())
# # print(content)

# import urllib.request
# from bs4 import BeautifulSoup
# import re
# descrUrl='http://www.youxidian.com/goods/1065578.html'
# web=urllib.request.urlopen(descrUrl)
# webcontent=web.read().decode().strip()
# soup = BeautifulSoup(webcontent, 'html.parser')
# description = soup.select('.detail_msg')
# print(description)

# import urllib.request
# # from bs4 import BeautifulSoup
# import re
# url=r'http://www.youxidian.com/goods/search.html?keyword=%E7%94%9F%E6%AD%BB%E7%8B%99%E5%87%BB&server_id=0&game_id=0&cat_id=0&extra=&page=1'
# web=urllib.request.urlopen(url)
# data=web.read().decode().strip()
# soup=BeautifulSoup(data,'html.parser')
# testContent=str(soup.select('.m_detail_pages'))
# soup=BeautifulSoup(testContent,'html.parser')
# tags=soup('a')
# for tag in tags:
#     print(tag.text)

# l=list(range(107))
# print(l)

# import sqlite3
# con=sqlite3.connect('J:/test.db')
# c=con.cursor()
# c.execute('''
#     create table t_yxdproduct(
#       id INT PRIMARY KEY NOT NULL ,
#       name TEXT,
#       href TEXT,
#       price INT,
#       stock INT,
#       pv INT,
#       gamezone TEXT,
#       description TEXT
#     );
# ''')
# con.commit()
# con.close()

import sqlite3
con=sqlite3.connect('J:/test.db')
cursor=con.cursor()
cursor.execute('''
    insert into t_yxdproduct (name,href,price,stock,pv,gamezone,description)
    VALUES ('黄金SCAR猎魔沙鹰双持蓝魔等','http://www.youxidian.com/goods/1065612.html',
    30,1,64,'电信一区','黄金SCAR猎魔沙鹰双持蓝魔等')
''')
con.commit()
con.close()
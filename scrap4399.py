import urllib.request
from bs4 import BeautifulSoup
import re
import sqlite3

class Product(object):
    def __init__(self,name,href,price,stock,pv,gamezone,description):
        self.__name=name
        self.__href=href
        self.__price=price
        self.__stock=stock
        self.__pv=pv
        self.__gamezone=gamezone
        self.__description=description
    def getAttr(self):
        return self.__name,self.__href,self.__price,self.__stock,self.__pv,self.__gamezone,self.__description


def getProductNameAndHref(content):
    soup = BeautifulSoup(content, 'html.parser')
    subcontent=soup.select('.intro_bx')
    subcontent=str(subcontent).strip()
    soup = BeautifulSoup(subcontent, 'html.parser')
    subcontent=soup('a')
    # name= re.findall('/>(.*)<img',str(subcontent), re.S)
    name=re.findall('/>(.*?)<',str(subcontent),re.S)
    name=str(name[0]).strip()
    # for getting product href
    # print(subcontent[0])
    href='http://www.youxidian.com'+str(subcontent[0].get('href')).strip()
    return name,href

def getProductPrice(content):
    soup=BeautifulSoup(content,'html.parser')
    subcontent=soup.select('.price')
    result=0
    for item in subcontent:
        # print('part:',str(content))
        item = str(item).strip()
        # price=re.findall('<li class="price top">.([0-9]+.[0-9]+)\s.*</li>',content)
        if item.__contains__('上架时间'):
            result = re.findall('<li class="price top">¥.(\d+\.\d+).*', item)
            continue
        result = re.findall('<li class="price top">¥.(\d+\.\d+).*</li>', item)
        result=int(float(str(result[0])))
    return result

def getProductStockAndPV(content):
    soup = BeautifulSoup(content, 'html.parser')
    subcontent = soup.select('.stock')
    subcontent=str(subcontent).strip()
    stock=re.findall('.库存：(\d)<p>',subcontent)
    pv=re.findall('.浏览次数：(\d+)</p>',subcontent)
    stock=int(str(stock[0]))
    pv=int(str(pv[0]))
    return stock,pv

def getProductGamezone(content):
    gamezone = re.findall('<span class="info">生死狙击 / (.+)</span>', content)
    return str(gamezone[0])

def getProductDecription(descrUrl):
    web=urllib.request.urlopen(descrUrl)
    webcontent=web.read().decode().strip()
    soup = BeautifulSoup(webcontent, 'html.parser')
    description = soup.select('.detail_msg')
    description=str(description)
    soup=BeautifulSoup(description,'html.parser')
    tags=soup('p')
    descrpList=list()
    for tag in tags:
        descrpList.append(tag.text.strip())
    message=''
    for item in descrpList:
        message=message+item+'\n'
    return message

def getTotalPages(data):
    soup = BeautifulSoup(data, 'html.parser')
    testContent = str(soup.select('.m_detail_pages'))
    soup = BeautifulSoup(testContent, 'html.parser')
    tags = soup('a')
    pageList=list()
    for tag in tags:
        infor=tag.text.strip()
        isNumber=True
        for alpha in infor:
            if not alpha.isdigit():
                isNumber=False
        if isNumber:
            pageList.append(int(infor))
    return max(pageList)

def writeToDB(data,cursor,con):
    cursor.execute('''
        insert into t_yxdproduct (name,href,price,stock,pv,gamezone,description) values (?,?,?,?,?,?,?)
    ''',data[:])
    con.commit()

#init zone
url=r'http://www.youxidian.com/goods/search.html?keyword=%E7%94%9F%E6%AD%BB%E7%8B%99%E5%87%BB&server_id=0&game_id=0&cat_id=0&extra=&page='
web=urllib.request.urlopen(url+'1')
data=web.read().decode().strip()
soup=BeautifulSoup(data,'html.parser')
testContent=soup.select('.list_item')
maxPage=getTotalPages(data)
#init database
con=sqlite3.connect('J:/test.db')
cursor=con.cursor()
# testContent=str(testContent).strip()


# Test
# print(maxPage)
# testContent=str(testContent[1]).strip()
# print(getProductNameAndHref(testContent))
# print(getProductPrice(testContent))
# print(getProductStockAndPV(testContent))
# print(getProductGamezone(testContent))
# print(getProductDecription('http://www.youxidian.com/goods/1065578.html'))
#     print(product.getAttr())
for i in range(96,maxPage+1,1):
    curUrl=url+str(i)
    web = urllib.request.urlopen(curUrl)
    data = web.read().decode().strip()
    soup = BeautifulSoup(data, 'html.parser')
    testContent = soup.select('.list_item')
    print('Current Page:',i,'\t-------------------------------------------')
    for content in testContent:
        try:
            content = str(content).strip()
            name, href = getProductNameAndHref(content)
            price = getProductPrice(content)
            stock, pv = getProductStockAndPV(content)
            gamezone = getProductGamezone(content)
            description = getProductDecription(href)
            product = Product(name, href, price, stock, pv, gamezone, description)
            print(product.getAttr())
            writeToDB(product.getAttr(),cursor,con)
        except:
            continue
con.close()



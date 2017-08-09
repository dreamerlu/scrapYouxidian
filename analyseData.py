import sqlite3
import operator
from operator import itemgetter
from collections import OrderedDict
import matplotlib.pyplot as plt
plt.rc('font', family='SimHei', size=8)
import numpy as np
con=sqlite3.connect('J:/test.db')
cursor=con.cursor()

gamezone={11:'联通一区',12:'联通二区',13:'联通三区',14:'联通四区',15:'联通五区',16:'联通六区',
              21:'电信一区',22:'电信二区',23:'电信三区',24:'电信四区',25:'电信五区',26:'电信六区',27:'电信七区',28:'电信八区'}
''' 分析不同区的商品数量 '''
def getZoneProductNumber():

    resultDict=dict()
    for key in gamezone.keys():
        result=cursor.execute('SELECT count(*) FROM t_yxdproduct WHERE gamezone=?',(gamezone[key],))
        for row in result:
            resultDict[key]=int(row[0])
    sorted_x = OrderedDict(sorted(resultDict.items(), key=itemgetter(1)))
    # 绘制柱状图
    xaix=list(gamezone.values())
    yaix=list(resultDict.values())
    plt.bar(range(len(gamezone)),yaix,tick_label=xaix)
    plt.show()

''' 分析各个区的最高售价、最低售价、平均值 '''
maxPrice,minPrice,avePrice=dict(),dict(),dict()
def getZonePrice():
    for key in gamezone.keys():
        result = cursor.execute('SELECT max(price),min(price),avg(price) FROM t_yxdproduct WHERE gamezone=?', (gamezone[key],))
        for row in result:
            maxPrice[key]=row[0]
            minPrice[key]=row[1]
            avePrice[key]=round(row[2],2)
    print(maxPrice,minPrice,avePrice)
    #  绘制多柱状图
    n_groups = len(gamezone.keys())
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    rects1 = plt.bar(index, tuple(maxPrice.values()), bar_width,
                     alpha=opacity,
                     color='b',
                     label='最高价')
    rects2 = plt.bar(index + bar_width, tuple(avePrice.values()), bar_width,
                     alpha=opacity,
                     color='r',
                     label='平均价')
    rects3 = plt.bar(index + bar_width*2, tuple(minPrice.values()), bar_width,
                     alpha=opacity,
                     color='g',
                     label='最低价')
    plt.xlabel('游戏区')
    plt.ylabel('价格')
    plt.title('出售价格分析')
    #决定了x轴每个单位中心刻度的位置
    plt.xticks(index + 2*bar_width / 2, tuple(gamezone.values()))
    plt.legend()
    plt.tight_layout()
    plt.show()

''' 测试区 '''
getZonePrice()
import sqlite3
import operator
from operator import itemgetter
from collections import OrderedDict
import matplotlib.pyplot as plt
con=sqlite3.connect('J:/test.db')
cursor=con.cursor()
''' 分析不同区的商品数量 '''
gamezone={11:'联通一区',12:'联通二区',13:'联通三区',14:'联通四区',15:'联通五区',16:'联通六区',
          21:'电信一区',22:'电信二区',23:'电信三区',24:'电信四区',25:'电信五区',26:'电信六区',27:'电信七区',28:'电信八区'}
resultDict=dict()
for key in gamezone.keys():
    result=cursor.execute('SELECT count(*) FROM t_yxdproduct WHERE gamezone=?',(gamezone[key],))
    for row in result:
        resultDict[key]=int(row[0])
sorted_x = OrderedDict(sorted(resultDict.items(), key=itemgetter(1)))
# 绘制柱状图
plt.rc('font', family='SimHei', size=8)
xaix=list(gamezone.values())
yaix=list(resultDict.values())
plt.bar(range(len(gamezone)),yaix,tick_label=xaix)
plt.show()

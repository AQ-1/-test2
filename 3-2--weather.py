# encoding=utf-8

import requests as req
res=req.get('https://weather.com/weather/monthly/l/97eb14db9945c4c1447710e459568a0da23b3748315729fb4674be7dc7443cad')
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')


wraper=soup.find(name='span', attrs={'classname': 'forecast-monthly__calendar'})
import math
def FtoC(f):
    return math.ceil((f-32)*5/9)
day_list=[]
hi_list=[]
low_list=[]
for cell in wraper.findChildren(recursive=False):
    date_tag=cell.find(attrs={'class': 'date'})
    hi_tag=cell.find(attrs={'class': 'temp hi'})
    low_tag=cell.find(attrs={'class': 'temp low'})
    if date_tag==None:
        break
    day_list.append(date_tag.text)
    hi_list.append(FtoC(int(hi_tag.text.replace('°', ''))))
    low_list.append(FtoC(int(low_tag.text.replace('°', ''))))


import numpy as np
import matplotlib.pyplot as plt
plt.gcf().set_size_inches(11, 5)
plt.plot(hi_list, 'red')
plt.plot(low_list, 'blue')
plt.xticks(np.arange(len(day_list)), day_list)
plt.ylim([min(low_list)-1,max(hi_list)+5])
plt.ylabel('°C')
plt.xlabel('day')
plt.legend(['high', 'low'], loc='upper left')
plt.show()

# encoding=utf-8

import requests as req
date='20200719'
stockNo='0051'
res=req.get(url='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&'+'date='+date+'&'+'stockNo='+stockNo)
import json
data=json.loads(res.text)
for i in data['data']:
    print(i)

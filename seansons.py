#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:11:28 2017

@author: jifeihe
"""
import pandas as pd
calendar_data=pd.read_csv('calendar.csv',sep=',')
calendar_data.head()

split=pd.DataFrame()
split['year']=pd.to_datetime(calendar_data['date']).dt.year
split['month']=pd.to_datetime(calendar_data['date']).dt.month
split['dayofweek']=pd.to_datetime(calendar_data['date']).dt.dayofweek
split.head()
new_calendar=calendar_data.join(split,on=None,how='left',sort=False)


#remove $ sign in price

new_calendar['price']=new_calendar['price'].str.replace('$','')
new_calendar['price']=pd.to_numeric(new_calendar['price'],errors='coerce')

#Data exploration
import seaborn as sn
import matplotlib.pyplot as plt
#%matplotlib inline
price_month=new_calendar[['month','price']]
price_month_mean=price_month.groupby('month').mean()
plot1=price_month_mean.plot(kind='bar')
plot1.set_xlabel('Month')
plot1.set_ylabel('Average price of listings ($)')
plot1
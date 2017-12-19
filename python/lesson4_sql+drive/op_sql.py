# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2017年   11 月  3 日
实现功能：第四次实训-数据库的基本操作
"""

import MySQLdb
import pandas as pd
import numpy as np
import datetime

db = MySQLdb.connect("localhost", "root", "123qwe", "mytrip")
cursor = db.cursor()
sql = "select t.record_time,max(t.vehicle_speed),t.engine_rpm from tb_iov_device_obd_41030402427 t where Device_ID='41030402427' GROUP BY t.record_time"
cursor.execute(sql)
results = cursor.fetchall()
results = pd.DataFrame(list(results), columns=['record_time', 'vehicle_speed', 'engine_rpm'])
i = 1
trip = 1
results['trip'] = 1
results['Time_diff'] = 0

print "大小是"
size = results.size / 5
print results.size
try:
    while i < size:
        t1 = str(results.iloc[i - 1, 0])
        t2 = str(results.iloc[i, 0])
        date_time1 = datetime.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        date_time2 = datetime.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        dif = (date_time2 - date_time1).total_seconds()
        if dif > 600:
            trip = trip + 1
        if dif > 0:
            results.loc[i, 'trip'] = trip
            results.loc[i, 'Time_diff'] = dif
        i += 1
    else:
        print "循环到头了"

except IndexError:
    print "越界错误："
    print i
else:
    print "无异常发生"

i = 0
while i < results.size / 5:
    if results.loc[i, 'trip'] < 0:
        results.loc[i, 'trip'] = 'BAD'
    i += 1

a = 0
b = 1
c = 2
# array = [0, 0, 0]
# ABS_Acceleration_Classify = [array] * (max(results['trip']) + 1)
ABS_Acceleration_Classify =[[0 for x in range(3)] for y in range(max(results['trip']) + 1)]
i = 1
j = 1
results['ABS_Acceleration'] = 0
results['ABS_Acceleration_Flag'] = 0
results.loc[0, 'ABS_Acceleration_Flag'] = 'a'
while i < results.size / 7:
    if results.loc[i, 'trip'] != j:
        j = results.loc[i, 'trip']
    spped_dif = results.loc[i, 'vehicle_speed'] - results.loc[i - 1, 'vehicle_speed']
    Acceleration = spped_dif / results.loc[i, 'Time_diff']
    ABS_Acceleration = abs(Acceleration)
    results.loc[i, 'ABS_Acceleration'] = ABS_Acceleration
    if ABS_Acceleration < 0.1:
        results.loc[i, 'ABS_Acceleration_Flag'] = 'a'
        ABS_Acceleration_Classify[j][a] += 1
    elif 0.1 <= ABS_Acceleration < 0.3:
        results.loc[i, 'ABS_Acceleration_Flag'] = 'b'
        ABS_Acceleration_Classify[j][b] += 1
    elif ABS_Acceleration >= 0.3:
        results.loc[i, 'ABS_Acceleration_Flag'] = 'c'
        ABS_Acceleration_Classify[j][c] += 1
    i += 1

d = 3
# array = [0, 0, 0, 0]
# Speed_Classify = [array] * (max(results['trip']) + 1)
Speed_Classify =[[0 for x in range(4)] for y in range(max(results['trip']) + 1)]
results['Speed_Flag'] = 0
i = 0
j = 1
while i < results.size / 8:
    if results.loc[i, 'trip'] != j:
        j = results.loc[i, 'trip']
    if results.loc[i, 'vehicle_speed'] < 5.6:
        results.loc[i, 'Speed_Flag'] = 'a'
        Speed_Classify[j][a] += 1
    if 5.6 <= results.loc[i, 'vehicle_speed'] < 11.1:
        results.loc[i, 'Speed_Flag'] = 'b'
        Speed_Classify[j][b] += 1
    if 11.1 <= results.loc[i, 'vehicle_speed'] < 16.7:
        results.loc[i, 'Speed_Flag'] = 'c'
        Speed_Classify[j][c] += 1
    if 16.7 <= results.loc[i, 'vehicle_speed']:
        results.loc[i, 'Speed_Flag'] = 'd'
        Speed_Classify[j][d] += 1
    i += 1

results['RPM_Flag'] = 0
# array = [0, 0, 0]
# RPM_Classify = [array] * (max(results['trip']) + 1)
RPM_Classify =[[0 for x in range(3)] for y in range(max(results['trip']) + 1)]
i = 0
j = 1
while i < results.size / 9:
    if results.loc[i, 'trip'] != j:
        j = results.loc[i, 'trip']
    if results.loc[i, 'engine_rpm'] < 1000:
        results.loc[i, 'RPM_Flag'] = 'a'
        RPM_Classify[j][a] += 1
    if 1000 <= results.loc[i, 'engine_rpm'] < 2000:
        results.loc[i, 'RPM_Flag'] = 'b'
        RPM_Classify[j][b] += 1
    if 2000 <= results.loc[i, 'engine_rpm']:
        results.loc[i, 'RPM_Flag'] = 'c'
        RPM_Classify[j][c] += 1
    i += 1

print results.head(5)
print results.tail(5)
j = 1
i = 0
trip_v = np.zeros(max(results['trip']) + 1)
trip_a = np.zeros(max(results['trip']) + 1)
trip_r = np.zeros(max(results['trip']) + 1)
num = np.zeros(max(results['trip']) + 1)
while i < results.size / 9:
    if results.loc[i, 'trip'] != j:
        j = results.loc[i, 'trip']
    if results.loc[i, 'trip'] == j:
        trip_v[j] += results.loc[i, 'vehicle_speed']
        trip_a[j] += results.loc[i, 'ABS_Acceleration']
        trip_r[j] += results.loc[i, 'engine_rpm']
        num[j] += 1
    i += 1

print "trip1的平均速度"
print trip_v[92] / num[92]
i = 1

#计算方差
trip_v_var = np.zeros(max(results['trip']) + 1)
trip_a_var = np.zeros(max(results['trip']) + 1)
trip_r_var = np.zeros(max(results['trip']) + 1)
i = 1
j = 1
while i < num.size:
    trip_v_var[i] = round(np.var(results.loc[np.sum(num[0:i]):np.sum(num[0:i + 1]) - 1, 'vehicle_speed']),2)
    trip_a_var[i] = round(np.var(results.loc[np.sum(num[0:i]):np.sum(num[0:i + 1]) - 1, 'ABS_Acceleration']),2)
    trip_r_var[i] = round(np.var(results.loc[np.sum(num[0:i]):np.sum(num[0:i + 1]) - 1, 'engine_rpm']),2)
    i += 1

print trip_v_var[92]
print trip_a_var[92]
print trip_r_var[92]
n=num.size
Speed_Classify=pd.DataFrame(Speed_Classify)
ABS_Acceleration_Classify=pd.DataFrame(ABS_Acceleration_Classify)
RPM_Classify=pd.DataFrame(RPM_Classify)

newtrip = pd.DataFrame({'trip':np.arange(1,93,1),
                   'v_avg':(trip_v/num)[1:n],
                   'v_std':trip_v_var[1:n] ,
                   'v_a':Speed_Classify.iloc[1:n,a],
                   'v_b':Speed_Classify.iloc[1:n,b],
                   'v_c':Speed_Classify.iloc[1:n,c],
                   'v_d':Speed_Classify.iloc[1:n,d],
                   'a_avg':(trip_a/num)[1:n],
                   'a_std':trip_a_var[1:n] ,
                   'a_a':ABS_Acceleration_Classify.iloc[1:n,a],
                   'a_b':ABS_Acceleration_Classify.iloc[1:n,b],
                   'a_c':ABS_Acceleration_Classify.iloc[1:n,c],
                   'r_avg':(trip_r/num)[1:n],
                   'r_std':trip_r_var[1:n] ,
                   'r_a':RPM_Classify.iloc[1:n,a],
                   'r_b':RPM_Classify.iloc[1:n,b],
                   'r_c':RPM_Classify.iloc[1:n,c]
                   },columns=['trip','v_avg','v_std','v_a','v_b','v_c','v_d',
                              'a_avg','a_std','a_a','a_b','a_c',
                              'r_avg','r_std','r_a','r_b','r_c'])
# ,'v_avg':(trip_v/num)[1:num.size]
# print (trip_v/num)[1:num.size]
# ,'v_a':Speed_Classify
# ,columns={'trip','v_avg','v_std','v_a','v_b','v_c','v_d'}
newtrip=newtrip.round({'v_avg':2,'a_avg':2,'r_avg':2})
print newtrip.head()
newtrip.to_csv("newtrip.csv")


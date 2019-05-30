# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:39:49 2019

@author: DHF
"""

#CREATE TABLE Loan_Data
#(
#ID int NOT NULL AUTO_INCREMENT,
#LastName nvarchar(255),
#FirstName nvarchar(255),
#Address varchar(255),
#City varchar(255)
#)
import pandas as pd

#以下获取插入sql
df=pd.read_excel('Data_Feature.xlsx')
#sql_str='''CREATE TABLE Loan_Data
#(
#ID int NOT NULL IDENTITY(1, 1) PRIMARY KEY'''
#
#for i in range(1,75):
#    sql_str+=',\n'
#    data=df.ix[i][1:3].values
#    t1=data[0]
#    t2=data[1]
#    sql_str+=t1
#    sql_str+=' '+t2
#sql_str+='\n)'
#print("读取指定行的数据：\n{0}".format(sql_str))


#以下获取更新sql
sql_str=''

from collections import defaultdict

d = defaultdict(list)
for i in range(1,75):
    data=df.ix[i][0:2].values
    t1=data[0]
    t2=data[1]
    d[t1].append(t2)
tables=['ContractManage',  'LoanApply', 'CreditRecord','TDInfo', 'CRM_Customer ', 'CRM_CustomerPersonal', 'CRM_ContactInformation', 'CRM_CollateralQuery']
print(d.keys())
print(tables[0])
for i in range(0,2):
    table=tables[i]
#    print(d[table])
    for col in d[table]:
        sql_str+='''update dbo.Loan_Data
SET dbo.Loan_Data.%s=t1.%s
FROM xcxd2019.dbo.%s as t1
left join dbo.Loan_Data as t2
ON t1.LoanNum=t2.LoanNum

'''%(col,col,table)
print(sql_str)


print('-----------------------------------------')
print('-----------------------------------------')
print('-----------------------------------------')
sql_str=''
for i in range(2,3):
    table=tables[i]
#    print(d[table])
    for col in d[table]:
        sql_str+='''update dbo.Loan_Data
SET dbo.Loan_Data.%s=t1.%s
FROM xcxd2019.dbo.%s as t1
left join dbo.Loan_Data as t2
ON t1.ContractNum=t2.ContractNum

'''%(col,col,table)
print(sql_str)


print('-----------------------------------------')
print('-----------------------------------------')
print('-----------------------------------------')
sql_str=''
count=0
for i in range(3,8):
    table=tables[i]
#    print(d[table])
    for col in d[table]:
        count+=1
        sql_str+='''update dbo.Loan_Data
SET dbo.Loan_Data.%s=t1.%s
FROM xcxd2019.dbo.%s as t1
left join dbo.Loan_Data as t2
ON t1.CustomerNum=t2.CustomerNum

'''%(col,col,table)
print(sql_str)
print(count)
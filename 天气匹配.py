import pandas as pd
import datetime


# df=pd.read_excel('/Users/xyc/Desktop/百果园/hyz/门店影响数据集_合并.xlsx')
df=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/门店数据/汇总.csv',index_col=0)
dzb=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/sz.csv',index_col=0)
# print(df.saledate.head())
# print(dzb.saledate.head())
dzb['saledate']=dzb.apply(lambda x: datetime.datetime.strptime(x['日期'], '%Y/%m/%d').strftime('%Y/%m/%d'), axis=1)
# print(set(dzb.saledate))
# print(set(df.saledate))
dd=pd.merge(df,dzb,how='left',on=['saledate','area'])
# print(dd.head().columns)
dd.to_csv('/Users/xyc/Desktop/百果园/hyz/匹配后门店数据.csv')
# print(len(dzb))
# sum=0
# gp_dzb=dzb.groupby('area')
# for name,group in gp_dzb:
#     print(name)
#     print(len(group.saledate))
#     print(group.saledate)
#     sum=sum+len(group.saledate)
# print(sum)
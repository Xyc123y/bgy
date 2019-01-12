import pandas as pd
import datetime
from sqlalchemy.engine import create_engine
import matplotlib.pyplot as plt
import matplotlib
from pylab import *

# engine = create_engine('presto://118.89.18.229:18080/hive/ods')
# df = pd.read_sql(sql="select * from erp_mag_customer_sale_state_item where saledate>'2018/12/01' and itemcode<='200000'  and customercode<'880001' limit 10 "
#                      ,con=engine)
# print(df.columns)
# print(df)
#
# a=['enterprisecode', 'customertype', 'customercode', 'saledate',
#        'itemcode', 'customername', 'itemname', 'saleqty', 'saleweight',
#        'saleamt', 'guests', 'itemtypecode', 'itemtypename', 'areacode',
#        'areaname', 'saleunitcode', 'unitname', 'profit', 'insaleqty',
#        'insaleweight', 'insaleamt', 'inguests', 'inprofit', 'aidunitcode',
#        'aidqty', 'couponamt', 'itemcouponamt', 'memdiscountamt',
#        'positiveprofit', 'negativeprofit', 'synctime', 'part_date']
#
#
#
#
# import pandas as pd
# import datetime
# df=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/匹配test.csv')
# dzb=pd.read_excel('/Users/xyc/Desktop/百果园/hyz/对照表.xlsx')
# gp_df=df.groupby('customercode')
# gp_dzb=dzb.groupby('ERP部门编码')
# df=df.set_index('saledate',drop=True).sort_index()
#
# pv_df=pd.DataFrame()
#
# for name,group in gp_df:
#
#     try:
#
#         for i in gp_dzb.get_group(name).index:
#
#             start=datetime.datetime.strptime(gp_dzb.get_group(name).loc[i,'任职开始时间'],'%Y/%m/%d').strftime('%Y/%m/%d')
#
#             stop=datetime.datetime.strptime(gp_dzb.get_group(name).loc[i,'任职结束时间'], '%Y/%m/%d') + datetime.timedelta(days=1)
#             stop=stop.strftime('%Y/%m/%d')
#
#             st_group=group.set_index('saledate',drop=True).sort_index()
#
#             st_group['职工姓名']=st_group.truncate(before=start).truncate(after=stop).apply(lambda x:gp_dzb.get_group(name).loc[i,'职工姓名'],axis=1)
#
#         pv_df=pv_df.append(st_group)
#     except KeyError:
#         print('对照表找不到'+str(name))
#     except ValueError:
#         print('对照表里没有')
# # print(pv_df)
# pv_df.to_csv('/Users/xyc/Desktop/百果园/hyz/匹配test结果.csv')
# df=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/天气网天气(截至20180831).csv')
# dzb=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/天气量化标准/fengxiang.csv',encoding='gbk')
# print(df.head)
# df.head().to_csv('/Users/xyc/Desktop/百果园/hyz/天气网天气(截至20180831)样本.csv)
# da=df[df['city_cn']=='深圳']
# print(da.columns)
# da=da.set_index('日期',drop=True).sort_index()
# print(set(df['area_cn']))
# print(dzb[['天气','tianqi']])
# print(dzb.columns)
# print(set(da.天气).difference(set(dzb.天气)))
# da.to_csv('/Users/xyc/Desktop/百果园/hyz/深圳.csv')
# sz=pd.merge(dzb[['风向','fengxiang_code']],sz,how='right',on='风向')
# print(sz)
# sz.to_csv('/Users/xyc/Desktop/百果园/hyz/sz.csv')
#
#

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei Regular']
plt.rcParams['font.sans-serif'] = ['SimHei']  # for Chinese characters
mpl.rcParams['axes.unicode_minus'] = False




import getNum as gN
a='01/01'
b='11/25'
bc=gN.getNum(a,b)
bc.contract('2017','2018')
bc.mth_plt()






# print(bc.price_index_2017)
# price_index_2017=bc.price_index_2017.copy()
# price_index_2018=bc.price_index_2018.copy()
# print(p)
# df_mth=bc.local_var['price_index2017'].append(bc.local_var['price_index2018'])
# print(df_mth)
# print(bc.contract[['2018mth', 'Mth', '2017price_index', '2018price_index', '同比']])
# df_mth=pd.merge(df_mth,bc.contract[['2018mth',  '同比']],how='left',left_on='mth',right_on='2018mth')
# # dd['Mth']=dd.apply(lambda x:x['mth'][5:7],axis=1)
# print(dd.columns)
# # print(bc.price_index_2017)
# dd=bc.price_index_2017.copy()
# dd.rename(columns={dd.columns[1]:dd.columns[1][4:15],dd.columns[0]:dd.columns[0][4:7]},inplace=True)
# contract=pd.merge(bc.price_index_2017,bc.price_index_2018,how='outer',on='Mth')
# print(contract)
# contract['同比']=contract.apply(lambda x:x['2018price_index']/x['2017price_index']-1,axis=1)
# dd=pd.DataFrame(ba.price_index_2017).reset_index(drop=False)
# # print(pd.DataFrame(ba.price_index_2017).reset_index(drop=False))
#
#
# import pandas as pd
# import datetime
#
# df=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/raw_data_v3.csv',encoding='gbk')#读取数据表
# dzb=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/销量更新数据—20181226.csv')#读取对照表
# dzb_2=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/商品结构更新数据—20181226.csv')
# # dzb['saledate']=dzb.apply(lambda x: datetime.datetime.strptime(x['saledate'], '%Y/%m/%d').strftime('%Y/%m/%d'), axis=1)#将saledate列转化为时间格式，需要就调用
# dd=pd.merge(df,dzb,how='left',on=['saledate','customercode'])#左合并，匹配列：'saledate','customercode'
# dd=pd.merge(dd,dzb_2,how='left',on=['saledate','customercode'])#左合并，匹配列：'saledate','customercode'
# dd.to_csv('/Users/xyc/Desktop/百果园/hyz/匹配结果(3表合一).csv',encoding='gbk')
# dd.to_excel('/Users/xyc/Desktop/百果园/hyz/匹配结果(天气).xlsx')
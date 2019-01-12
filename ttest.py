import pandas as pd
import datetime
from sqlalchemy.engine import create_engine
engine = create_engine('presto://118.89.18.229:18080/hive/ods')
# data=["'2017/11/01'","'2017/11/02'","'2017/11/03'","'2017/11/04'"]
# for sub in data:
#     start=sub
#     print(start)
start='2018/08/01'
stop='2018/11/25'
# aa=pd
start1=datetime.datetime.now()
print(start1)
# aa = pd.read_sql(sql="select * "
#                  "from ods.erp_mag_customer_sale_state_item t "
#                  "limit 5000000"
#                  ,con=engine)




aa = pd.read_sql(sql="select substr(saledate,1,7) as mth,itemcode,sum(cast(saleweight as double)) as saleweight,sum(cast(saleamt as double)) as saleamt "
                 "from ods.erp_mag_customer_sale_state_item  "
                 "where itemcode <= '200000' and saledate between '%s' and '%s' and saleweight>'0' and enterprisecode='bgy' and customertype='S' and customercode<'880001' "
                 "group by itemcode,substr(saledate,1,7) "%(start,stop)
                 ,con=engine)
# aa.to_csv('/Users/xyc/Desktop/百果园/price_index_test/price_index_mth.csv')
# print(aa.columns)
print(aa)
print(datetime.datetime.now()-start1)
# df=pd.read_csv('/Users/xyc/Desktop/百果园/price_index_test/price_index_mth.csv',index_col='Unnamed: 0')
df=aa
# # print(df)
sum_df=df.groupby('mth')['saleweight'].sum()
sum_df=pd.DataFrame(sum_df)
sum_df.reset_index(drop=False,inplace=True)
sum_df.rename(columns={'saleweight':'sum_saleweight'},inplace=True)
merge_df=pd.merge(df,sum_df,how='left',on=['mth','mth'])
merge_df['price']=merge_df.apply(lambda x:x['saleamt']/x['saleweight'],axis=1)
merge_df['share']=merge_df.apply(lambda x:x['saleweight']/x['sum_saleweight'],axis=1)
merge_df['price_index']=merge_df.apply(lambda x:x['price']*x['share'],axis=1)
sum_price_index=merge_df.groupby('mth')['price_index'].sum()
print(sum_price_index)
# print(sum_df)
# print(merge_df)
# # print(sum_price_index)
# price_index_mth=pd.read_excel('/Users/xyc/Desktop/百果园/price_index_month.xlsx')
# price_index_mth['月份']=price_index_mth.apply(lambda x:x['年月'].strftime('%m'),axis=1)
# price_index_mth['年/月']=price_index_mth.apply(lambda x:x['年月'].strftime('%Y/%m'),axis=1)
# print(price_index_mth)



prepare_list = locals()
for i in range(16):
    prepare_list['list_' + str(i)] = ('我是第' + str(i)) + '个list'
    # print(prepare_list['list_%d'%i])
    # prepare_list['list_' + str(i)].append(('我是第' + str(i)) + '个list')
    print(prepare_list['list_%d'%i])
# print(prepare_list)
    print(list_3)
    # print(prepare_list['list_1'])
    # print(prepare_list['list_2'])
    # print(prepare_list['list_3'])

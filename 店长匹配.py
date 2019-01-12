import pandas as pd
import datetime
df=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/匹配后门店数据.csv',index_col=0)
dzb=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/对照表.csv')
# print(df.head())
# print(dzb.tail())
gp_df=df.groupby('customercode')
gp_dzb=dzb.groupby('ERP部门编码')
print(len(df))
df=df.set_index('saledate',drop=True).sort_index()
# print(df)
# print(df.truncate(before='2011/05/01').truncate(after='2011/11/20'))
pv_df=pd.DataFrame()

for name,group in gp_df:
    # print('分组'+str(name)+'如下：')
    # print(group)
    # print(name)
    # print(gp_dzb.get_group(name))
    try:
        # print(gp_dzb.get_group(name))
        # print(gp_dzb.get_group(name)[0])
        # print(len(gp_dzb.get_group(name)))
        for i in gp_dzb.get_group(name).index:
            # print(i)
            start=datetime.datetime.strptime(gp_dzb.get_group(name).loc[i,'任职开始时间'],'%Y/%m/%d').strftime('%Y/%m/%d')
            # stop=gp_dzb.get_group(name).loc[i,'任职开始时间']
            stop=datetime.datetime.strptime(gp_dzb.get_group(name).loc[i,'任职结束时间'], '%Y/%m/%d') + datetime.timedelta(days=1)
            stop=stop.strftime('%Y/%m/%d')
            # data.sort_index().truncate(before=self.start).truncate(after=self.stop)
            st_group=group.set_index('saledate',drop=True).sort_index()
            # print(gp_dzb.get_group(name).loc[i,'职工姓名'])
            # print(st_group)
            # print('%s'%start)
            # print(stop)
            # print(gp_dzb.get_group(name).loc[i])
            st_group['index']=st_group.truncate(before=start).truncate(after=stop).apply(lambda x:gp_dzb.get_group(name).loc[i,'index'],axis=1)

            # print(st_group)
        # print(st_group)
        pv_df=pv_df.append(st_group)
    except KeyError:
        print('对照表找不到'+str(name))
        pv_df = pv_df.append(st_group)
    except ValueError:
        print('对照表里没有')
print(pv_df)
# pv_df.to_csv('/Users/xyc/Desktop/百果园/hyz/匹配结果.csv',encoding='gbk')
da=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/匹配结果.csv',encoding='gbk',index_col=0)
dd=pd.merge(dd,dzb,how='left',on=['index'])
da.reset_index(drop=False,inplace=True)
print(dd.columns)
dd.to_csv('/Users/xyc/Desktop/百果园/hyz/匹配结果(全).csv',encoding='gbk')
df.rename(columns={'saledate':'日期'},inplace=True)
dzb=pd.read_csv('/Users/xyc/Desktop/百果园/hyz/数量/汇总.csv')
dd=pd.merge(da,dzb,how='left',on=['saledate', 'customercode'])
dd=dd[['saledate','customercode','currenct_year', 'currenct_mth', 'currenct_day',
        'open_year', 'open_mth', 'open_day', 'gap',
       'store_level', 'store_type', 'store_square', 'store_warehouse', 'area',
       'online_amt_share', 'online_qty_share', 'fin_amt', 'fin_qty',
       'big_con_saleamt', 'big_con_saleamt_share', 'discount', 'top_10',
       'a_amt', 'zp_amt', 'coupon_value', 'activity_num', 'mem_saleamt',
       'saleamt', 'fengxiang_code', 'fengli_code','tianqi_code', 'area_py',
        '最低气温', '最高气温',
        '学历.1', '年龄', '性别', '用工类型',
       '岗位状态', '是否主任职', '职位', '变动类型', '变动原因', '入职时长', '任职店长时长', '任职店长年',
       '任职店长月', '任职店长日', '入职年', '入职月', '入职日','sumqty',
       'weight']]


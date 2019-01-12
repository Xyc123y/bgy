import pandas as pd
import datetime
from sqlalchemy.engine import create_engine
# import matplotlib.pyplot as plt
# import matplotlib
# from pylab import *


class getNum:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.engine = create_engine('presto://118.89.18.229:18080/hive/ods')
        self.local_var = locals()
        self.price_index_2017 = self.price_index('2017')
        self.price_index_2018 = self.price_index('2018')

    def data_get(self, year):
        start = year + '/' + self.start
        stop = year + '/' + self.stop
        raw_data = pd.read_sql(
            sql="select substr(saledate,1,7) as mth,itemcode,sum(cast(saleweight as double)) as saleweight,sum(cast(saleamt as double)) as saleamt "
                "from ods.erp_mag_customer_sale_state_item "
                "where itemcode <= '200000' and saledate between '%s' and '%s' and saleweight>'0' and enterprisecode='bgy' and customertype='S' and customercode<'880001' "
                "group by itemcode,substr(saledate,1,7) " % (start, stop)
            , con=self.engine)
        # print(start)
        return raw_data

    def price_index(self, year):
        df = self.data_get(year)
        sum_df = df.groupby('mth')['saleweight'].sum()
        sum_df = pd.DataFrame(sum_df)
        sum_df.reset_index(drop=False, inplace=True)
        sum_df.rename(columns={'saleweight': 'sum_saleweight'}, inplace=True)
        merge_df = pd.merge(df, sum_df, how='left', on='mth')
        merge_df['price'] = merge_df.apply(lambda x: x['saleamt'] / x['saleweight'], axis=1)
        merge_df['share'] = merge_df.apply(lambda x: x['saleweight'] / x['sum_saleweight'], axis=1)
        merge_df['price_index'] = merge_df.apply(lambda x: x['price'] * x['share'], axis=1)
        sum_price_index = pd.DataFrame(merge_df.groupby('mth')['price_index'].sum()).reset_index(drop=False)
        sum_price_index['Mth'] = sum_price_index.apply(lambda x: x['mth'][5:7], axis=1)
        sum_price_index_year = sum_price_index.copy()
        self.local_var['price_index' + year] = sum_price_index
        sum_price_index_year.rename(columns={'price_index': '%sprice_index' % year, 'mth': '%smth' % year},
                                    inplace=True)
        return sum_price_index_year

    def contract(self, last_year, this_year):
        contract = pd.merge(self.price_index_2017, self.price_index_2018, how='outer', on='Mth')
        contract['同比'] = contract.apply(lambda x: x['%sprice_index' % this_year] / x['%sprice_index' % last_year] - 1,
                                        axis=1)
        self.contract = contract
        return contract

    def mth_plt(self):
        import matplotlib.pyplot as plt
        import matplotlib
        from pylab import mpl
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei Regular']
        plt.rcParams['font.sans-serif'] = ['SimHei']  # for Chinese characters
        mpl.rcParams['axes.unicode_minus'] = False
        df_mth = self.local_var['price_index2017'].append(self.local_var['price_index2018'])
        df_mth = pd.merge(df_mth, self.contract[['2018mth', '同比']], how='left', left_on='mth', right_on='2018mth')
        df_mth = df_mth[['mth', 'price_index', '同比']].rename(columns={'mth': '年月', 'price_index': '价格指数'}, inplace=0)
        # df_mth = pd.read_excel('/Users/xyc/Desktop/百果园/price_index_month.xlsx')
        df_mth.fillna(0, inplace=True)
        df_mth1 = df_mth[['年月', '同比']].fillna(0)
        df_mth1.set_index(['年月'], inplace=True)
        # print(df_mth)
        fig, ax1 = plt.subplots(figsize=(15, 4))
        ax2 = ax1.twinx()
        ax1.stackplot(df_mth1.index, df_mth1['同比'], color='lightpink', zorder=2)
        ax1.plot([], [], color='lightpink', label='同比', linewidth=5)
        ax2.plot(df_mth.年月, df_mth.价格指数, "-", label="价格指数", color='springgreen', zorder=3)
        # for a, b in zip(df_mth.年月, df_mth.价格指数):
        #     ax2.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
        plt.xticks(rotation=-90)
        ax1.set_ylabel('同比')
        ax2.set_ylabel('价格指数')
        fig.legend()
        plt.title('百果园价格指数(全国)', fontsize=20)
        plt.show()

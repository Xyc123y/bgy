import pandas as pd


def psjm(a, mth, malilj, pslj):
    x = a['月销售成本%d月' % mth]

    if a.城市类型 == '甲类':
        # 甲类的配送减免函数
        # 销售毛利额低于malilj元/月
        # 门店配送额低于pslj元/月，给予配货额95折优惠。
        # x为配送额,y为减免额
        if x > pslj:
            y = 0
        else:
            y = x * 0.1 * 0.05

    else:
        # 乙类的配送减免函数
        # 销售毛利额低于malilj元/月
        # 门店配送额低于pslj元/月，给予配货额95折优惠。
        # x为配送额,y为减免额
        if x > pslj:
            y = 0
        else:
            y = x * 0.1 * 0.05
    return y


def txf(a, mth, lj):
    x = a['毛利额%d月份' % mth]
    if a.城市类型 == '甲类':
        # 甲类的特许权使用费函数
        # 毛利额6.2万及以内：收取3%
        # 毛利额为起征点-12万（含12万）：收取15%
        # 毛利额为12万以上：收取25%
        # 此处理解为全部毛利额收取3%,高于起征点部分再额外收取12%,高于120000部分再额外收取10%
        y = 0.03 * x + max([0.12 * (x - 62000), 0]) + max([0.1 * (x - 120000), 0])
        if a['毛利额%d月份' % mth] >= lj:
            y1 = y
            y2 = 0
        else:
            y1 = 0
            y2 = y
    else:
        # 乙类的特许权使用费函数
        # 毛利额5.6万及以内：收取3%
        # 毛利额为起征点-12万（含12万）：收取15%
        # 毛利额为12万以上：收取25%
        # 此处理解为全部毛利额收取3%,高于起征点部分再额外收取12%,高于120000部分再额外收取10%
        y = 0.03 * x + max([0.12 * (x - 56000), 0]) + max([0.1 * (x - 120000), 0])
        if a['毛利额%d月份' % mth] >= lj - 3500:
            y1 = y
            y2 = 0
        else:
            y1 = 0
            y2 = y
    return y1, y2  # y1是特权使用费,y2是特权使用费减免


file_path = '/Users/xyc/Desktop/百果园/练手/01.xlsx'
df = pd.read_excel(file_path, index_col='序号')

df1 = df[['城市类型', '月销售成本8月', '月销售成本9月', '月销售成本10月', '毛利额8月份', '毛利额9月份', '毛利额10月份']]
df1 = df1.fillna(0)

for malilj in range(30000, 80000, 10000):
    zong = pd.DataFrame()
    ps_jm = pd.DataFrame()
    tq_jm = pd.DataFrame()
    for j in range(80000, 200001, 5000):
        sum_psjm = {}
        sum_tqjm = {}
        # malilj=38500
        pslj = j
        for i in range(3):
            mth = 8 + i
            df1['%d月减免的配送额' % mth] = df1.apply(lambda x: psjm(x, mth, malilj, pslj), axis=1)
            df1['%d月特权使用费' % mth] = df1.apply(lambda x: txf(x, mth, malilj)[0], axis=1)
            df1['%d月特权使用费减免费' % mth] = df1.apply(lambda x: txf(x, mth, malilj)[1], axis=1)
            sum_psjm['%d月配送减免' % mth] = sum(df1['%d月减免的配送额' % mth])
            sum_tqjm['%d月特权减免' % mth] = sum(df1['%d月特权使用费减免费' % mth])
        sum_tqjm['临界配送额'] = j
        sum_psjm['临界配送额'] = j
        ps_jm = ps_jm.append(pd.DataFrame.from_dict(sum_psjm, orient='index').T)
        tq_jm = tq_jm.append(pd.DataFrame.from_dict(sum_tqjm, orient='index').T)
    zong = pd.merge(ps_jm, tq_jm, on='临界配送额')
    zong = zong[['临界配送额', '8月配送减免', '8月特权减免', '9月配送减免', '9月特权减免', '10月配送减免', '10月特权减免']]
    zong['配送总减免'] = zong.apply(lambda x: x['8月配送减免'] + x['9月配送减免'] + x['10月配送减免'], axis=1)
    zong['特权总减免'] = zong.apply(lambda x: x['8月特权减免'] + x['9月特权减免'] + x['10月特权减免'], axis=1)
    zong.to_csv('/Users/xyc/Desktop/百果园/练手/0102减免(毛利临界=%d).csv' % malilj)

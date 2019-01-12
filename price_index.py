import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import mpl

# from matplotlib.font_manager import _rebuild
#
# _rebuild() #reload一下
# myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/xyc/Downloads/微软雅黑.ttf') # 这一行
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei Regular']
plt.rcParams['font.sans-serif'] = ['SimHei']  # for Chinese characters
mpl.rcParams['axes.unicode_minus'] = False

# #月价格指数——百果园价格指数(全国)
df_mth = pd.read_excel('/Users/xyc/Desktop/百果园/price_index_month.xlsx')
df_mth.fillna(0, inplace=True)
df_mth1 = df_mth[['年月', '同比']].fillna(0)
df_mth1.set_index(['年月'], inplace=True)
print(df_mth)
fig, ax1 = plt.subplots(figsize=(15, 4))
ax2 = ax1.twinx()
ax1.stackplot(df_mth1.index, df_mth1['同比'], color='lightpink', zorder=2)
ax1.plot([], [], color='lightpink', label='同比', linewidth=5)
ax2.plot(df_mth.年月, df_mth.价格指数, "-", label="价格指数", color='springgreen', zorder=3)
for a, b in zip(df_mth.年月, df_mth.价格指数):
    ax2.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

ax1.set_ylabel('同比')
ax2.set_ylabel('价格指数')
fig.legend()
plt.title('百果园价格指数(全国)', fontsize=20)
# plt.xticks(rotation=-90)
plt.show()
# plt.savefig('/Users/xyc/Desktop/百果园/百果园价格指数(全国).png')
# plt.close()


# 日价格指数——百果园价格指数(全国)
df_day = pd.read_excel('/Users/xyc/Desktop/百果园/price_index_day.xlsx', index_col='日期')
# print(df_day)
# df_day.index.strftime('%m/%d')
fig, ax1 = plt.subplots(figsize=(15, 8))
# plt.xticks(rotation=-90)
ax2 = ax1.twinx()
ax1.stackplot(df_day.index.strftime('%m/%d'), df_day['同比'], color='lightpink', zorder=2)
ax1.plot([], [], color='lightpink', label='同比', linewidth=5)
ax2.plot(df_day.index.strftime('%m/%d'), df_day['%s' % df_day.columns[0]], "-", label="%s" % df_day.columns[0],
         color='springgreen', zorder=3)
ax2.plot(df_day.index.strftime('%m/%d'), df_day['%s' % df_day.columns[1]], "-", label="%s" % df_day.columns[1],
         color='skyblue', zorder=3)
# for a, b in zip(df_mth.年月,df_mth.价格指数):
#     ax2.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

ax1.set_ylabel('同比')
ax2.set_ylabel('价格指数')
fig.legend()
plt.title('%s-%s商品价格指数（日）' % (
df_day.index.strftime('%m/%d')[0], df_day.index.strftime('%m/%d')[len(df_day.index.strftime('%m/%d')) - 1]),
          fontsize=20)
ax1.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(10))
plt.show()
# plt.savefig('/Users/xyc/Desktop/百果园/%s-%s商品价格指数（日）.png'%(df_day.index.strftime('%m-%d')[0],df_day.index.strftime('%m-%d')[len(df_day.index.strftime('%m/%d'))-1]))
# plt.close()

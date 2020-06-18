import akshare as ak
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_rows', None)

# real time stock quotes
# stock_zh_a_spot_df = ak.stock_zh_a_spot()
# print(stock_zh_a_spot_df)

# history data    stock_zh_a_daily
# stock_zh_a_daily_hfq_df = ak.stock_zh_a_daily(symbol="sz000063", adjust="qfq")

# stock_zh_index_spot  实时指数行情数据

# 获取东方财富网-数据中心-研究报告-东方财富分析师指数-东方财富分析师指数2020最新排行
# stock_em_analyst_rank_df = ak.stock_em_analyst_rank()
# print(stock_em_analyst_rank_df)

# indicator="今日"; {"今日", "3日", "5日", "10日"}  资金流向
stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator="今日")
cashintoday = stock_individual_fund_flow_rank_df.head(70)[['代码', '名称', '最新价', '涨跌幅', '主力净流入-净额', '主力净流入-净占比']]
cashin3 = ak.stock_individual_fund_flow_rank(indicator="3日").head(70)[
    ['代码', '名称', '最新价', '涨跌幅', '主力净流入-净额', '主力净流入-净占比']]
cashin5 = ak.stock_individual_fund_flow_rank(indicator="5日").head(70)[
    ['代码', '名称', '最新价', '涨跌幅', '主力净流入-净额', '主力净流入-净占比']]

print(pd.merge(pd.merge(cashintoday, cashin3), cashin5))
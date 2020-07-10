import tushare as ts
import pandas as pd
import yagmail

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_rows', None)
inventory = ['300059', '002624']


def get_pricereport(stock):
    df = ts.get_realtime_quotes(stock)
    df['cost'] = ['17.251', '59.451']
    df['vol'] = ['1000', '1000']
    df['prof'] = df[['price', 'cost', 'vol']].apply(
        lambda x: round(float(x['vol']) * (float(x['price']) - float(x['cost'])), 2),
        axis=1)
    print(df[['name', 'code', 'price', 'cost', 'vol', 'prof']])
    print(df['prof'].sum())
    return df['prof'].sum()

get_pricereport(inventory)

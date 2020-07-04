import requests
import akshare as ak
import json
from datetime import datetime

now = datetime.now().strftime("%m%d-%H:%M")

# testurl = 'http://qt.gtimg.cn/q=r_hk09988'
wx_bot_hk = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*******************'
def send_msg_hkbot(content):
    data = json.dumps({"msgtype": "markdown",
                       "markdown": {"content": content,
                       "mentioned_list":['@all']}})
    r = requests.post(wx_bot_hk, data, auth=('Content-Type', 'application/json'))
    return r
    
def get_hongkong_stock(symbol):
    url = 'http://qt.gtimg.cn/q=r_hk' + str(symbol)
    res = requests.get(url)
    result = res.content.decode('gbk').split('~')
    current_details = '名称：'+ result[1] +'\n' + '当前价格：' + result[3] +'\n' + '涨跌：' + result[31] + '\n'+ '涨跌幅：' + result[32]+'%'
    return current_details

def get_hongkong_ma5(symbol1):
    stock_hk_daily_hfq_df = ak.stock_hk_daily(symbol=symbol1, adjust="")
    return stock_hk_daily_hfq_df.sort_index(ascending = False).head(5)[['close']].mean()

def get_hongkong_ma10(symbol1):
    stock_hk_daily_hfq_df = ak.stock_hk_daily(symbol=symbol1, adjust="")
    return stock_hk_daily_hfq_df.sort_index(ascending = False).head(10)[['close']].mean()

def send_message_details_hk(symbol):
    send_msg_hkbot("""现在的时间是%s\n<font color="info"></font>\n%s \nMA5: %.2f \nMA10: %.2f""" % (now,get_hongkong_stock(symbol),get_hongkong_ma5(symbol),get_hongkong_ma10(symbol)))

send_message_details_hk('01896')

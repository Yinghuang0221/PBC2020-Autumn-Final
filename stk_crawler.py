import time
from io import StringIO
import requests
import pandas as pd

#取得今天日期
def create_today_timestamp():
    today = time.strftime("%Y-%m-%d", time.gmtime())
    return int(time.mktime(time.strptime(today, "%Y-%m-%d")))
#計算需要資料的天數
def create_timestamp_from_today(n):
    today = create_today_timestamp()
    return today + n*24*3600
#取得天數
tomorrow_timestamp = create_timestamp_from_today(1)

#由證券交易所網站獲得所需資料
def create_tw_stock_info_list():
    res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
    #資料存成Dataframe格式
    df = pd.read_html(res.text)[0]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    #刪除不必要之欄位資訊
    df = df.dropna(thresh=6, axis=0)
    df = df.dropna(how='any', axis=1)
    df = df.dropna(how='any', axis=0)
    #刪除後重新排序
    df = df.reset_index(drop=True)
    #此幾行資料為標題名稱，故刪除
    df = df.drop([0, 947, 948, 949, 967, 968, 969, 970], axis=0)
    df = df.reset_index(drop=True)
    
    #設定要輸出之資料之欄位名稱
    new_df = df['有價證券代號及名稱'].str.replace(u'\u3000', ' ').str.split(u' ', expand=True)
    new_df.columns = ['Ticker', 'StockName']
    new_df['Sector'] = df['產業別']

    return new_df

#要輸出之資料
tw_stock_info_df = create_tw_stock_info_list()

#設定輸出成CSV後之格式
stock_df = pd.DataFrame()
Stock_Name_list = tw_stock_info_df['StockName']
Sector_list = tw_stock_info_df['Sector']
ticker_list = tw_stock_info_df['Ticker']
count = 0


for ticker in ticker_list:
    if count != 861: #此筆資料有問題
        #可以成功下載資料之情況
        print('## Info:Download Ticker' + ticker + '!')
        site = "https://query1.finance.yahoo.com/v7/finance/download/"+ticker+".TW?period1=0&period2="+str(tomorrow_timestamp)+"&interval=1d&events=history&crumb=hP2rOschxO0"
        #可以成功輸出
        try:
            response = requests.get(site)
            tmp_df = pd.read_csv(StringIO(response.text))
            tmp_df['Ticker'] = ticker
        #當比資料無法輸出
        except:
            print('## Warning: Ticker '+ticker+' is failed!')
        #將檔案存為CSV檔
        tmp_df.to_csv(Stock_Name_list.iloc[count] + " " + Sector_list.iloc[count] + ".csv")
    count += 1

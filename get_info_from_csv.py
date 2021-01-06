import os, csv, math, statistics
import time


# 算各個標準差的平均
def avg(std_list):
    summary = 0
    for num in std_list:
        summary += num
    if len(std_list) == 0:
        return "ERROR"
    else:
        return summary / len(std_list)


# 取得資料夾內所有CSV檔名(預設此檔案與CSV同路徑)
def get_excels():
    filelist = []
    now_dir = os.getcwd()
    for root, dirs, files in os.walk(now_dir):
        for name in files:
            if name.split('.')[-1] == "csv":
                filelist.append(name)
    return filelist


# 處理每個CSV的資料
def get_info(filename):
    lns = []
    ln_err = []
    stde = []
    count = 0
    # 讀檔
    with open(filename, 'r', encoding="utf-8") as csvfile:
        file = csv.reader(csvfile)
        # 取收盤價對數
        for line in file:
            try:
                lns.append(math.log(float(line[5])))
                stock_price = float(line[5])
                count += 1
            except:
                pass

    # 與前一天的差
    for i in range(1, len(lns)):
        error = lns[i] - lns[i - 1]
        ln_err.append(error)

    # 算五天的標準差並乘根號252
    for i in range(4, len(ln_err)):
        std = statistics.stdev([ln_err[i], ln_err[i - 1], ln_err[i - 2], ln_err[i - 3], ln_err[i - 4]])
        stde.append(std*math.sqrt(252))

    # 取五日標準差的平均，並四捨五入
    if avg(stde) != "ERROR":
        variation = avg(stde) * 1000
        if variation % 10 >= 5:
            variation += 10
        variation = int(variation / 10)
        variation /= 100
    # 有些算不出來就ERROR
    else:
        variation = 2
    # 印出方便確認
    # print(filename.split(".")[0])
    # print(variation , int(stock_price*100) / 100)
    # 暫時存在list裡? 在依照波動分類?
    # if variation != "ERROR":  # 試寫分類 應該沒啥問題
        # if (float(variation) >= 0.05) and ((int(stock_price*100) / 100) <= 100):
            # print(filename.split(".")[0])
            # print(variation , int(stock_price*100) / 100)
    stock_list.append([filename.split(".")[0], variation, int(stock_price*100) / 100])
    stock_variation_list.append(variation)


stock_list = []
stock_variation_list = []
filenames = get_excels()

# 開始跑每個資料
for name in filenames:
    get_info(name)
print(len(stock_list))

high_risk_list = []
mid_risk_list = []
low_risk_list = []
#輸出低風險名單
for i in range(math.ceil(len(stock_list)/4)):
    if stock_variation_list[i] != "ERROR":
        min_idx = stock_variation_list.index(min(stock_variation_list))
        low_risk_list.append(stock_list[min_idx])
        stock_variation_list[min_idx] = 3
#輸出中風險名單
for i in range(math.ceil(len(stock_list)/2)):
    min_idx = stock_variation_list.index(min(stock_variation_list))
    mid_risk_list.append(stock_list[min_idx])
    stock_variation_list[min_idx] = 3
#輸出高風險名單
for i in range(math.ceil(len(stock_list)/4)):
    min_idx = stock_variation_list.index(min(stock_variation_list))
    high_risk_list.append(stock_list[min_idx])
    stock_variation_list[min_idx] = 3

#將三種風險名單存為CSV
h_name = []
h_var = []
h_pri = []    
for i in range(len(high_risk_list)):
    h_name.append(high_risk_list[i][0])
    h_var.append(high_risk_list[i][1])
    h_pri.append(high_risk_list[i][2])
data = {'name':h_name , 'var':h_var , 'price':h_pri}

high_df = pd.DataFrame(data)
high_df.to_csv("high_risk_list" + ".csv" , encoding="utf_8_sig")

m_name = []
m_var = []
m_pri = []    
for i in range(len(mid_risk_list)):
    m_name.append(mid_risk_list[i][0])
    m_var.append(mid_risk_list[i][1])
    m_pri.append(mid_risk_list[i][2])
data = {'name':m_name , 'var':m_var , 'price':m_pri}

mid_df = pd.DataFrame(data)
mid_df.to_csv("mid_risk_list" + ".csv" , encoding="utf_8_sig")

l_name = []
l_var = []
l_pri = []    
for i in range(len(low_risk_list)):
    l_name.append(low_risk_list[i][0])
    l_var.append(low_risk_list[i][1])
    l_pri.append(low_risk_list[i][2])
data = {'name':l_name , 'var':l_var , 'price':l_pri}

low_df = pd.DataFrame(data)
low_df.to_csv("low_risk_list" + ".csv" , encoding="utf_8_sig")

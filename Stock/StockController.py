from urllib import parse
from ast import literal_eval
import requests
import time
from . import StockInfo

def getStockInfoAPI(itemcode):
    time.sleep(0.3) #단시간에 주가정보 자주 호출 시 block 가능성
    get_param = {
        'itemcode': itemcode
    }
    get_param = parse.urlencode(get_param)
    url = "https://api.finance.naver.com/service/itemSummary.nhn?%s" % (get_param)
    response = requests.get(url)
    stock = StockInfo.StockInfo(literal_eval(response.text.strip()))
    print(stock)

    return stock

def getStockRiseFallCd(stock):
    #주가가 상승했는지 하락했는지 동결인지 return하는 함수

    if stock.now>stock.prev:
        return "I" #increase
    elif stock.now<stock.prev:
        return "D" #decrease
    else:
        return "E" #equal

def getFormattedKoreanNumStr(num):
    #조, 억 구분
    #만은 버림
    korNumStr = str(num)
    numStr=str(int(num/100000000))
    print("korNumStr :"+korNumStr)
    # 449246
    if len(numStr)<=4:
        return format(int(numStr),',')+"억"
    elif len(numStr)>4 and len(numStr)<=8:
        print("진입")
        korNumStr= format(int(numStr[0:len(numStr)-4]), ',') + "조"
        aftNum = int(numStr[len(numStr)-4:]) #뒤에 오는 숫자(억단위)
        if aftNum>0:
            korNumStr += " "+format(aftNum, ',') + "억"
    print("korNumStr :" + korNumStr)

    return korNumStr




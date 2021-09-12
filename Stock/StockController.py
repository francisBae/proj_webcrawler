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
    stock = StockInfo(literal_eval(response.text.strip()))
    print(stock)

    return literal_eval(response.text.strip())
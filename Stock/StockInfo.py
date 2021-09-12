import datetime

class Stock:
    def __init__(self,itemcode, marketSum
                 # , per, eps, pbr
                 , now, diff, rate, quant, amount, high, low
                 # , risefall
                 ):
        self.itemcode = itemcode #종목코드
        self.marketSum = marketSum #시가총액
        # self.per = per
        # self.eps = eps
        # self.pbr = pbr
        self.now = now #현재주가
        self.diff = diff #전일 대비 가격차이
        self.rate = rate #상승율
        self.quant = quant #거래량
        self.amount = amount #거래대금
        self.high = high #고가
        self.low = low #저가
        # self.risefall = risefall
        self.prev = int(now)-int(diff) #전일종가
        self.curtime = datetime.datetime.now() #현재시간 기록

    def __init__(self,stock):
        self.itemcode = stock['itemcode'] #종목코드
        self.marketSum = stock['marketSum'] #시가총액
        # self.per = per
        # self.eps = eps
        # self.pbr = pbr
        self.now = stock['now'] #현재주가
        self.diff = stock['diff'] #전일 대비 가격차이
        self.rate = stock['rate'] #상승율
        self.quant = stock['quant'] #거래량
        self.amount = stock['amount'] #거래대금
        self.high = stock['high'] #고가
        self.low = stock['low'] #저가
        # self.risefall = risefall
        self.prev = int(self.now)-int(self.diff) #전일종가
        self.curtime = datetime.datetime.now() #현재시간 기록

    # def __init__(self,itemcode, stock):
    #     stock['itemcode'] = itemcode
    #     self(stock)

    def printInfo(self):
        print(self.itemcode+" | 현재주가 : "+str(+self.now)
              + " | 전일종가 : " + str(self.prev)
              + " | 전일대비 : "+str(self.diff)
              + " | 상승율 : " + str(self.rate)
              + " | 거래량 : " + str(self.quant)
              + " | 거래대금 : " + str(self.amount)
              + " | 고가 : " + str(self.high)
              + " | 저가 : " + str(self.low)
              + " | 기준시간 : "+ str(self.curtime))


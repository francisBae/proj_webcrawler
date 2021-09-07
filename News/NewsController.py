from . import NewsInfo
from MariaDb import QueryStatements as qs, DbConnector
from Utils import DateConverter as dc
from News import NewsInfo
import html
import re

def removeHtmlTag(htmlStr):
    newStr = htmlStr
    newStr = newStr.replace("<b>","")
    newStr = newStr.replace("</b>", "")
    newStr = re.sub("[\/:*?\"<>|]", "", newStr)
    newStr = html.unescape(newStr)

    return newStr

#news_link, news_title, news_date, news_by_company_name, news_description
def getNewsInfoListFromDict(newsDict):
    #사전구조를 뉴스객체 리스트로 전환

    news_list = list()

    for key in newsDict:
        news_by_company_name = key #회사명

        for title_key in newsDict[key]:
            news_link = newsDict[key][title_key]["link"]
            news_title = removeHtmlTag(title_key)
            # news_title = html.escape("""& < " ' >""") #특수문자 치환(따옴표 등)

            # news_title = re.sub("[\/:*?\"<>|]", "", news_title) #특수문자 제거(괄호 등)
            # news_title = html.unescape(news_title)

            news_date = str(dc.convertStringToDate(newsDict[key][title_key]["pubDate"]))

            news_description = removeHtmlTag(newsDict[key][title_key]["description"])
            # news_description = html.escape("""& < " ' >""")  # 특수문자 치환(따옴표 등)
            # news_description = re.sub("[\/:*?\"<>|]", "", news_description)  # 특수문자 제거(괄호 등)
            # news_description = html.unescape(news_description)

            news = NewsInfo.NewsInfo(news_link, news_title, news_date, news_by_company_name, news_description)
            # news.printInfo()

            news_list.append(news)
        # print(contents)
    return news_list

# def getNewsInfoLastSeq():
#     #마지막 뉴스 시퀀스번호 호출
#     query = qs.getNewsInfoLastSeq()
#     print(query)
#     seqNo = DbConnector.selectQuery(query)
#     print(seqNo)
#
#     return seqNo

def insertNewsInfo(newsInfoList):
    #마지막 뉴스 시퀀스번호 호출
    # seqNo = getNewsInfoLastSeq()

    # query = qs.getNewsInfoLastSeq()
    query = qs.insertNewsInfo()

    for newsInfo in newsInfoList:
        print(newsInfo.printInfo())
        # seqNo = seqNo+1

        try:
            val = (newsInfo.news_link, newsInfo.news_title, newsInfo.news_date, newsInfo.news_by_company_name, newsInfo.news_description)
            DbConnector.executeQuery(query, val)

        except:
            # seqNo = seqNo-1
            print("이미 저장된 뉴스입니다.")
            print(newsInfo.printInfo())
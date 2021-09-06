import os
import sys
import urllib.request
from urllib.parse import *
import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
#사용자지정 py임포트
import MariaDb
import SubscriberInfo
import MailSender
import NaverNewsCrawler as nnc
import QueryStatements as qs

email_targets = list()

query = qs.getSubscriberInfo()
subscr_infos = MariaDb.selectQuery(query)

for scr in subscr_infos:

    subscriber = SubscriberInfo.SubscriberInfo(str(scr['subscriber_seqno']),scr['subscriber_name'],scr['subscriber_phone'],scr['subscriber_email'])
    subscriber.printInfo()

    # query2 = "select A.subscriber_seqno, A.subscriber_email from TB_SUBSCRIBER_INFO A, TB_RECEIVE_CONSENT B"\
    #          +" where A.subscriber_seqno  = B.subscriber_seqno" \
    #          + " and A.subscriber_seqno = "+str(subscriber.subscriber_seqno) \
    #          +" and rcv_email_yn = 'Y'"

    query2 = qs.getSubscriberRcvConsentInfo(str(subscriber.subscriber_seqno))

    rcv_info = MariaDb.selectQuery(query2)
    print(rcv_info)

    if rcv_info is not None:
        print(subscriber.subscriber_email)
        email_targets.append(subscriber.subscriber_email)
    else:
        print("전송 대상 제외")

print(email_targets)
dtime = datetime.today().strftime("%Y%m%d%H%M")
title = "[오늘의 기사] "+str(dtime[0:4]+"년 "+dtime[4:6]+"월 "+dtime[6:8]+"일 "+dtime[8:10]+"시 "+dtime[10:12]+"분")

# contents = "테스트용 이메일"

keyword_1 = ['삼성전자', '카카오', '네이버', 'SK', '현대', 'LG', '애플']
keyword_2 = ['증권', '주식', '친환경','전기차','수소차','IT']

newsDict = nnc.keyword_combined(keyword_1,keyword_2)

cnt = 1
contents = ""

for key in newsDict:
    contents+="<br><div><p><font size=\"4px\" face=\"맑은고딕\"><b>"+str(cnt)+". "+key+"</b></p></div>"
    print(key) #삼성전자
    cnt+=1
    # print(newsDict[key]) #제목+링크
    # contents += "<div><font size=\"3px\" face=\"돋움\">"
    subcnt = 1
    for title_key in newsDict[key]:

        contents+="<a href="+newsDict[key][title_key]+">"+str(subcnt)+") "+title_key +"</a><br>"

        # contents+=str(subcnt)+") "+title_key + " : " + newsDict[key][title_key]+"<br>"
        subcnt+=1

        print(title_key+" : "+newsDict[key][title_key]) #제목:링크
    contents+"</font><br><br><br></div>"
    print()


# newsDict - titleLink - key/val

print(contents)

#HTML 정제

contents = MailSender.refineHtml(contents)
print(contents)

#발송 모듈
MailSender.sendEmail(email_targets,title,contents)

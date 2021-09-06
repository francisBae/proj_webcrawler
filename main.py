#사용자지정 py임포트
from datetime import datetime
from Subscriber import SubscriberInfo, SubscriberController as ssc
from WebCrawler import NaverNewsCrawler as nnc
from MailSender import MailSender as ms
from Mail import MailController as mc
from Keyword import CompanyController as cc, InterestController as ic, KeywordController as kc

def main():
    subscr_list = ssc.getSubscriberList()
    email_targets = ssc.getEmailTargets(subscr_list)
    print(email_targets)
    title = mc.getCurTimeNewsMailTitle()

    #키워드 리스트
    companyList = cc.getCompanyList()
    keyword_1 = kc.getKeywordList(companyList,"company_name")

    interestList = ic.getInterestList()
    keyword_2 = kc.getKeywordList(interestList,"interest_name")

    # keyword_1 = ['삼성전자', '카카오', '네이버', 'SK', '현대', 'LG', '애플']
    # keyword_2 = ['증권', '주식', '친환경','전기차','수소차','IT']


    newsDict = nnc.keyword_combined(keyword_1,keyword_2)

    contents = mc.getRefinedNewsContentsForHtml(newsDict)
    print(contents)



    # cnt = 1
    # contents = ""
    #
    # for key in newsDict:
    #     contents+="<br><div><p><font size=\"4px\" face=\"맑은고딕\"><b>"+str(cnt)+". "+key+"</b></p></div>"
    #     print(key) #삼성전자
    #     cnt+=1
    #     # print(newsDict[key]) #제목+링크
    #     # contents += "<div><font size=\"3px\" face=\"돋움\">"
    #     subcnt = 1
    #     for title_key in newsDict[key]:
    #
    #         contents+="<a href="+newsDict[key][title_key]+">"+str(subcnt)+") "+title_key +"</a><br>"
    #
    #         # contents+=str(subcnt)+") "+title_key + " : " + newsDict[key][title_key]+"<br>"
    #         subcnt+=1
    #
    #         print(title_key+" : "+newsDict[key][title_key]) #제목:링크
    #     contents+"</font><br><br><br></div>"
    #     print()


    # newsDict - titleLink - key/val

    # print(contents)

    #HTML 정제

    # contents = ms.refineHtml(contents)
    # print(contents)

    #발송 모듈
    ms.sendEmail(email_targets, title, contents)



if __name__ == "__main__":
	main()



#사용자지정 py임포트
from datetime import datetime
from Subscriber import SubscriberController as ssc
from WebCrawler import NaverNewsCrawler as nnc
from MailSender import MailSender as ms
from Mail import MailController as mc
from Keyword import CompanyController as cc, InterestController as ic, KeywordController as kc
from News import NewsController as nc

def main():
    # 구독자 리스트 조회
    subscr_list = ssc.getSubscriberList()

    # 구독자 중 이메일 수신 동의자를 리스트에 추가
    email_targets = ssc.getEmailTargets(subscr_list)

    # 이메일 제목 설정 (오늘의 기사 & 시간)
    title = mc.getCurTimeNewsMailTitle()

    # 키워드 리스트 생성 (db 조회)
    companyList = cc.getCompanyList() #기업 리스트
    keyword_1 = kc.getKeywordList(companyList,"company_name")
    interestList = ic.getInterestList() #관심사 리스트
    keyword_2 = kc.getKeywordList(interestList,"interest_name")
    # keyword_1 = ['삼성전자', '카카오', '네이버', 'SK', '현대', 'LG', '애플']
    # keyword_2 = ['증권', '주식', '친환경','전기차','수소차','IT']

    #네이버 뉴스 API 호출
    newsDict = nnc.keyword_combined(keyword_1,keyword_2)

    #이메일용으로 내용 정제
    # contents = mc.getRefinedNewsContentsForHtml(newsDict)
    contents = mc.getRefinedNewsContentsForResponsiveHtml(newsDict)

    #발송 모듈 호출
    ms.sendEmail(email_targets, title, contents)

    #DB 저장 위해 리스트 변환
    newsList = nc.getNewsInfoListFromDict(newsDict)

    #DB에 뉴스 정보 저장
    nc.insertNewsInfo(newsList)

if __name__ == "__main__":
	main()



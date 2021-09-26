# Naver News Mail Automation System
### 네이버 뉴스 메일 자동화 시스템

This project is a side project crawling news headlines posted in Naver and sending email via SMTP.

## Members
- 배종후(Bae Jong Hoo) <jonghoo.bae@kakao.com>

## Contents
1. [System](#system)
2. [UI/UX Design](#ui/ux-design)
3. [DB Models](#db-models)
4. [To Do](#to-do)
5. [Appendix](#appendix)

## System

<p align="center">
	<img src="https://github.com/francisBae/python-naver-news-crawler/blob/master/static/readme/webcrawlerjpg.jpg?raw=true", width="650">
</p>

The project is primarily designed using MariaDB.
Thanks to the convenience and velocity on data handling, using this RDBMS helped me out a lot on reducing the development period. Plus MariaDB is still free.

There are **5 main events** in this system and the events are as follows.

    1. Get Subscriber List (구독자 리스트 조회) 
    - SubscriberController.getSubscriberList()
    
    2. Get Keyword List (키워드 리스트 조회)
    - CompanyController.getCompanyList() #List of Interested Companies
    - KeywordController.getKeywordList() #List of Interested keywords

    3. Call Naver News API (네이버 뉴스 API 호출)
    - NaverNewsCrawler.keyword_combined() 
    
    4. Sending Email (이메일 전송 이벤트)
    - MailController.getRefinedNewsContentsForResponsiveHtml() #Refining text for html usage
    - MailSender.sendEmail() #Function sending Email via smtp protocol
    
    5. Insert News Info to Database (DB에 뉴스 정보 저장)
    - NewsController.insertNewsInfo()

## UI/UX Design
<p align="center">
	<img src="https://github.com/francisBae/python-naver-news-crawler/blob/master/static/readme/reactive.gif?raw=true", width="550">
</p>

The system focused on **user's interest** about each company, showing the daily stock info and news headlines about major interested keywords.
Implemented a reactive front-end design via bootstrap for **platform compatibility**. 

Receivers can get daily news headlines of the company based on interested keywords, and also can get the daily stock information.
For the convenience of users interested in stock infos, added a button [주가 정보 바로가기 = view stock info] above the headline.

<p align="center">
	<img src="https://github.com/francisBae/python-naver-news-crawler/blob/master/static/readme/stockinfo.jpg?raw=true", width="250">
    <br>
    press the button [주가정보 바로가기] for detailed stock info
</p>

## DB Models
<p align="center">
	<img src="https://github.com/francisBae/python-naver-news-crawler/blob/master/static/readme/dbmodel.png?raw=true">
</p>

The database(db_webcrawler) consists of 6 models(tables) and the models are as follows.

    1. tb_subscriber_info : information of news-email subscribers (이메일 구독자 정보)
    2. tb_receive_consent : information on whether you agree to receive emails (이메일 수신동의 여부)
    3. tb_interest_info : information on major interested keywords (주요 관심 키워드 정보)
    4. tb_company_info :  information on major interested companies (주요 관심 기업 정보)
    5. tb_news_info : stores news headline information received from the server (뉴스 헤드라인 데이터 저장 용도) 
    6. tb_cmmn_cd : common code used for settings (공통코드-설정값들 저장)

## ToDo
Still got some action items going on.

- add company_ssc column on news info table(tb_news_info) for join performance.
- visualize stock data via pandas library
- send file via email

## Appendix

### Naver API
[[네이버 API][Python] 네이버 뉴스를 가져오기 위해 네이버 검색 API 사용해보기 (1)](https://brightnightsky77.tistory.com/66)

### Email Settings
[파이썬 : 이메일 자동으로 보내기(gmail 사용법)](https://creatorjo.tistory.com/89)
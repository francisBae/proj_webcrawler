
def getSubscriberInfo():
    return "select * from TB_SUBSCRIBER_INFO"

def getSubscriberRcvConsentInfo(subscriber_seqno):
    query = "select A.subscriber_seqno, A.subscriber_email from TB_SUBSCRIBER_INFO A, TB_RECEIVE_CONSENT B"\
            +" where A.subscriber_seqno  = B.subscriber_seqno" \
            + " and A.subscriber_seqno = "+subscriber_seqno+" and rcv_email_yn = 'Y'"
    return query

def getCompanyInfoForKeyword():
    return "select * from TB_COMPANY_INFO where company_keyword_use_yn = 'Y'"

def getInterestInfoForKeyword():
    return "select * from TB_INTEREST_INFO where interest_keyword_use_yn = 'Y'"

# def getNewsInfoLastSeq():
#     return "SELECT LASTVAL(SEQ_NEWS_INFO)"

def insertNewsInfo():
    return "insert into TB_NEWS_INFO(news_seqno,news_link,news_title,news_date,news_by_company_name,news_description"+\
           ",sys_creation_date,sys_update_date)"\
           +"values (NEXTVAL(SEQ_NEWS_INFO), %s, %s, %s, %s, %s, SYSDATE(), SYSDATE())"

def getCompanySscByName(company_name):
    return "select * from tb_company_info where COMPANY_NAME =\'"+company_name+"\'"

def getCmmnCdInfo(grp_cd, cmmn_cd):
    return "select * from TB_CMMN_CD where GRP_CD =\'"+grp_cd+"\' and CMMN_CD =\'"+cmmn_cd+"\'"

def getSubscriberInfo():
    return "select * from TB_SUBSCRIBER_INFO"

def getSubscriberRcvConsentInfo(subscriber_seqno):
    query = "select A.subscriber_seqno, A.subscriber_email from TB_SUBSCRIBER_INFO A, TB_RECEIVE_CONSENT B"\
            +" where A.subscriber_seqno  = B.subscriber_seqno" \
            + " and A.subscriber_seqno = "+subscriber_seqno+" and rcv_email_yn = 'Y'"
    return query

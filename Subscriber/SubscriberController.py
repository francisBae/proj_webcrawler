from . import SubscriberInfo
from MariaDb import QueryStatements as qs, DbConnector


def getSubscriberList():
    query = qs.getSubscriberInfo()
    subscr_infos = DbConnector.selectQuery(query)

    subscr_list = list()
    for scr in subscr_infos:

        subscriber = SubscriberInfo.SubscriberInfo(str(scr['subscriber_seqno']), scr['subscriber_name'], scr['subscriber_phone'], scr['subscriber_email'])
        subscriber.printInfo()
        subscr_list.append(subscriber)


    # return subscr_infos
    return subscr_list

def getEmailTargets(subscr_infos):
    email_targets = list()

    for scr in subscr_infos:

        # subscriber = SubscriberInfo.SubscriberInfo(str(scr['subscriber_seqno']), scr['subscriber_name'], scr['subscriber_phone'], scr['subscriber_email'])
        # subscriber.printInfo()
        subscriber = SubscriberInfo.SubscriberInfo.getSubScriber(scr)

        query = qs.getSubscriberRcvConsentInfo(str(subscriber.subscriber_seqno))

        rcv_info = DbConnector.selectQuery(query)
        print(rcv_info)

        if rcv_info is not None:
            print(subscriber.subscriber_email)
            email_targets.append(subscriber.subscriber_email)
        else:
            print("전송 대상 제외")
    return email_targets
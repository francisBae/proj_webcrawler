class SubscriberInfo:
    def __init__(self,subscriber_seqno, subscriber_name, subscriber_phone, subscriber_email):
        self.subscriber_seqno = subscriber_seqno
        self.subscriber_name = subscriber_name
        self.subscriber_phone = subscriber_phone
        self.subscriber_email = subscriber_email
    def printInfo(self):
        print(self.subscriber_seqno+" | 이름 : "+self.subscriber_name +" | 전화번호 : "
              +self.subscriber_phone+" | 이메일 : "+self.subscriber_email)
    def getSubScriber(self):
        return self
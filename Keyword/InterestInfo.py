
class InterestInfo:
    def __init__(self,interest_seqno, interest_name, interest_keyword_use_yn):
        self.interest_seqno = interest_seqno
        self.interest_name = interest_name
        self.interest_keyword_use_yn = interest_keyword_use_yn #키워드여부
    def printInfo(self):
        print(self.interest_seqno+" | 관심사명 : "+self.interest_name)

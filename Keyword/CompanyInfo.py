
class CompanyInfo:
    def __init__(self,company_seqno, company_ssc, company_name, company_website, company_keyword_use_yn, company_stock_use_yn):
        self.company_seqno = company_seqno
        self.company_ssc = company_ssc #증권표준코드 Securities standard code
        self.company_name = company_name
        self.company_website = company_website
        self.company_keyword_use_yn = company_keyword_use_yn #키워드여부
        self.company_stock_use_yn = company_stock_use_yn #주식조회여부
    def printInfo(self):
        print(self.company_seqno+" | 증권표준코드 : "+self.company_ssc +" | 회사명 : "
              +self.company_name+" | 대표웹사이트 : "+self.company_website)



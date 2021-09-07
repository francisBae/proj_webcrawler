class NewsInfo:
    def __init__(self, news_link, news_title, news_date, news_by_company_name, news_description):
        self.news_link = news_link
        self.news_title = news_title
        self.news_date = news_date
        self.news_by_company_name = news_by_company_name
        self.news_description= news_description
    def printInfo(self):
        print(self.news_by_company_name+" | "+self.news_title+" | 링크 : "+self.news_link +" | 날짜 : "
              +self.news_date+" | 기사상세 : "+self.news_description)
    def getnews(self):
        return self
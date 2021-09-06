class MailInfo:
    def __init__(self,title, contents):
        self.title = title
        self.contents = contents

    def printInfo(self):
        print("[제목] "+self.title +"\n"+"[내용]\n"+self.contents)
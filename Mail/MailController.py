from datetime import datetime
from Utils import DateConverter as dc

def getCurTimeNewsMailTitle():
    dtime = datetime.today().strftime("%Y%m%d%H%M")
    title = "[오늘의 기사] " + str(dtime[0:4] + "년 " + dtime[4:6] + "월 " + dtime[6:8] + "일 " + dtime[8:10] + "시 " + dtime[10:12] + "분")
    return title

def getRefinedNewsContentsForHtml(newsDict):
    cnt = 1
    contents = "<html><body>"
    for key in newsDict:
        contents+="<br><div><p><font size=\"4px\" face=\"맑은고딕\"><b>"+str(cnt)+". "+key+"</b></p></div>"
        print(key) #삼성전자
        cnt+=1
        # print(newsDict[key]) #제목+링크
        # contents += "<div><font size=\"3px\" face=\"돋움\">"
        subcnt = 1
        for title_key in newsDict[key]:
            # print(newsDict[key][title_key])

            contents+="<a href="+newsDict[key][title_key]["link"]+">"+str(subcnt)+") "+title_key +"</a> ("+\
                      str(dc.convertStringToDate(newsDict[key][title_key]["pubDate"]))+")<br>"

            # contents+=str(subcnt)+") "+title_key + " : " + newsDict[key][title_key]+"<br>"
            subcnt+=1

            print(title_key+" : "+newsDict[key][title_key]["link"]) #제목:링크
        contents+"</font><br><br><br></div></body></html>"
        # print(contents)
    return contents
from datetime import datetime
from Utils import DateConverter as dc
from Keyword import CompanyController as cc
from CmmnCd import CmmnCdController as ccc
from Stock import StockInfo , StockController as sc
from bs4 import BeautifulSoup as bs

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

def getNewsHeader():
    html="""<head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width,initial-scale=1">
                <meta name="x-apple-disable-message-reformatting">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500;700&display=swap" rel="stylesheet">
            
            
                <style>
                    table, td, div, h1, p {
                        font-family: 'Noto Sans KR', sans-serif;
                    }
                    a:link {
                      color: #87cefa !important;
                    }
                    a:visited {
                      color: #2f4f4f !important;
                    }  
                    @media screen and (max-width: 530px) {
                        .unsub {
                                display: block;
                                padding: 8px;
                                margin-top: 14px;
                                border-radius: 6px;
                                background-color: #555555;
                                text-decoration: none !important;
                                <!-- CSS에서 나중에 설정한 값이 적용되지 않게 하려면 속성값 뒤에 !important -->
                                font-weight: bold;
                          }
                        .col-lge {
                            max-width: 100% !important;
                        }
                    }
                    @media screen and (min-width: 531px) {
                        .col-sml {
                         max-width: 27% !important;
                        }
                        .col-lge {
                         max-width: 73% !important;
                         }
                    }
                </style>
            </head>
        """
    return html

def getCompanyImgTitle(stockLink, company_image, company_name, stockNumber):
    html="""    
                 <tr>
                   <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                     <a href=""" \
                     + stockLink \
                     + """" style="text-decoration:none;"><img src=\"""" \
                     + company_image \
                     + """" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a>
                   </td>
                 </tr>
                 <tr>
                   <td style="padding:20px 30px 20px 30px;font-size:24px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                     <h1 style="margin-top:0;margin-bottom:16px;text-align:center;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;">""" \
                     + company_name + " [ " + """<a href=\"""" + (
                       stockLink) + """" style="color: #5a616b;text-decoration:none;">""" + stockNumber + "</a> ]" \
                + """</h1>
                 </tr>"""
    return html

def getCompanyStockTitle(stockLink, company_image, company_name, stockNumber):
    stockInfo = sc.getStockInfoAPI(stockNumber)
    stockRiseFallCd = sc.getStockRiseFallCd(stockInfo) #I : inc / D : dec / E : eq
    stockRFColor = ''
    stockRFIcon = ''
    stockHighColor = ''
    stockLowColor = ''

    #전일대비 상승/하락여부
    if stockRiseFallCd == 'I':
        stockRFColor = '#ed344a;' #red
        stockRFIcon = '▲'
    elif stockRiseFallCd == 'D':
        stockRFColor = '#40afde;' #blue
        stockRFIcon = '▼'
    else:
        stockRFColor = '#4d4d4d;' #gray
        stockRFIcon = '-' #━

    if stockInfo.high>stockInfo.now:
        stockHighColor = '#ed344a;'
    else:
        stockHighColor = '#000000;'

    if stockInfo.low<stockInfo.now:
        stockLowColor = '#40afde;'
    else:
        stockLowColor = '#000000;'

    


    html="""    
                 <tr>
                   <td align="center" style="padding:30px 30px 10px 30px;font-size:0;background-color:#ffffff;">
                     <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;">
                       <div align="center">
                         <img src=\""""\
                         +company_image\
                        +"""" width="115" alt="" style="width:80%;max-width:115px;margin-bottom:20px;">
                       </div>
                       <p style="margin-top:0;margin-bottom:12px;font-size:16px;text-align:center;">"""\
                        +company_name\
                        +"""<span style="font-size:14px;color:gray;">&nbsp;"""\
                        +stockNumber\
                        +"""</span><p>
				        <p style="margin-top:0;margin-bottom:12px;font-size:18px;text-align:center;color:"""\
				        +stockRFColor\
				        +""""">"""\
                        +str(format(stockInfo.now,','))\
                        +"""<br><span style="font-size:16px;">"""

    print(stockInfo.diff)
    print(type(stockInfo.diff))
    # formattedDiff = format(stockInfo.diff,',')

    stockRFInfo = stockRFIcon+" "+str(format(stockInfo.diff,','))+" ("
    if int(stockInfo.diff)>0:
        stockRFInfo+="+"
    stockRFInfo += str(stockInfo.rate)+"%)"

    html+=stockRFInfo\
    +"""
                          </span>
                        </p>
                      </div>
                      <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                      
                        <table role="presentation" style="width:100%;max-width:600px;border:none;border-spacing:0;font-size:16px;line-height:22px;color:#363636;">
				          <tr>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">전일종가</td>
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">고가</td>
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">저가</td>
				          </tr>
				          <tr>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;">"""\
                            +str(format(stockInfo.prev,','))\
                        +"""</td> 
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;color:"""\
                            +stockHighColor\
                            +"""">"""\
                            +str(format(stockInfo.high,','))\
                            +"""</td>
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;color:"""\
                            +stockLowColor\
                            +"""">"""\
                            +str(format(stockInfo.low,','))\
                            +"""</td>
				          </tr>
				          <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
				          <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
				          <tr>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">거래량</td>
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">시가총액</td>
					        <td align="center" style="padding:0;font-size:16px;line-height:28px;font-weight:bold;width:33%;">거래대금(백만)	</td>
				          </tr>
				          <tr>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;">""" \
                            + str(format(stockInfo.quant, ','))\
                            +"""</td>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;">""" \
                            + sc.getFormattedKoreanNumStr(stockInfo.marketSum)\
                            +"""</td>
				            <td align="center" style="padding:0;font-size:16px;line-height:28px;width:33%;">""" \
                            + str(format(stockInfo.amount, ','))\
                            +"""</td>
				          </tr>
				        </table>
                      </div>
                    </td>
                   </tr>
                   <tr>
                     <td align="center" style="padding:20px 30px 20px 30px;font-size:18px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                       <p style="margin:0;">
                         <a href=\""""\
                         +stockLink\
                         +""""style="text-decoration:none; background: #7C7877; text-decoration: none; padding: 10px 25px; color: #ebe6e1; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#ff3884">
                            <span style="mso-text-raise:10pt;font-weight:bold;">주가 정보 바로가기</span>
                         </a>
                       </p>
                     </td>
                   </tr>"""
    return html


def getHtmlFormat(htmlStr):
    html = """<!DOCTYPE html>
                <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">"""
    html+=htmlStr
    html+= """</html>"""

    return html


def getRefinedNewsContentsForResponsiveHtml(newsDict):
    #commit test after changing prj name
    # company_name = "삼성전자"
    # company = cc.getCompanyByName(company_name)
    # stockNumber = company.company_ssc
    # news_link = "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=014&aid=0004704537"
    # company_website = "https://www.samsung.com/sec/"

    # cnt = 1
    # newstitle = """'2차전지 부품제조' 지아이텍, 증권신고서 제출..."10월 코스닥 상장"""
    # company_image = "https://lh3.googleusercontent.com/proxy/WvN5LD33iG6opFBGXBhN0Rx6eFAFdJ5KkjSUMG_cFqX2Zxzx7k6f3w3FdE3SiHs-MPiDskNSrPWOO-eDB8Zulmias4rjmnPnBq0vhLoVEf0m"
    # headlinetitleLink = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw1aWzSzE8CmpHUrma7dYdC702aw869hDNmQ&usqp=CAU"
    headlinetitleImage = "https://github.com/francisBae/proj_webcrawler/blob/master/static/titleImg.jpg?raw=true"
    # stockNumber = "005930"
    stockLink = "https://finance.naver.com/item/main.nhn?code="
    news_today_mail_yn = ccc.getCmmnCdVal('C0001', 'NEWS_TODAY_MAIL_YN') #오늘자 기사만 보낼지 여부
    current_stock_info_mail_yn =  ccc.getCmmnCdVal('C0002', 'CURRENT_STOCK_INFO_MAIL_YN') #주가정보 전송할지 여부

    html = getNewsHeader()+"""
            <body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
              <div role="article" aria-roledescription="email" lang="ko" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#f0e5de;">
                <table role="presentation" style="width:100%;border:none;border-spacing:0;">
                  <tr>
                    <td align="center" style="padding:0;">
                      <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                        <tr>
                          <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;">
                            <a href="http://www.naver.com/" style="text-decoration:none;"><img src=\""""\
                            +headlinetitleImage\
                            +"""" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a>
                          </td>
                        </tr>
                        """
    for company_name in newsDict:
        # print(company_name)  # 삼성전자
        company = cc.getCompanyByName(company_name)
        stockNumber = company.company_ssc
        # company_image = company.company_image
        company_image = "https://github.com/francisBae/python-naver-news-crawler/blob/master/static/companyImage/"\
                        +str(stockNumber)\
                        +".png?raw=true"
        #이미지가 자주 만료되는 현상으로 인해 깃허브 저장소에 업로드


        if company.company_world_stock_yn == 'Y':
            stockLink = "https://m.stock.naver.com/index.html#/worldstock/stock/" + stockNumber+".O"

            html+=getCompanyImgTitle(stockLink, company_image, company_name, stockNumber) #해외는 무조건 기존 타이틀대로

        else:
            stockLink = "https://finance.naver.com/item/main.nhn?code=" + stockNumber

            if current_stock_info_mail_yn == 'Y': #현재주가를 표시하기로 했을 때
                html+=getCompanyStockTitle(stockLink, company_image, company_name, stockNumber)
            else: #표시 안하기로 하면
                html+=getCompanyImgTitle(stockLink, company_image, company_name, stockNumber)

        subcnt = 0
        for newstitle in newsDict[company_name]:
            news_link = newsDict[company_name][newstitle]["link"]
            news_pupdate = dc.convertStringToDate(newsDict[company_name][newstitle]["pubDate"])
            # news_today_mail_yn = 'N' #테스트용 플래그 설정
            if news_today_mail_yn == 'Y':
                if dc.isDateTodayYn(news_pupdate) is False:
                    continue #오늘 뉴스 아니라면 스킵
            subcnt += 1
            html+=\
            """
                        <tr>
                          <td style="padding:20px;font-size:20px;line-height:28px;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                            <p style="margin:0;font-size:15px; color:#a3a09d">"""\
                               +str(news_pupdate)\
                               +"""</p>
                            <p style="margin:0; font-weight: 700;">"""
            html+=str(subcnt)
            html+=\
                        """] <a href="""\
                        +news_link\
                        +"""" style="color: #274c5e;text-decoration:none;">"""
            newstitle = newstitle.replace("<b>","<font color =\"#7f9eb2\">")
            newstitle = newstitle.replace("</b>", "</font>")
            html+=newstitle\
                        +"""</a></p>
                          </td>
                        </tr>"""
    html+=\
        """
                        <tr>
                          <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                            <p style="margin:0 0 8px 0;"><a href="http://www.facebook.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="http://www.twitter.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                            <p style="margin:0;font-size:14px;line-height:20px;">&reg; Jonghoo Bae, Korea 2021<br><a class="unsub" href="http://www.example.com/" style="color:#cccccc;text-decoration:underline;">Unsubscribe instantly</a></p>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </div>
            </body>
"""
    html = getHtmlFormat(html)

    soup = bs(html, "html.parser")
    print(soup.prettify())

    return html
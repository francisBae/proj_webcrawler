from datetime import datetime
from Utils import DateConverter as dc
from Keyword import CompanyController as cc
from CmmnCd import CmmnCdController as ccc

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


def getRefinedNewsContentsForResponsiveHtml(newsDict):

    # company_name = "삼성전자"
    # company = cc.getCompanyByName(company_name)
    # stockNumber = company.company_ssc

    # news_link = "https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=101&oid=014&aid=0004704537"
    # company_website = "https://www.samsung.com/sec/"
    cnt = 1
    # newstitle = """'2차전지 부품제조' 지아이텍, 증권신고서 제출..."10월 코스닥 상장"""
    # company_image = "https://lh3.googleusercontent.com/proxy/WvN5LD33iG6opFBGXBhN0Rx6eFAFdJ5KkjSUMG_cFqX2Zxzx7k6f3w3FdE3SiHs-MPiDskNSrPWOO-eDB8Zulmias4rjmnPnBq0vhLoVEf0m"
    headlinetitleLink = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw1aWzSzE8CmpHUrma7dYdC702aw869hDNmQ&usqp=CAU"
    headlinetitleImage = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Headlines_Today_logo.svg/1200px-Headlines_Today_logo.svg.png"
    # stockNumber = "005930"
    stockLink = "https://finance.naver.com/item/main.nhn?code="

    html = """\
    <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width,initial-scale=1">
                <meta name="x-apple-disable-message-reformatting">
            <title></title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@700&display=swap" rel="stylesheet">
            
            
            <style>
                table, td, div, h1, p {
                    font-family: 'Nanum Gothic', sans-serif;
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
            <body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
              <div role="article" aria-roledescription="email" lang="ko" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">
                <table role="presentation" style="width:100%;border:none;border-spacing:0;">
                  <tr>
                    <td align="center" style="padding:0;">
                      <!--[if mso]>
                      <table role="presentation" align="center" style="width:600px;">
                      <tr>
                      <td>
                      <![endif]-->
                      <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                        <tr>
                          <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;">
                            <a href=\""""\
                            +headlinetitleLink\
                            +"""" style="text-decoration:none;"><img src=\""""\
                            +headlinetitleImage\
                            +"""" width="300" alt="Logo" style="width:80%;max-width:300px;height:auto;border:none;text-decoration:none;color:#ffffff;"></a>
                          </td>
                        </tr>"""
    for company_name in newsDict:
        print(company_name)  # 삼성전자
        company = cc.getCompanyByName(company_name)
        stockNumber = company.company_ssc

        if company.company_world_stock_yn == 'Y':
            stockLink = "https://m.stock.naver.com/index.html#/worldstock/stock/" + stockNumber+".O"
        else:
            stockLink = "https://finance.naver.com/item/main.nhn?code=" + stockNumber
        company_image = company.company_image

        html+=\
            """<tr>
               <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;">
                <a href="""\
                +stockLink\
                +"""" style="text-decoration:none;"><img src=\""""\
                +company_image\
                +"""" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a>
              </td>
            </tr>
                <tr>
                  <td style="padding:30px;font-size:24px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                    <h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;">"""\
                    +company_name+" ("+"""<a href=\""""+(stockLink)+"""">"""+stockNumber+"</a>)"\
                    +"""</h1></tr>"""

        subcnt = 0
        for newstitle in newsDict[company_name]:

            news_link = newsDict[company_name][newstitle]["link"]
            news_pupdate = dc.convertStringToDate(newsDict[company_name][newstitle]["pubDate"])

            news_today_mail_yn = ccc.getCmmnCdVal('C0001','NEWS_TODAY_MAIL_YN')

            if news_today_mail_yn == 'Y':
                if dc.isDateTodayYn(news_pupdate) is False:
                    continue #오늘 뉴스 아니라면 스킵

            subcnt += 1

            html+=\
                    """<tr><td style="padding:20px;font-size:18px;line-height:28px;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                    <p style="margin:0;">"""\
                    +str(news_pupdate)\
                    +"""</p>
                    <p style="margin:0;">"""
            html+=str(subcnt)
            html+=\
                    """) <a href="""\
                    +news_link\
                    +""">"""\
                    +newstitle\
                    +"""</a></p>
                  </td>
                </tr>"""



    html+=\
                        """
                        
                        <tr>
                          <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                            <p style="margin:0 0 8px 0;"><a href="http://www.facebook.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="http://www.twitter.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                            <p style="margin:0;font-size:14px;line-height:20px;">&reg; Someone, Somewhere 2021<br><a class="unsub" href="http://www.example.com/" style="color:#cccccc;text-decoration:underline;">Unsubscribe instantly</a></p>
                          </td>
                        </tr>
                      </table>
                      <!--[if mso]>
                      </td>
                      </tr>
                      </table>
                      <![endif]-->
                    </td>
                  </tr>
                </table>
              </div>
            </body>
            </html>"""

    return html
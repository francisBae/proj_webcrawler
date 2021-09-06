import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

#메일 전송을 위한 정보
from . import MailSenderInfo as msi

def sendEmail(email_targets, title,contents):
    # 로그인하기
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(msi.sender_email, msi.sender_pw)

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = title  # "보낼 메일 제목"
    msg['From'] = msi.sender_email
    receiver_email = ""

    # 메일 내용 쓰기
    # part2 = MIMEText(contents, 'plain')  # 보낼 메일의 내용 담기
    part2 = MIMEText(contents, 'html')  # 보낼 메일의 내용 담기
    msg.attach(part2)

    # 받는 사람 정보
    for target in email_targets:
        receiver_email = target #받는 사람 이메일
        msg['To'] = receiver_email


        # 파일 첨부하기
        # part = MIMEBase('application', "octet-stream")
        # with open("articles.xlsx", 'rb') as file:
        #     part.set_payload(file.read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx") # 첨부파일 이름
        # msg.attach(part)

        # 메일 보내고 서버 끄기
        s.sendmail(msi.sender_email, receiver_email, msg.as_string())
        print(receiver_email+" 메일 전송 완료")
        
    s.quit()

def refineHtml(text):
    return "<html><body>"+text+"</body></html>"

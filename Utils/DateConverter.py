from datetime import datetime
from time import strptime


def convertStringToDate(dateStr):
    '''
    Format
    Wed, 01 Sep 2021 13:20:00 +0900
    Tue, 07 Sep 2021 11:30:00 +0900
    Tue, 07 Sep 2021 17:39:00 +0900 
    '''

    try:
        month = str(strptime(dateStr[8:11], '%b').tm_mon)
        year = dateStr[12:16]
        day = dateStr[5:7]
        hhmmdd = dateStr[17:25]

        dateTimeStr = year+'-'+month+'-'+day+' '+hhmmdd
        dateTimeObj = datetime.strptime(dateTimeStr,'%Y-%m-%d %H:%M:%S')


        print(dateTimeObj)
        return dateTimeObj
    except:
        return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def convertDateStringToKorean(dateStr):
    '''
    Format
    2021-09-06 17:53:00
    '''
    koreanDate = dateStr[0:4]+"년 "+str(int(dateStr[5:7]))+"월 "+str(int(dateStr[8:10]))+"일 "+dateStr[11:]

    return koreanDate

def isDateTodayYn(dateObj):
    # paramDate = datetime.strptime(dateObj,'%Y-%m-%d')
    # todayDate = datetime.today().strftime('%Y-%m-%d')

    if dateObj.date() == datetime.today().date():
        return True
    else:
        return False



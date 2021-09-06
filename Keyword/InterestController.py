from MariaDb import QueryStatements as qs, DbConnector
from . import InterestInfo

def getInterestList():
    query = qs.getInterestInfoForKeyword()
    interestDataset = DbConnector.selectQuery(query)

    interestList = list()
    for intr in interestDataset:
        interest = InterestInfo.InterestInfo(str(intr['interest_seqno']), intr['interest_name'],intr['interest_keyword_use_yn'])
        interest.printInfo()
        interestList.append(interest)

    # return interestList
    return interestList

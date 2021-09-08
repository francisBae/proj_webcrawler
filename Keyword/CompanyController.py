from MariaDb import QueryStatements as qs, DbConnector
from . import CompanyInfo

def getCompanyList():
    query = qs.getCompanyInfoForKeyword()
    companyDataset = DbConnector.selectQuery(query)

    companyList = list()
    for com in companyDataset:
        company = CompanyInfo.CompanyInfo(str(com['company_seqno']), com['company_ssc'], com['company_name'],
                                          com['company_website'],
                                          com['company_keyword_use_yn'], com['company_stock_use_yn'], com['company_world_stock_yn'], com['company_image'])
        company.printInfo()
        companyList.append(company)

    # return companyList
    return companyList

def getCompanyByName(company_name):
    query = qs.getCompanySscByName(company_name)
    companyDataset = DbConnector.selectQuery(query)

    for com in companyDataset:
        company = CompanyInfo.CompanyInfo(str(com['company_seqno']), com['company_ssc'], com['company_name'],
                                          com['company_website'],
                                          com['company_keyword_use_yn'], com['company_stock_use_yn'], com['company_world_stock_yn'], com['company_image'])
        company.printInfo()
        break

    # return companyList
    return company
from . import CmmnCdInfo
from MariaDb import QueryStatements as qs, DbConnector

def getCmmnCdVal(grp_cd, cmmn_cd):
    query = qs.getCmmnCdInfo(grp_cd, cmmn_cd)
    cmmnCdDataset = DbConnector.selectQuery(query)

    for cmmn_cd_data in cmmnCdDataset:
        cmmn_cd = CmmnCdInfo.CmmnCdInfo(cmmn_cd_data['grp_cd'], cmmn_cd_data['cmmn_cd'], cmmn_cd_data['cmmn_cd_nm'],
                                        cmmn_cd_data['cmmn_cd_val'])
        # cmmn_cd.printInfo()
        break

    # return subscr_infos
    return cmmn_cd.cmmn_cd_val
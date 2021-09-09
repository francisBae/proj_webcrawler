class CmmnCdInfo:
    def __init__(self,grp_cd, cmmn_cd, cmmn_cd_nm, cmmn_cd_val):
        self.grp_cd = grp_cd
        self.cmmn_cd = cmmn_cd
        self.cmmn_cd_nm = cmmn_cd_nm
        self.cmmn_cd_val = cmmn_cd_val
    def printInfo(self):
        print(self.grp_cd+" | 코드 : "+self.cmmn_cd +" | 코드명 : "
              +self.cmmn_cd_nm+" | 코드값 : "+self.cmmn_cd_val)
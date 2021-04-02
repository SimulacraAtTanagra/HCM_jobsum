# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:07:31 2021

@author: shane
"""
from src.seltools import main
from src.HCM_main import hcm
from time import sleep


 
class jobsummary(hcm,main):
    search=("#ICSearch")
    def __init__(self,driver):
        self.driver=driver
        self.url="https://hrsa.cunyfirst.cuny.edu/psp/cnyhcprd/EMPLOYEE/HRMS/c/CU_E065_JOB_SUMMARY.CU_JOB_SUMMARY.GBL"
        self.searchfield="CU_JOB_SUM_SRCH_EMPLID"
    def survey(self):
        return(self.outer_instance.survey())
    def nav(self):
        self.outer_instance.nav(self.url,self.searchfield)
    
    def downloader(self,emplid):    #TODO modify to accept multiple values
        self.data_distribute({"CU_JOB_SUM_SRCH_EMPLID":f'{emplid}'})
        self.waitid(self.search)
        self.wait_spin()
        self.waitid("ICTAB_HIDE_29")
        sleep(1)
        self.waitid("WF_JOB_SUMM$hexcel$0")
        sleep(5)
        jsrename(emplid,download_dir)
        self.nav()
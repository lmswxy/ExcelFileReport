import os
import sys
import pandas as pd
import matplotlib as mp
import xlrd
import xlwt
import platform
import csv
import getpass
import time 
import getopt
import subprocess
import threading
import optparse

PARAM_DUT                      = 'HAWKEYE'
PARAM_TEST_PLAN_COVER          = 'Testplan Cover'
PARAM_TEST_PLAN_DEFINITION     = 'Definitions'
PARAM_TEST_PLAN_REVISION       = 'Revision'
PARAM_TEST_BLOCK_WIFI_SOC      = 'WIFI_SoC'
PARAM_TEST_BLOCK_QDSP6SS       = 'QDSP6SS'
PARAM_TEST_BLOCK_DATAPATH      = 'WIFI_M2M_DATAPATH'
PARAM_TEST_CASE_QUALITY        = ['Q0','Q1','Q2','Q3']
PARAM_TEST_CASE_PRIORITY       = ['P0','P1','P2','P3']
PARAM_TEST_RESULT_PASS         = 'PASS'
PARAM_TEST_RESULT_FAIL         = 'FAIL'
PARAM_TEST_RESULT_NOTRUN       = 'Not Run'
PARAM_TEST_RESULT_UNDERRUN     = 'Under Run'
PARAM_TEST_RESULT_NA           = 'NA'

def Search_File(FileName, SearchPath, PathSep=os.pathsep):
    for path in SearchPath.split(os.pathsep):
        candidate = os.path.join(path, FileName)
        if os.path.isfile(candidate):
            yield os.path.abspath(candidate)

def FileExist(FileName, SearchPath):
    find_file = list(Search_File(FileName, SearchPath))
    if find_file:
	return True
    else:
	return False

def PlatformInfo():
    if platform.platform()[:3].lower() == 'win':
	return 'Windows'
    elif platform.platform()[:3].lower() == 'lin':
	return 'Linux'
    else:
	pass

def MarkTestResulttoTestPlan(ResultFileName, TestPlanName):
    
def parse_args():
    usage = u'''To Find a file, the 1st para is path, and the 2nd para is file name'''
    parser = optparse.OptionParser(usage)
    help = u'The target file name'
    parser.add_option('--filename', help=help)
    help = u'multi path which seperate via ',''
    parser.add_option('--path', help=help, default='e:')
    options, args = parser.parse_args()
    return options, args

if __name__ == '__main__':
    print FileExist('Hawkeye_WiFi_SoC_VI_Testplan.xlsx',os.getcwd())
    print PlatformInfo()

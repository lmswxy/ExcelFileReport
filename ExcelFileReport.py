import os
import sys
import panda as pd
import matplotlib as mp
import xlrd
import xlwt
import platform
import csv

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


#-*-:coding utf-8 -*

"""
author:rontgen(wanggeng)
Date: 2018-08-08
Function Description:
    1. read, write, add, del, modify, query operation for excel files
    2. read data from excel, analyze and draw graphic chart
"""

# -*-: coding: utf-8 -*

# -*-: coding: utf-8 -*
import openpyxl as ox

import os, sys, string
from wgkits.build_tool import *
import math

ref=string.ascii_uppercase

cur_dir = os.getcwd()

def read_xlsx(file_path):
    file_path = unicode(path2unix(file_path), 'utf8')
    wb = ox.load_workbook(file_path)
    return wb

def write_xlsx(file_path, wb):
    folder_name = os.path.dirname(path)
    if not has_dir(folder_name):
        os.makedirs(folder_name)
    wb.save(file_path)

def modify_xlsx():
    pass

def query_xlsx_coordinate():
    pass

def query_xlsx_data():
    pass

def rc2cor(row, column):
    remainder = 0
    ret = 0
    rl = []
    result=""
    pow_num = 10
    lenlist=0
    while True:
        rt = column - math.pow(26, pow_num)
        if rt > 0:
            break
        else:
            pow_num = pow_num -1
    print("pow_num=%s" %pow_num)
    lenlist = pow_num
    while True:
        ret = int(round(math.floor(column / math.pow(26, pow_num))))
        remainder = column % 26
        if ret >= 0:
            print("remainder=%d" %remainder)
            print("ret=%d" %ret)
            rl.append(ret)
            remainder = 0
            column = column - math.pow(26, pow_num)
            pow_num = pow_num - 1
        else:
            ret=""
            print("remainder=%s" %remainder)
            if remainder >= 1: 
                remainder = ref[int(round(remainder)) -1]
            else:
                remainder=""
            break
                
    print("rl=%s" %rl)
    index=-1
    if len(rl) < lenlist:
        tmp = [0] * (lenlist-len(rl))
        rl=rl+tmp
    for m in rl[::-1]:
        #if m > 0
        index=index-1
        print("index=%d" %index)
        if -index > len(rl):
            break
        if m == 0 and rl[index]>0:
            rl[index+1]=rl[index+1]+26
            rl[index]=rl[index]-1
        print("reorder list=%s" %rl)
    for m in rl[::-1]: 
        if m >0:   
            result=ref[m-1]+result
    print("result=%s" %result)
    return result+remainder+ str(row)

def cor2rc(corstr):
    pass

def main():
    file_path = path2unix(os.path.join(cur_dir, "新建 Microsoft Office Excel 工作表.xlsx"))
    wb = read_xlsx(file_path)
    sheet_list = wb.sheetnames
    print(sheet_list)
    sh1=sheet_list[0]
    sheet = wb.get_sheet_by_name(sh1)
    for row in sheet.iter_rows():
        for cell in row:
            print(cell.coordinate)
            print(cell.value)
    
    print(sheet.max_row, sheet.max_column)
    print(wb.active)
    print(rc2cor(3,456977))
    #print(math.pow(26, 10))


if __name__ == '__main__':
    main()
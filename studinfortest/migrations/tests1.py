#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : tests1.py
# @Author: 橘子
# @Date  : 2020/12/25
# @Desc  : execise


import xlrd
import xlwt
from random import Random

def set_style(name,height,bold=False):
    style = xlwt.XFStyle        #初始化样式

    font = xlwt.Font()
    #为样式创建字体
    font.name = name           #Times New Roman'
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font

    return style

    # borders = xlwt.Borders()
    # borders.left = 6
    # borders.right = 6
    # borders.top = 6
    # borders.bottom = 6


    # style.borders = borders


def write_excel():
    f = xlwt.Workbook()         #创建工作簿

    '''
    创建第一个sheet:
    sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)      #创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车标', u'汽车票', u'其它']
    status = [u'预定', u'出票', u'退票', u'业务小计']
    #生成第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))

    #生成第一列和最后一列（全并4行）
    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i+3, 0, 0, column0[j], set_style('Arial', 220, True))
        sheet1.write_merge(i, i+3, 7, 7)            #最后一列“合计”
        i += 4
        j += 1

    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))
    #生成第二列
    i = 0
    while i < 4 * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j+i+1, 1, status[j])
        i += 4
    f.save('demo1.xls')        #保存文件
if __name__ == '__main__':
    write_excel()
    # sheet2 = f.add_sheet(u'sheet2', cell_overwrite_ok=True)      #创建sheet2
    # row0 = [u'姓名', u'年龄', u'出生日期', u'爱好', u'关系']
    # column0 = [u'小杰', u'小胖', u'小明', u'大神', u'大仙', u'小敏', u'无名']
    #
    # #生成第一行
    # for i in range(0, len(row0)):
    #     sheet2.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    #
    # #生成第一列
    # for i in range(0, len(column0)):
    #     sheet2.write(i+1, 0, column0[i], set_style('Times New Roman', 220))
    #
    # sheet2.write(1, 2, '1991/11/11')
    # sheet2.write_merge(7, 7, 2, 4, u'暂无')          #合并列单元格
    # sheet2.write_merge(1, 2, 4, 4, u'好朋友')         #合并行单元格
    # f.save('demo1.xlsx')        #保存文件






#打开excel文件
# data = xlrd.open_workbook(r'G:\1.xls', "rb")
# # r = Random



#获取所有sheet表名
# sheet_name = data.sheet_names()
# print(sheet_name)
# #根据sheet索引或者名称获取sheet内容
#
# sheet2 = data.sheet_by_name('oms_robots')
# #sheet表里的名称，行数，列数
# print(sheet2.name, sheet2.nrows, sheet2.ncols)
# nrows = sheet2.nrows
# ncols = sheet2.ncols



# r = Random()
# winner = lists[r.randrange(0, len(lists), 1)]
# print('The winner is :%s' % winner['ID'])
# print('The winner is :%s' % winner['等级'])


#遍历行和列
# for i in range(nrows):
#     for j in range(ncols):
#
#         print(sheet2.cell(i, j).value)

#获取整行和整列的值（数组）
# rows = sheet2.row_values(3)    #获取第四行内容
# cols = sheet2.col_values(2)     #获取第三列内容
# row1 = sheet2.row(1)
# col1 = sheet2.col(4)

# print(rows)
# print(cols)

#获取单元格内容
# cell1 = sheet2.cell(1, 0).value
# cell2 = sheet2.cell_value(2, 1).encode('utf-8')
# cell3 = sheet2.row(1)[4].value
# print('cell1:%s' % cell1, 'cell2:%s' % cell2, 'cell3:%s' % cell3)

#获得sheet3表里的索引所有数据。
sheet3 = data.sheet_by_index(0)

#循环获得sheet2表里的内容
# for i in range(sheet2.nrows):
#     rowlist = sheet2.row_values(i)
#     print(rowlist)



#获取单元格内容数据类型
# print(sheet2.cell(1, 5).ctype)
# data_value = xlrd.xldate_as_tuple(sheet2.cell_value(1, 5), data.datemode)
# data_tmp = data_value[:3]
# print(data_tmp)
# ids = sheets.cell(row=1, column=1).value
#
# print(ids)



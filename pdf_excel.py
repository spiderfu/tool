# -*- coding: utf-8 -*-
"""
@Time : 2019/12/4 10:15
@Author : Spider fu
@File : pdf_excel.py
"""
import pdfplumber
pdf = pdfplumber.open(".pdf")
# 这里只读取了第一页，我的文档第一页是有表格的，
# 自己相应的改表格的页码就行了，示例代码
page = pdf.pages[0]
for row in page.extract_tables():
    print(row)
    print(row[0])

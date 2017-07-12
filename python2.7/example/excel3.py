import xlwt
filename = xlwt.Workbook ()
sheet = filename.add_sheet('name')
sheet.write(0,0,'hao123')
filename.save('test.xls')
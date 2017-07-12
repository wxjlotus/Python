import xlrd
workbook = xlrd.open_workbook('成绩单.xls')
print "There are {} sheets in the workbook".format(workbook.nsheets)
for booksheet in workbook.sheets():
    print booksheet.name
    for row in xrange(booksheet.nrows):
        for col in xrange(booksheet.ncols):
            print xlrd.cellname(row, col)
            print booksheet.cell(row, col).value
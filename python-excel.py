import xlrd
l=('C:\Users\Jaiswal7N\Downloads\Python\python\python-test-data.xlsx')
w=xlrd.open_workbook(l)
s=w.sheet_by_index(0)
x=[]
y=[]
for i in range(s.nrows):
	x.append(s.cell_value(i,0))
for i in range(s.nrows):
	y.append(s.cell_value(i,1))
print(x[1:s.nrows])
print(y[1:s.nrows])
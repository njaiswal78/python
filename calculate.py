def sum(x,y):
	return x+y
def sub(x,y):
	if x>y:
		return x-y
	else:
		return y-x
def mul(x,y):
	return x*y
def div(x,y):
	if y==0:
		print('Division by 0 is not possible')
	else:
		return float(x/y)
import calculate
print("Enter two numbers two do +,-,*,/")
print('a= ')
a=input()
print('b= ')
b=input()
print("Operation to be applied= ")
c=input()
if c=='+':
	print(calculate.sum(a,b))
elif c=='-':
	print(calculate.sub(a,b))
elif c=='*':
	print(calculate.mul(a,b))
else:
	print(calculate.div(a,b))

x=dir(calculate)
print(x)
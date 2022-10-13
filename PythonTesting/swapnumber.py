#by using temp variable
x=5
y=10

temp=x
x=y
y=temp

print('the value of x after swap:{}',format(x))
print('the value of y after swap:{}',format(y))


#without using temp variable
x=5
y=10

x,y=y,x

print("x=",x)
print("y=",y)
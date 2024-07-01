a=input()
b=input()

x=list(map(int,a))
y=list(map(int,b))

print(( x[0] * 100 * y[2] ) + ( x[1] * 10 * y[2] ) + ( x[2] * y[2] ))
print(( x[0] * 100 * y[1] ) + ( x[1] * 10 * y[1] ) + ( x[2] * y[1] ))
print(( x[0] * 100 * y[0] ) + ( x[1] * 10 * y[0] ) + ( x[2] * y[0] ))
print(int(a)*int(b))
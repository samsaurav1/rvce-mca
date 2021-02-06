# operators: Operators are special symbols in Python that carry out
#  arithmetic or logical computation. The value that the operator
#  operates on is called the operand.

# plus : +
# minus : -
# mult : *
# div : /
# modulo : %
# floor div : //
# square : **

# saurav apply all operators on two number and show the result

f1 = int(input("First number: "))
f2 = int(input("Second number: "))

plus = f1 + f2
minus = f1 - f2
mult = f1 * f2
div = f1 / f2
modulo = f1 % f2
floorDiv = f1 // f2
sqr = f1 ** f2

print("--"*20)

print(plus)
print(minus)
print(mult)
print(div)
print(modulo)
print(floorDiv)
print(sqr)

print("--"*20)

# return true or false after comparison
print("Comparison operators")
x = int(input("First number: "))
y = int(input("Second number: "))


print('x > y is',x>y)


print('x < y is',x<y)


print('x == y is',x==y)


print('x != y is',x!=y)


print('x >= y is',x>=y)


print('x <= y is',x<=y)

# arithmetic operator
a=10
b=5
print(a + b)   #output=15
print(a - b)   # 5
print(a * b)   # 50
print(a / b)   # 2.0
print(a // b)  # 2
print(a % b)   # 0
print(a ** b)  # 100000


# comparison operator
x=10
y=5
print(x == y)    # False
print(x !=  y)   # True
print(x > y)     # True
print(x < y)     # Flase
print(x >= 10)   # True
print(x <= 5)    # True


# Assignment operator
x = 10
x += 5
x *= 2
x -= 10
print(x)  # output=20


# Logical operator
x = 10                     # 0utput=True
y = 20                     # True
print(x > 5 and y < 30)    # Flase 
print(x > 15 or y < 30)
print(not (x > 5 ))


# Membership operator
animals = ["cat","dog","fox"]   # output =True
print("cat" in animals)         # True
print("bull" not in animals)    # True
print("fox" in animals)         # Flase
print("dog" not in animals)


# Identity operator
a = [1,2,3]
b = a
c = [1,2,3]         # output=True
print(a is c)       # Flase
print(a is not c)   # True

# Bitwise operator
x = 5
y = 3
print(x & y)   # output=1
print(x | y)   # 7
print(x ^ y)   # 6
print(~x)      # -6
print(x << 1)  # 10
print(x >> 1)  # 2

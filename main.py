print("hello world")

print("hello people! Myself honey.I am here for learning python with all of you. Good to see you all")

print(80 - 50 , "it's Thirty")

name = "Hoor-Ul-Ain"
currentLearning = "Artificial Inteligence"
year = 1
feePerQtr = 4.5 

print("My name is: ", name)
print("currently.i am learning ",currentLearning)
print("this is a ", year , "year program")
print("the Fee we have to pay for ater every three moths is" ,feePerQtr,"K")
# OR
print(name,currentLearning,year)

print(type(name))  
# str
print(type(year))
# int
print(type(feePerQtr))
# float


"""
multi
line
comment
"""

a = 100 
b  = 2

#         #    "ARITHMETIC OPERATORS"


sum = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
power = a ** b
print(sum , diff , product , division, power)
      
#     #   relational operators

print(a == b)    
print(a != b)
print(a > b)
print(a < b)
print( a >= b)
print(a <= b)

#                 #  "ASSIGNMENT OPERATORS"

num1 = 10


num1 += 20
print( num1)
num1 -= 5
print( num1)
num1 *= 4
print( num1)
num1 /= 2
print( num1)
num1 %= 3
print( num1)
num1 **= 2
print( num1)

#    "LOGICAL OPERATORS"   (AND , OR , NOT)

a = 100 
b  = 2
print(not False)
print(not(a > b))
print(not(a < b))


val1 =False
val2 = True

print("AND operator:" , val1 and val2)

# only true if both values will be true


print("OR operator:" , val1 or val2)

# true if one of both values will be true

print((a != b) and (a >= b))
# " True"
print((a != b) or (a >= b))       
# " False"



x = 56
y = 32
z = 24

print((x > y) and (y > z))
# true
print((x > y) and (y < z))
# False
print((x < y) and (y < z))
# false
print((x < y) and (y > z))
# false

print((x > y) or (y > z))
# true
print((x > y) or (y < z))
# true
print((x < y) or (y < z))
# False
print((x < y) or (y > z))
# true

print(not(x > y))
# false
print(not(x < y))
# True
print(not(z > y))
# true
print(not(x > z))
# false


#                    "TYPE CONVERSION"


a = int(34)
b = 3
print(type(a))
# class 'int'
print( a + b)
# 37

# x = float("honey")
# error
y = str("hello")
print(type(y))


            # "INPUT STATEMENT"

age = input("what's your age? ")
print("I am" , age , "years old." )

name = input("What's your name?")
print("Myself" , name)

val = input("enter some value:")
print(type(val), val)

# avg area of square

a = float(input("enter 1 side"))
b = float(input("enter 2 side"))
print("avg=",(a+b)/2)
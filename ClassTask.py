"""
Subject : Computational Physics 
Faculty : Dr.Priyanka Jha 
These Codes are the Task Provided By Dr.Priyanka Jha as Daily Understanding Task.
Date:07/08/2026 
We are Currently learning beginners of Python.
"""

#Task 1 :Define 3 Variables... , Let's take x,y,z
x = 2 
y = 5.12
z = 'FUNNY'

#Task 2 : Convert String to an Integer

numstr = input("Enter a number and I will convert it to A Number: ")
while True:
    try:
        num = float(numstr)
        print(f"Converted number: {num} ")
        break
    except ValueError:
        print("Invalid input: Number Should Not Be String..")
        numstr = input("Enter a number and I will convert it to a Number: ")


#Task 3: A Short Code with 3 comments 
print(type(x)) #<class 'int'>
print(type(y)) #<class 'float'>
print(type(z)) #<class 'str'>

#Task 4: Analyse membership Operator with 2 comments
fruits =['apple','banana','mango','raspberry']
if 'apple' in fruits:
    print("There's apple In fruit basket") # This will print 

print('watermelon' in fruits) # false

#Task 5: Bitwise Operators
#There are 6 Bitwise operator, & (And) ,|(Or) , ^(XOR) , ~(NOT) , << (Bitwise Left) , >> (Bitwise Right).

num1 = 25 #in Binary 011001
num2 = 48 #in Binary 110000
print(num1 & num2) # Output :16 , which is 010000
#In binary Representation , 101 is 5 and 100 is 4 for an example, using & operator will return 1 if both bits are 1 else 0.

print(num1 | num2) # Output :57 , which is 111001, In | operator , values will be 1 if any Of bits is 1 if both are 0 then output is 0

print(num1 ^ num2) # Output :41

print(~num1) #Output: -26
print(~num2) #Output: -49

print(num1 << 1) #output: 50
print(num2 >> 1) #output: 24 , very fast way to double or half the number

#Task 6 : Relational Operators, ==(Equals) , >=(Greater/equal) , <=(Less/equal) , !=(not equal) , <(less), >(greater) 
print(num1>num2) #false
print(num1.is_integer() == num2.is_integer()) #True

#task 7 :Logical Operators , &&(and), ||(or), not(not)
print(num1 >20 and num1 <40) #True ,both condition must be true
print(num1 > num2 or num1 < num2) #True , any one condition true is true
print(not(num2 > num1)) #False , it was true but because of Not output is reversed

#Task 8:Assignment operator, assigns value to variable

sumNum = 10
sumNum += sumNum
print(sumNum) #output :20
multNum = 5
multNum *= multNum+1
print(multNum) #Output :30


#Task 9 Identity Operator , Unlike Membership operator , it checks whether it belongs to that memory address
a= 4
b=1
c=4
print(a is c)     #True
print(b is not c) #True
print(b is c)     #False

#Final Task 10 :apply bodmas.
bdmas_calc = float(a + b * ( c - b )/2)
print(bdmas_calc) #5.5, first bracket, 4-1 =3 . then open all, division 3/2 = 1.5 then multiply 1 * 1.5 = 1.5 then add 1.5 + 4 = 5.5 ,
#no subtraction as not mentioned outside bracket and brackets always first
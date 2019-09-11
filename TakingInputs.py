#Comment are made with a #
#It is essential you comment code

#This program will take two integers
#Multiply them

#Input
#The input function reutrn the string the user enterd
#All inputs start as Strings
#To change the type of variable you "Cast" it
#Casting is the process of changing type
name = input("Please input your name: ")
a = input("Please input first number ")
a = int(a) #Self-refrencing assignment statement
b = input ("Please input second number ")
b = int(b)
#Process

#What is process
product = a * b

#Output
print("Hi, "+name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")
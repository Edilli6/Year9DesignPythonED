import math

#Input 
#What inputs are needed to calculate the volume of a cylinder
name = input("What is your name: ")

radius = input ("Input radius (cm): ")
radius = int(radius)

height = input ("Input height (cm): ")
height = int(height)

#Process
#What formula is used to calculate the volume of a cylinder?
#V = pi * r * r * h 
volume = math.pi * radius * radius * height
volume = round(volume,2)

#Output
#What is important about the output?

print ("The volume is: ",volume)
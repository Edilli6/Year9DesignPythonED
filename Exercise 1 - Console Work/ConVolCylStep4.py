import math

print("\n\tThe volume of a cylinder is: ")
print("\n\t\t\tV = \u03C0 \u00d7 radius \u00b2 \u00d7 height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")
#Input 
#What inputs are needed to calculate the volume of a cylinder

file = open("data.txt","aclear")

name = input("\n\tWhat is your name: ")

radius = 1
height = 1

while (radius != 0 or height != 0): 

	try: 
		radius = input("\n\tInput radius (cm): ")
		radius = int(radius)

		height = input("\n\tInput height (cm): ")
		height = int(height)
	except:
		print("\n\t\tNumeric Type Required")
		height = -1
		radius = -1

	#Process
	#What formula is used to calculate the volume of a cylinder?
	#V = pi * r * r * h 
	
	volume = math.pi * radius * radius * height
	volume = round(volume,2)

	#Output
	#What is important about the output?
	
	print("\n\t\tHi "+name+"!")
	print("\n\t\tGive a cylinder with:")
	print("\t\tRadius = "+str(radius))
	print("\t\tHeight = "+str(height))
	print ("\t\tThe volume is: "+str(volume)+"\n")
	file.write(str(volume)+"\n")


else:
	print("\n\t\tYou have entered an invalid value")
	#Checks while boolean expression 


print("END PROGRAM")
file.close()
speedLimit = input("Enter the speed limit:")
speedLimit = float(speedLimit)

carspeed = input("Enter the car speed:")
carspeed = float(carspeed)


if carspeed <= speedLimit: 
	print("Congratulations, you are within the speed limit!")
elif carspeed - speedLimit <= 20 :
	print("You are speeding and your fine is $100.")
elif carspeed - speedLimit <= 30 :
	print("You are speeding and your fine is $270.")
elif carspeed - speedLimit > 30 :
	print("You are speeding and your fine is $500.")
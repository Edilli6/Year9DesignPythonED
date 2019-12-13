data =  open("randomdataextract.txt","r");

dataString = data.read()

dataList = dataString.split("\n")

print(dataList)

for i in range(0, len(dataList),1):
	dataList[i] = dataList[i].replace(",","")
	dataList[i] = float(dataList[i])

print(dataList)

#Create a loop that goes from 0 to the length of the list

minimum = min(dataList)
print("Min Is: "+str(minimum))

maximum = max(dataList)
print(maximum)

diff = maximum - minimum

smallest = dataList[0]

for i in range(0,len(dataList),1):
	if smallest > dataList[i]:
		smallest = dataList[i]

print("MIN IS: "+str(smallest))


for i in range(0,len(dataList),1):
	if maximum < dataList[i]:
		maximum = dataList[i]

print("MAX IS: "+str(maximum))

value = input("What number y'all want to set as upper limit")
value = float(value)

#Write a loop that will do some data analsis using value

ctr = 0
for i in range(0,len(dataList),1):
	if (dataList[i] < 100):
		ctr=ctr+1
		print(dataList[i])

print(ctr)




stringX = "Mr John Smith"
length = 13
string = []
for x in stringX:
	string.append(x)

posOfSpace = []
for x in range(len(string)):
	if(string[x] == " "):
		posOfSpace.append(x)
		string.append(" ")
		string.append(" ")

spaceN = 0
for x in posOfSpace: #2,7
	x += spaceN
	for i in range(len(string) - x):
		string[len(string) - 1 - i] = string[len(string) - 3 - i]
	string[x + 2] = "0"
	string[x + 1] = "2"
	string[x] = "%"
	spaceN += 2

output = ""
for x in string:
	output += x

print output

#Can't do it in place; 'str' object does not support item assignment
#I am shifting empty spaces in the end. Can I avoid that and do it dynamically?
def binarySearch(target, myList):
	found = False
	bottom = 0
	cnt = 0
	top = len(myList) - 1
	while(bottom <= top and not found):
		cnt += 1
		middle = (bottom + top)//2 
		if(myList[middle] == target):
			found = True;
		elif(myList[middle] > target):
			top = middle - 1
		else:
			bottom = middle + 1
	print("length of list is ", len(myList), "and # of searches done is ", cnt)
	return found

numberList = [1,4,5,6,7,8,10,21,14,16,17,18,20]
item = int(input("What number are you looking for? "))
isitFound = binarySearch(item,numberList)
if isitFound:
	print("Number", item, "is in the list!")
else:
	print("Number", item, "is not in the list!")

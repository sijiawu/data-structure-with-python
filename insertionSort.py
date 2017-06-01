myList = [9,8,7,6,5,4,3,2,1]

def insertionSort(myList):
	marker = 0
	while (marker < len(myList) - 1):
		print("in")
		marker += 1
		for i in range(marker-1):
			print("mylist[i] is",myList[i],"mylist[marker]is",myList[marker])
			if(myList[i] < myList[marker]):
				print("yes?")
				a = myList[i]
				myList[i] = myList[marker]
				myList[marker] = a
			break
	return myList

print(insertionSort(myList))

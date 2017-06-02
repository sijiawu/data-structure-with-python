myList = [9,8,7,6,5,4,5,4,3,2,1]

def insertionSort(myList):
	marker = 1
	while (marker < len(myList)):
		for i in range(marker):
			if(myList[i] > myList[marker]):
				j = marker 
				a = myList[j]
				while(j > i):
					myList[j] = myList[j-1]
					j-=1
				myList[i] = a
		marker += 1
	return myList

print(insertionSort(myList))

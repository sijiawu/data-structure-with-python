myList = [1,2,4,3,5,6,7,2]

def insertionSort(myList):
	marker = 1
	numberOfComparisons = 0
	while (marker < len(myList)):
		for i in range(marker):
			numberOfComparisons += 1
			if(myList[i] > myList[marker]):
				j = marker 
				a = myList[j]
				while(j > i):
					myList[j] = myList[j-1]
					j-=1
				myList[i] = a
		marker += 1
	print("# of comparisons using insertion sort:",numberOfComparisons)
	return myList

def bubbleSort(myList):
	upperLimit = len(myList) - 1
	numberOfComparisons = 0
	while (upperLimit > 0):
		i = 0
		while(i < upperLimit):
			numberOfComparisons += 1
			if(myList[i] > myList[i+1]):
				a = myList[i+1]
				myList[i+1] = myList[i]
				myList[i] = a
			i += 1
		upperLimit -= 1
	print("# of comparisons using bubble sort:",numberOfComparisons)
	return myList

insertionSort(myList)
bubbleSort(myList)

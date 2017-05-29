def bubbleSort(myList):
	upperLimit = len(myList) - 1
	numberOfSwaps = 0
	numberOfComparisons = 0
	while (upperLimit > 0):
		i = 0
		while(i < upperLimit):
			numberOfComparisons += 1
			if(myList[i] > myList[i+1]):
				numberOfSwaps += 1
				a = myList[i+1]
				myList[i+1] = myList[i]
				myList[i] = a
			i += 1
		upperLimit -= 1
	print("# of comparisons:",numberOfComparisons,"# of swaps:",numberOfSwaps)
	return myList

numberList = [9,8,7,5,6,4,3,2,1]
print(bubbleSort(numberList))

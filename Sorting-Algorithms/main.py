from Algorithms import *

ELEM_COUNT = 10000

numberArray = SortingAlgorithms.returnRandomArray(ELEM_COUNT)
startingTime = None
endingTime = None
differences = []

startingTime = time.time()
SortingAlgorithms.radixsort(numberArray)
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.quicksort(numberArray)
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.bubbleSort(numberArray)
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.selectionSort(numberArray)
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.mergeSort(numberArray)
endingTime = time.time()
differences.append(endingTime - startingTime)

dataHolder = {
    1: ["Radixsort", ELEM_COUNT, differences.pop(0)],
    2: ["Quicksort", ELEM_COUNT, differences.pop(0)],
    3: ["Bubblesort", ELEM_COUNT, differences.pop(0)],
    4: ["Selectionsort", ELEM_COUNT, differences.pop(0)],
    5: ["Mergesort", ELEM_COUNT, differences.pop(0)],
}

print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Type','Amount','Time (s)'))
for index, item in dataHolder.items():
    sortingType, count, timeNeeded = item
    print ("{:<8} {:<15} {:<10} {:<10}".format(index, sortingType, count, timeNeeded))
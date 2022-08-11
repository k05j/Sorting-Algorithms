from Algorithms import *

ELEM_COUNT = 5000
ALGORITHMS_COUNT = 9

randomArray = SortingAlgorithms.returnRandomArray(ELEM_COUNT)
numberArrays = [randomArray.copy() for i in range(ALGORITHMS_COUNT)]
startingTime = None
endingTime = None
differences = []

startingTime = time.time()
SortingAlgorithms.radixSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.quicksort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.bubbleSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.selectionSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.mergeSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.insertionSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.shellSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.randomQuickSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

startingTime = time.time()
SortingAlgorithms.countingSort(numberArrays.pop(0))
endingTime = time.time()
differences.append(endingTime - startingTime)

dataHolder = {
    1: ["Radixsort", ELEM_COUNT, differences.pop(0)],
    2: ["Quicksort", ELEM_COUNT, differences.pop(0)],
    3: ["Bubblesort", ELEM_COUNT, differences.pop(0)],
    4: ["Selectionsort", ELEM_COUNT, differences.pop(0)],
    5: ["Mergesort", ELEM_COUNT, differences.pop(0)],
    6: ["Insertionsort", ELEM_COUNT, differences.pop(0)],
    7: ["Shellsort", ELEM_COUNT, differences.pop(0)],
    8: ["Random Quicksort", ELEM_COUNT, differences.pop(0)],
    9: ["Countingsort", ELEM_COUNT, differences.pop(0)],
}

print ("{:<10} {:<20} {:<10} {:<10}".format('Pos','Type','Elements','Time (s)'))
for index, item in dataHolder.items():
    sortingType, count, timeNeeded = item
    print ("{:<10} {:<20} {:<10} {:<10}".format(index, sortingType, count, timeNeeded))
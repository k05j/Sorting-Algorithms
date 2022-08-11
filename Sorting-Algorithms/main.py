from Algorithms import *

ELEM_COUNT = 250
ALGORITHMS_COUNT = 9

randomArray = SortingAlgorithms.returnRandomArray(ELEM_COUNT)
numberArrays = [randomArray.copy() for i in range(ALGORITHMS_COUNT)]
startingTime = None
endingTime = None
differences = []


def trackTimeFromAlgorithm(algorithmIndex):
    global startingTime, endingTime, differences
    startingTime = time.time()

    match algorithmIndex:
        case 0:
            SortingAlgorithms.radixSort(numberArrays.pop(0))
        case 1:
            SortingAlgorithms.quicksort(numberArrays.pop(0))
        case 2:
            SortingAlgorithms.bubbleSort(numberArrays.pop(0))
        case 3:
            SortingAlgorithms.selectionSort(numberArrays.pop(0))
        case 4:
            SortingAlgorithms.mergeSort(numberArrays.pop(0))
        case 5:
            SortingAlgorithms.insertionSort(numberArrays.pop(0))
        case 6:
            SortingAlgorithms.shellSort(numberArrays.pop(0))
        case 7:
            SortingAlgorithms.randomQuickSort(numberArrays.pop(0))
        case 8:
            SortingAlgorithms.countingSort(numberArrays.pop(0))

    endingTime = time.time()

    differences.append(endingTime - startingTime)

if __name__ == "__main__":
    # Radix Sort
    trackTimeFromAlgorithm(0)
    # Quicksort
    trackTimeFromAlgorithm(1)
    # Bubble Sort
    trackTimeFromAlgorithm(2)
    # Selection Sort
    trackTimeFromAlgorithm(3)
    # Merge Sort
    trackTimeFromAlgorithm(4)
    # Insertion Sort
    trackTimeFromAlgorithm(5)
    # Shell Sort
    trackTimeFromAlgorithm(6)
    # Random Quick Sort
    trackTimeFromAlgorithm(7)
    # Counting Sort
    trackTimeFromAlgorithm(8)

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

    print("{:<10} {:<20} {:<10} {:<10}".format(
        'Pos', 'Type', 'Elements', 'Time (s)'))
    for index, item in dataHolder.items():
        sortingType, count, timeNeeded = item
        print("{:<10} {:<20} {:<10} {:<10}".format(
            index, sortingType, count, timeNeeded))
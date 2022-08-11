from cmath import log
import time, random

class SortingAlgorithms:
    @staticmethod
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return SortingAlgorithms.quicksort(less) + [pivot] + SortingAlgorithms.quicksort(greater)

    @staticmethod
    def radixSort(inputArray):
        maxEl = max(inputArray)

        maximumDigit = len(str(maxEl))
        placeVal = 1

        outputArray = inputArray
        while maximumDigit > 0:
            outputArray = SortingAlgorithms.__countingSortForRadix(outputArray, placeVal)
            placeVal *= 10  
            maximumDigit -= 1

        return outputArray

    @staticmethod
    def bubbleSort(array):
        for i in range(len(array)):
            for j in range(len(array) - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def selectionSort(array):
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min]:
                    min = j
            array[i], array[min] = array[min], array[i]
        return array

    @staticmethod
    def mergeSort(array):
        if len(array) > 1:
            divider = len(array) // 2
            left_side = array[:divider]
            right_side = array[divider:]

            SortingAlgorithms.mergeSort(left_side)
            SortingAlgorithms.mergeSort(right_side)

            i = j = k = 0

            while i < len(left_side) and j < len(right_side):
                if left_side[i] < right_side[j]:
                    array[k] = left_side[i]
                    i += 1
                else:
                    array[k] = right_side[j]
                    j += 1
                k += 1

            while i < len(left_side):
                array[k] = left_side[i]
                i += 1
                k += 1

            while j < len(right_side):
                array[k] = right_side[j]
                j += 1
                k += 1

        return array
    
    @staticmethod
    def insertionSort(array):
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1
        return array

    @staticmethod
    def shellSort(array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                j = i
                while j >= gap and array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]
                    j -= gap
            gap = gap // 2
        return array

    @staticmethod
    def randomQuickSort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[random.randint(0, len(array) - 1)]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return SortingAlgorithms.randomQuickSort(less) + [pivot] + SortingAlgorithms.randomQuickSort(greater)

    @staticmethod
    def countingSort(array):
        maxEl = max(array)
        countArrayLength = maxEl + 1
        countArray = [0 for i in range(countArrayLength)]

        for el in array: 
            countArray[el] += 1

        for i in range(1, countArrayLength):
            countArray[i] += countArray[i - 1] 

        outputArray = [0] * len(array)
        i = len(array) - 1
        while i >= 0:
            currentEl = array[i]
            countArray[currentEl] -= 1
            newPosition = countArray[currentEl]
            outputArray[newPosition] = currentEl
            i -= 1

        return outputArray

    @staticmethod
    def __countingSortForRadix(inputArray, placeValue):
        countArray = [0 for i in range(10)]
        inputSize = len(inputArray)

        for i in range(inputSize): 
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] += 1

        for i in range(1, 10):
            countArray[i] += countArray[i-1]
        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = inputArray[i]
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            i -= 1
            
        return outputArray
        
    @staticmethod
    def returnRandomArray(size):
        return [random.randint(0, size ^ 2) for i in range(size)]
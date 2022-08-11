import time

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
    def radixsort(array):
        queues = [[] for i in range(10)]
        maximum = max(array)
        for i in range(len(str(maximum))):
            for j in array:
                queues[int(j / (10 ** i) % 10)].append(j)
            array = []
            for q in queues:
                while len(q) > 0:
                    array.append(q.pop(0))
        return array

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
    def returnRandomArray(size):
        import random
        return [random.randint(0, size) for i in range(size)]
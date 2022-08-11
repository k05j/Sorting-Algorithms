def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


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

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
    
def returnRandomArray(size):
    import random
    return [random.randint(0, size) for i in range(size)]

test = returnRandomArray(500000)

import time

start = time.time()
radixsort(test)
end = time.time()
print("Radixsort took", end - start, "seconds for {} elements".format(len(test)))

start = time.time()
quicksort(test)
end = time.time()
print("Quicksort took", end - start, "seconds for {} elements".format(len(test)))

start = time.time()
bubbleSort(test)
end = time.time()
print("Bubblesort took", end - start, "seconds for {} elements".format(len(test)))

start = time.time()
selectionSort(test)
end = time.time()
print("Selectionsort took", end - start, "seconds for {} elements".format(len(test)))

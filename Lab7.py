# Search Algorithms
# Linear Search algorithm

# Q1a


from typing import Counter


def linearSearch(target, iList):
    """
    Returns the position of the target item if found, or -1 otherwise

    """
    position = -1
    i = 0
    while i < len(iList):

        if target == iList[i]:
            position = i + 1
            break
        i += 1
    return position


def linearSearchFor(target, iList):
    """
    Returns the position of the target item if found, or -1 otherwise

    """
    position = -1

    for index, element in enumerate(reversed(iList)):

        if target == element:
            position = len(iList) - index
            break

    return position


def binarySearch(target, iList):
    """
    This function expects sorted Lists
    """
    mpi = len(iList) // 2
    pivot = iList[mpi]
    if target == pivot:
        return pivot, mpi
    elif len(iList) <= 1:
        return -1
    elif target < pivot:
        iList = iList[0 : len(iList) // 2]
        return binarySearch(target, iList)
    elif target > pivot:
        iList = iList[len(iList) // 2 : len(iList)]
        return binarySearch(target, iList)
    else:
        return -1


def bubbleSort(iList):
    """
    This function makes a bubble sort
    """
    counter = 0
    n = len(iList)
    for i in range(n - 1):

        for x in range(n - i - 1):
            counter += 1
            if iList[x] > iList[x + 1]:
                iList[x], iList[x + 1] = iList[x + 1], iList[x]
    return iList, counter


def selectionSort(iList):
    n = len(iList)
    minindex = 0
    counter = 0
    for i in range(n - 1):
        minindex = i
        for j in range(i + 1, n):
            counter += 1
            if iList[minindex] > iList[j]:
                # min = iList[j]
                minindex = j

        iList[i], iList[minindex] = iList[minindex], iList[i]
    return iList, counter


def insertionSort(iList):
    n = len(iList)

    for i in range(2, n):

        for j in range(i, 0, -1):
            if iList[j] < iList[j - 1]:
                iList[j], iList[j - 1] = iList[j - 1], iList[j]

    return iList


def insertionSortwhile(iList):
    n = len(iList)

    for i in range(2, n):
        j = i - 1
        while j > 0 and iList[i] < iList[j]:
            iList[j], iList[j - 1] = iList[j - 1], iList[j]
            j = j - 1
    return iList


myList1 = [2, 3, 6, 7, 8, 9, 10, 1]
myList2 = [6, 7, 5, 3, 2, 10]
myList3 = [3, 2, 1]
myList4 = [7, 4, 3, 28, 12]
# myList.sort()
# print(linearSearch(2,myList))
# print(linearSearchFor(2,myList))
# r = binarySearch(7, myList)
# print(r)
# s = bubbleSort(myList3)
# print(s)
# t = selectionSort(myList4)
# print(t)

i = insertionSortwhile(myList2)
print(i)


# nList=myList[0:len(myList)//2]
# print(nList)


# print(myList[-1])

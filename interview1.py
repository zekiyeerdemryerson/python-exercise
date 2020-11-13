def isValidSubsequence(array, sequence):
    # Write your code here.
    idxa = 0
    idxs = 0

    while idxa < len(array) and idxs < len(sequence):
        if array[idxa] == sequence[idxs]:
            idxs += 1
        idxa += 1
    return idxs == len(sequence)


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
s1 = [5, 25, 23]
print(isValidSubsequence(array1, s1))

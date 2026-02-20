def rotateLeft(d, arr):
    for i in range(d):
        firstNum = arr.pop(0)
        arr.append(firstNum)
    return arr

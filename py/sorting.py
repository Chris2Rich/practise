def bubblesort(v: list, asc=True):
    swapped = True
    while swapped != False:
        swapped = False
        for i in range(len(v) - 1):
            if ((v[i] > v[i+1]) and asc) or ((v[i] < v[i+1]) and not asc):
                v[i], v[i+1], swapped = v[i+1], v[i], True
    return v

def mergesort(v: list, asc=True):
    if len(v) <= 1:
        return v
    left = []
    right = []

    for i in range(len(v)):
        if i < len(v) / 2:
            left.append(v[i])
        else:
            right.append(v[i])

    left = mergesort(left, asc)
    right = mergesort(right, asc)


    return merge(left, right)

def merge(left: list, right: list):
    result = []

    while left != [] and right != []:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    
    while left != []:
        result.append(left[0])
        left = left[1:]
    while right != []:
        result.append(right[0])
        right = right[1:]

    return result

print(mergesort([123,325325,1213,43,1,4,5,6,2,22]))
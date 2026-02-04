import random


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0
    ordered=False
    while not(ordered):
        ordered=True
        for i in range(0,len(items)-1):
            if items[i]>items[i+1]:
                temp=items[i]
                items[i]=items[i+1]
                items[i+1]=temp
                swaps+=1
                comparisons += 1
                ordered=False
            else:
                comparisons+=1
    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    for i in range(1, len(items)):
        target=items[i]
        n=i-1

        while n>=0 and items[n]>target:
            comparisons+=1
            items[n+1]=items[n]
            swaps+=1
            n-= 1

        if n>= 0:
            comparisons += 1
        items[n+1] =target
    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0

    n=len(items)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]
        swaps += 1

    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))

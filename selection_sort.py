def selection_sort(arr):
    for ii in range(len(arr)):
        min_val = ii

        for item in range((ii + 1), len(arr)):
            if arr[item] < arr[min_val]:
                min_val = item
        arr[ii], arr[min_val] = arr[min_val], arr[ii]


array = []
numbers = int(input('enter numbers of elements: '))
for x in range(numbers):
    data = int(input())
    array.append(data)
    print(array)

selection_sort(array)
print('sorted array is : ', array)

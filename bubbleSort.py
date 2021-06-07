def bubble_sort(array):
    for iteration in range(len(array)):
        for index in range(len(array) - 1 - iteration):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                print(array)


arr = []
numbers = int(input('enter number of elements: '))
for i in range(numbers):
    data = int(input())
    arr.append(data)
bubble_sort(arr)

print('resulted array is ', arr)

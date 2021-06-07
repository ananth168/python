def binarySearch(my_array, target):
    left = 0
    right = len(my_array) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = my_array[mid]

        if target == mid_element:
            print('element is at : ', mid)
            return mid_element

        elif target > mid_element:
            left = mid + 1


        else:
            right = mid - 1

    print('not found')
    return


array = []
numbers = int(input('enter number of elements: '))
for i in range(numbers):
    data = int(input())
    array.append(data)
    array.sort()

print(array)

key = int(input('enter any digit: '))

print(binarySearch(array, key))

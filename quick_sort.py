def quickSort(my_array):
    qsHelper(my_array, 0, len(my_array) - 1)
    return my_array


def qsHelper(my_array, start, end):
    if start >= end:
        return

    pivot = start
    left = pivot + 1
    right = len(my_array) - 1

    while right >= left:
        if my_array[left] > my_array[pivot] and my_array[right] < my_array[pivot]:
            my_array[left], my_array[right] = my_array[right], my_array[left]

        if my_array[left] <= my_array[pivot]:
            left += 1

        if my_array[right] >= my_array[pivot]:
            right -= 1
    print('\nsteps :', my_array)

    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    qsHelper(my_array, start, right - 1)
    qsHelper(my_array, right + 1, end)


my_arr = []
number = int(input('enter number of elements: '))
for i in range(number):
    data = int(input())
    my_arr.append(data)
    print(my_arr)

quickSort(my_arr)
print('\nsorted array is : ', my_arr)

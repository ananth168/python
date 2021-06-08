def insertion_sort(array):
    for ii in range(1, len(array)):
        key = array[ii]
        last = ii - 1

        while last >= 0 and key < array[last]:
            array[last + 1] = array[last]
            last = last - 1
        array[last + 1] = key


number = []
num = int(input('enter no. of elements :'))
for i in range(num):
    data = int(input())
    number.append(data)
    print('unsorted array is : ', number)

insertion_sort(number)
print('\nSORTED ARRAY  IS : ', number)

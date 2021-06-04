def search(arr, key):  # this function searches for a given key in a input array

    for ii in range(len(arr)):

        if arr[ii] == key:
            print("found at ", ii)
            return

    print("not found")


a = [7, 3, 5, 1, 8]
k = (int(input("enter any number  ")))

print(search(a, k))


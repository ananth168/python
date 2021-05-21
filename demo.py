def search(arr, key):  #this function searches for a given key in a input array

    for ii in range(len(arr)):

        if arr[ii] == key:
            print ("found at ", ii)
            return

    print("not found")

arr = [7, 3, 5, 1, 8]
key = (int(input("enter any number  ")))

result = search(arr,key)
print(result)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


array = []
n = int(input("Number of Elements:"))

for i in range(0, n):
    ele = int(input("Enter the element:"))
    array.append(ele)
print(array)
print("Sorted array is")
print(insertionSort(array))

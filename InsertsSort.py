def findSmallest(arr):
    min = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    copy_arr = list(arr)
    for i in range(len(arr)):
        smallest = findSmallest(copy_arr)
        new_arr.append(copy_arr.pop(smallest))
    return  new_arr

if __name__ == "__main__":
    print(selection_sort([5,3,6,2,10]))
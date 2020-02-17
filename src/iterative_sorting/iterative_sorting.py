# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 +) 
        indexSmallest = arr.index(min(arr[i:]))
        
        # TO-DO: swap
        if indexSmallest > smallest_index:
            arr[indexSmallest], arr[smallest_index] = arr[smallest_index], arr[indexSmallest]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for (index, value) in enumerate(arr):
        while arr[index] > arr[index + 1]:
            print(index, 1)
            if arr[index] > arr[index + 1]:
                print(index, 2)
                for i in range(0, len(arr) - 1):
                    cur_index = i

                    if arr[cur_index] > arr[cur_index + 1]:
                        #print(index, value)
                        #print(arr[cur_index], arr[cur_index + 1], 'b')
                        arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index]
                        #print(arr[cur_index], arr[cur_index + 1], 'a')

    print(arr)
    return arr

selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
#bubble_sort([1, 5, 4, 2, 6, 0, 3, 7, 8, 9])

#bubble_sort([1, 4, 2, 5, 6, 0, 3, 7, 8, 9])

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
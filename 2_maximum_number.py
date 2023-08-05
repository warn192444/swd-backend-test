
arr = [1, 2, 1, 3, 5, 6, 4]

def find_index_maximum_number(arr):
    max = 0
    for i in range(len(arr)):
        if(arr[i] > max):
            max = i
            index = i
    return index

print(find_index_maximum_number(arr))
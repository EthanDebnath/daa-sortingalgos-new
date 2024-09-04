#Ethan Debnath

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        #Initialize the min index for the current position
        min_index = i
        
        #Find the index of the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        #Now Swap minimum element with the first element of the unsorted portion
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    arr = [23, 124, 535, 1243, 663, 13, 0]
    selection_sort(arr)
    print("Sorted array:", arr)

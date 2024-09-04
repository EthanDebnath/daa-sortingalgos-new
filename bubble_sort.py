#Ethan Debnath

def bubble_sort(arr):
    """Sorts an array in ascending order using the bubble sort algorithm."""
    n = len(arr)  # Length of the array
    
    #Perform passes over the entire array
    for pass_num in range(n - 1, 0, -1):
        swapped = False  #Flag for whether any swaps have occurred in this pass
        
        #Compare each pair of adjacent elements
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                #Swap if elements are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  #A swap occurred, so array may not be sorted
        
        #If no swaps occurred in this pass...then means array is sorted
        if not swapped:
            break

    return arr  #Return sorted array!

if __name__ == "__main__":
    arr = [23, 124, 535, 1243, 663, 13, 0]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
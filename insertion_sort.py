#Ethan Debnath

def insertion_sort(array):
    """Sorts an array in ascending order using the insertion sort algorithm."""
    
    #Iterate over array from the second element to the end
    for i in range(1, len(array)):
        key = array[i]  #Element to be positioned, calling it key
        j = i - 1  #Comparing with the previous element
        
        # Shift elements in the sorted portion of the array forward if they are greater than key
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  #Move the element one to the right
            j -= 1  #Move to the previous element
        
        #Insert the key in its correct position
        array[j + 1] = key

if __name__ == "__main__":
    arr = [5, 4, 2, 9, 3, 2]
    insertion_sort(arr)
    print(arr)

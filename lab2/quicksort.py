# CS 345
# Quicksort python implimentation
# Aleksandr Sergeev

import sys
import timeit

def partition(array, low, high):
    # Declare pivot, ending index of array
    pivot = array[high]
    # Lowest element
    i = low - 1

    # Loop through array and sort
    for j in range(low, high):
        # If lowest less than or equal to pivot, swap
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]


    # Insert pivot into correct position, return index
    array[i+1], array[high] = array[high], array[i+1]
    return(i+1)


def quicksort(array, low, high):
    if (low < high):
        # Partition array
        x = partition(array, low, high)

        # Recursive call on quicksort
        quicksort(array, low, x - 1)
        quicksort(array, x + 1, high)


def main(file):
    myArray = []

    # Try open file, catch path error
    try:
        fh = open(file, "r")
    except IOError:
        print("Incorrect file path given.")
        sys.exit()

    # Read ints to Array, close file
    lines = fh.readlines()
    if "int" in file:
        for line in lines:
            line.rstrip()
            myArray.append(int(line))
    elif "float" in file:
        for line in lines:
            line.rstrip()
            myArray.append(float(line))
    fh.close()

    # Call quicksort on array
    start = timeit.default_timer()
    quicksort(myArray, 0, len(myArray) - 1)
    stop = timeit.default_timer()
    time_sec = stop - start
    print(time_sec)
    return time_sec, myArray



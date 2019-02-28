# CS 345
# Quicksort python implimentation
# Aleksandr Sergeev

import sys
import timeit


# Recursion limit raised for pathological file sorting
# Can now sort path files up to 10,000
sys.setrecursionlimit(10100)

def partition(array, low, high):
    # Declare pivot, ending index of array
    pivot = array[high]
    # Lowest element index
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
    my_array = []

    # Try open file, catch path error
    try:
        fh = open(file, "r")
    except IOError:
        print("Incorrect file path given.")
        sys.exit()

    # Read numbers to Array, close file
    # Check file type being opened to correctly convert string to int or float
    lines = fh.readlines()
    for line in lines:
        line.rstrip()
        if "int" in file:
            my_array.append(int(line))
        elif "float" in file:
            my_array.append(float(line))
    fh.close()

    # Call quicksort on array and time
    start = timeit.default_timer()
    quicksort(my_array, 0, len(my_array) - 1)
    stop = timeit.default_timer()
    time_sec = stop - start

    # Let user know quicksort is complete, return timing & sorted array
    print("File " + file + " completed.")
    return time_sec, my_array



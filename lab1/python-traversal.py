# cs345 - Lab 1
#
# Python array traversal
#
# Aleksandr Sergeev

import sys
import timeit
import numpy as np

dimension = int(sys.argv[1])

def main():
    
    myArray = [['e' for i in range(dimension)] for j in range(dimension)]

    start = timeit.default_timer()
#   Row major traversal list
    for i in range(dimension):
        for j in range(dimension):
            myArray[i][j] = 'r'
    stop = timeit.default_timer()
    print('List row major traversal time: ', stop - start)


    start = timeit.default_timer()
#   Column major traversal list
    for i in range(dimension):
        for j in range(dimension):
            myArray[j][i] = 'c'
    stop = timeit.default_timer()
    print('List column major traversal time: ', stop - start)


    ndArray = np.ones((dimension, dimension), dtype = np.int8)

    start = timeit.default_timer()
#   Row major traversal np
    for i in range(dimension):
        for j in range(dimension):
            ndArray[i][j] = 2
    stop = timeit.default_timer()
    print('ndArray row major traversal time: ', stop - start)

    start = timeit.default_timer()
#   Column major traversal np
    for i in range(dimension):
        for j in range(dimension):
            ndArray[j][i] = 3
    stop = timeit.default_timer()
    print('ndArray column major traversal time: ', stop - start)


main()

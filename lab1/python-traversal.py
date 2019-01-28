# cs345 - Lab 1
#
# Python array traversal
#
# Aleksandr Sergeev

import sys

dimension = int(sys.argv[1])

def main():
    
    myArray = [['e' for i in range(dimension)] for j in range(dimension)]

#   Row major traversal
    for i in range(dimension):
        for j in range(dimension):


#   Column major traversal

main()

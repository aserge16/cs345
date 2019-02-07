# CS345 Software Engineering
# Lab 2 Int File Generators
# Aleksandr Sergeev


import random


# Worst case ordered array generation, input size as str
def pathological(size):
    # Define file name and open
    fileName = "ints-" + size + ".dat"
    fh = open(fileName, "w+")

    # Generate numbers and write
    for i in range(int(size) - 1, -1, -1):
        fh.write(str(i) + "\n")

    # Close file
    fh.close()

    return fileName


# Randomized ints written to file
def randomFile(size):
    # Define file name and open
    fileName = "ints-" + size + ".dat"
    fh = open(fileName, "w+")

    # Generate numbers and write
    for i in range( int(size) ):
        j = random.randint( 1, int(size) )
        fh.write(str(j) + "\n")

    # Close file
    fh.close()

    return fileName

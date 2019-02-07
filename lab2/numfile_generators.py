# CS345 Software Engineering
# Lab 2 Int File Generators
# Aleksandr Sergeev


import random


# Worst case ordered array generation, input size as str
def pathological(size):
    # Define file name and open
    fileName = "ints-" + str(size) + "path.dat"
    fh = open(fileName, "w+")

    # Generate numbers and write
    for i in range(size - 1, -1, -1):
        fh.write(str(i) + "\n")

    # Close file
    fh.close()

    return fileName


# Randomized ints written to file
def randomFile(size):
    # Define file name and open
    fileName = "ints-" + str(size) + "-random.dat"
    fh = open(fileName, "w+")

    # Generate numbers and write
    for i in range(size):
        j = random.randint( 1, size)
        fh.write(str(j) + "\n")

    # Close file
    fh.close()

    return fileName

# CS345 Software Engineering
# Lab 2 Int File Generators
# Aleksandr Sergeev


import random


# Worst case ordered array generation, input size as str
# Reverse order, ie. array initialized from 999 to 0.
def pathological(size):
    # Define file name and open
    file_name = "ints-" + str(size) + "path.dat"
    fh = open(file_name, "w+")

    # Generate numbers and write
    for i in range(size - 1, -1, -1):
        fh.write(str(i) + "\n")

    # Close file
    fh.close()

    return file_name


# Randomized ints written to file
def random_file(size):
    # Define file name and open
    file_name = "ints-" + str(size) + "-random.dat"
    fh = open(file_name, "w+")

    # Generate numbers and write
    for i in range(size):
        j = random.randint( 1, size)
        fh.write(str(j) + "\n")

    # Close file
    fh.close()

    return file_name

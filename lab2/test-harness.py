from quicksort import *
import datetime
import os


# Function running in O(n) checking if array is sorted
def arraySortTest(array):
    return all(array[i] <= array[i+1] for i in xrange(len(array)-1))


def testHarness(file):
    #Get result array, time
    time, array = main(file)

    # Open log file, if not present it will create new one
    fh = open("log-file.dat","a")

    # Get results and convert to strings for writing to file
    dayTime = str(datetime.datetime.now())
    outcome = str(arraySortTest(array))
    time = str(time)

    # Write results to log file
    fh.write("Test conducted at: " + dayTime + "\n", )
    fh.write("Array sorted correctly: " + outcome + "\n", )
    fh.write("Conducted on file " + file + "\n")
    fh.write("Ran in " + time + " seconds \n")
    fh.write("\n\n")

    # Close log file
    fh.close()


def run():
    # List of all possible file names
    files = ["ints-1.dat", "ints-10k.dat", "ints-100k.dat", "ints-1m.dat", "ints-10m.dat", "floats-1m.dat", "floats-10m.dat"]
    
    # Get user input on which files to run
    print("Please enter a number corresponding to desired file:\n 1 = ints-1.dat \n 2 = ints-10k.dat \n 3 = ints-100k.dat\n 4 = ints-1m.dat\n 5 = ints-10m.dat\n 6 = floats-1m.dat\n 7 = floats-10m.dat\n 8 = All int files\n 9 = All float files")
    files_to_run = int(input())
    
    # Run files based on index of filenames list
    if (0 < files_to_run < 10):
        if files_to_run == 8:
            for i in range(0, 5):
                testHarness(files[i])
        elif files_to_run == 9:
            for i in range(5, 7):
                testHarness(files[i])
        else:
            testHarness(files[files_to_run - 1])
    else:
        print ("You did not enter a valid arguement.")


if __name__ == "__main__":
    run()




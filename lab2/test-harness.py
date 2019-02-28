# CS345 Software Engineering
# Lab 2 Test Harness
# Aleksandr Sergeev


from numfile_generators import *
import quicksort
import datetime
import os


# Function running in O(n) returning boolean if array is sorted or not
# Checks each element through the array is greater or equal to previous element
def arraySortTest(array):
    return all(array[i] <= array[i+1] for i in xrange(len(array)-1))


def testHarness(file):
    #Get result array, time
    time, array = quicksort.main(file)

    # Get results and convert to strings for writing to file
    dayTime = str(datetime.datetime.now())
    outcome = str(arraySortTest(array))
    time = str(time)

    # Open log file, if not present it will create new one
    fh = open("log-file.dat","a")
    
    # Write results to log file
    fh.write("Test conducted at: " + dayTime + "\n", )
    fh.write("Array sorted correctly: " + outcome + "\n", )
    fh.write("Conducted on file " + file + "\n")
    fh.write("Ran in " + time + " seconds \n")
    fh.write("\n\n")

    # Close log file
    fh.close()

    print("Results sent to log-file.dat")


def run():
    # List of all possible file names
    files = ["ints-1.dat", "ints-10k.dat", "ints-100k.dat", "ints-1m.dat", "ints-10m.dat", "floats-1m.dat", "floats-10m.dat"]
    
    # Get user input on which files to run
    print("Please enter a number corresponding to desired file:\n 1 = ints-1.dat \n 2 = ints-10k.dat \n 3 = ints-100k.dat\n 4 = ints-1m.dat\n 5 = ints-10m.dat\n 6 = floats-1m.dat\n 7 = floats-10m.dat\n 8 = All int files\n 9 = All float files\n 10 = Pathologically ordered int file\n 11 = Randomly generated int file")
    filesToRun = int(input())
    
    # Run files based on index of file_names list
    if (0 < filesToRun < 12):
        if filesToRun == 8:
            for i in range(0, 5):
                testHarness(files[i])
        elif filesToRun == 9:
            for i in range(5, 7):
                testHarness(files[i])
        elif (filesToRun == 10 or filesToRun == 11):
            print("Please enter amount of integers to be generated:\n")
            try:
                amount = input()
                if filesToRun == 10:
                    file_name = pathological(amount)
                    testHarness(file_name)
                else:
                    file_name = random_file(amount)
                    testHarness(file_name)
            except ValueError:
                print("Please enter an integer.")
                return
        else:
            testHarness(files[filesToRun - 1])
    else:
        print ("You did not enter a valid arguement.")


if __name__ == "__main__":
    run()




# CS345 Software Engineering
# Lab 2 Test Harness
# Aleksandr Sergeev


from numfile_generators import *
import quicksort
import datetime
import os


# Function running in O(n) returning boolean if array is sorted or not
# Checks each element through the array is greater or equal to previous element
def array_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))


def test_harness(file):
    #Get result array, time from quicksort main()
    time, array = quicksort.main(file)

    # Get results and convert to strings for writing to file
    day_time = str(datetime.datetime.now())
    outcome = str(array_sorted(array))
    time = str(time)

    # Open log file, if not present it will create new one
    fh = open("log-file.dat","a")
    
    # Write results to log file
    fh.write("Test conducted at: " + day_time + "\n", )
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
    print("Please enter a number corresponding to desired file:"
            "\n 1 = ints-1.dat" 
            "\n 2 = ints-10k.dat" 
            "\n 3 = ints-100k.dat"
            "\n 4 = ints-1m.dat"
            "\n 5 = ints-10m.dat"
            "\n 6 = floats-1m.dat"
            "\n 7 = floats-10m.dat"
            "\n 8 = All int files"
            "\n 9 = All float files"
            "\n 10 = Pathologically ordered int file"
            "\n 11 = Randomly generated int file")
    files_to_run = int(input())
    
    # Run files based on index of file_names list
    if (0 < files_to_run < 12):
        if files_to_run == 8:
            for i in range(0, 5):
                test_harness(files[i])
        elif files_to_run == 9:
            for i in range(5, 7):
                test_harness(files[i])
        elif (files_to_run == 10 or files_to_run == 11):
            print("Please enter amount of integers to be generated:\n")
            try:
                amount = input()
                if files_to_run == 10:
                    file_name = pathological(amount)
                    test_harness(file_name)
                else:
                    file_name = random_file(amount)
                    test_harness(file_name)
            except ValueError:
                print("Please enter an integer.")
                return
        else:
            test_harness(files[files_to_run - 1])
    else:
        print("You did not enter a valid arguement.")

    print("Would you like to run the program again?\n 0 = No | 1 = Yes")
    answer = input()
    if answer == 1:
        run()
    else:
        return 0
        

if __name__ == "__main__":
    run()

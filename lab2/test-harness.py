from quicksort import *

def run():
    # List of all possible file names
    files = ["ints-1.dat", "ints-10k.dat", "ints-100k.dat", "ints-1m.dat", "ints-10m.dat", "floats-1m.dat", "floats-10m.dat"]
    
    # Get user input on which files to run
    print("Please enter a number corresponding to desired file:\n 1 = ints-1.dat \n 2 = ints-10k.dat \n 3 = ints-100k.dat\n 4 = ints-1m.dat\n 5 = ints-10m.dat\n 6 = floats-1m.dat\n 7 = floats-10m.dat\n 8 = All int files\n 9 = All float files")
    files_to_run = int(input())
    
    # Run files based on index
    if (0 < files_to_run < 10):
        if files_to_run == 8:
            for i in range(0, 6):
                main(files[i])
        elif files_to_run == 9:
            for i in range(7, 9):
                main(files[i])
        else:
            main(files[files_to_run - 1])
    else:
        print ("You did not enter a valid arguement.")



if __name__ == "__main__":
    run()




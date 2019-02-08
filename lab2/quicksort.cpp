/* Aleksandr Sergeev
01/31/2019

CS-345 Lab2
Quicksort Implimentation */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

/* Swap function */
void swap(int* a, int* b)
{
    int t=*a;
    *a=*b;
    *b=t;
}

/* Partition function implimentation */
int partition(int array[], int low, int high) {
    /* Declare Pivot, at ending index of array */
    int pivot = array[high];
    /* Lowest element to begin comparison */
    int i = low - 1;

    /* Loop through array and pivot swap */
    for ( int j = low; j < high; j++) {
        // If lowest less than or equal to pivot, swap */
        if (array[j] <= pivot) {
            i++ ;
            swap(&array[i], &array[j]) ;
        }
    }

    /* Insert pivot into correct position, return index */
    swap(&array[i+1], &array[high]) ;
    return (i + 1) ;
}


/* Quicksort function implimentation */
void quicksort(int array[], int low, int high) {
    if (low < high) {
        /* Partition array */
        int x = partition(array, low, high) ;

        /* Recursive call on quicksort */
        quicksort(array, low, x - 1) ;
        quicksort(array, x + 1, high) ;
    }
}


int main(int argc, char *argv[]) {
    /* Check for bash file input */
    if (argc != 3) {
        cout << "Incorrect bash input. Please run the code followed by the name of file.\n" ;
        exit(1) ;
    }
    else {
        ifstream int_File(argv[1]) ;
        /* Check if file can be opened */
        if ( !int_File.is_open() ) {
            cout << "Could not open int file.\n" ;
        }
        else {
            /* Count number of lines in file for static array decleration */
            /* Size is taken from user input in bash */
            int size = atoi(argv[2]) ;
            int x, y = 0 ;
            int array[size] ;

            while (int_File >> x) {
                array[y] = x ;
                y++ ;
            }
            int_File.close() ;
            /* Call quicksort */
            quicksort(array, 0, size - 1) ;
            }
        }
    }
}

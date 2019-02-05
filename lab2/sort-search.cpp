/* Aleksandr Sergeev
01/31/2019

CS-345 Lab2
Quicksort Implimentation */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


/* Partition function implimentation */
int partition(vector<int> array, int low, int high) {
    /* Declare Pivot, at ending index of array */
    int pivot = array[high];
    /* Lowest element to begin comparison */
    int i = low;

    /* Loop through array and pivot swap */
    for ( int j = low + 1; j < high; j++) {
        // If lowest less than or equal to pivot, swap */
        if (array[j] <= pivot) {
            i++ ;
            iter_swap(array.begin() + i, array.begin() + j) ;
        }
    }

    /* Insert pivot into correct position, return index */
    iter_swap(array.begin() + i + 1, array.begin() + high) ;
    return (i + 1) ;
}


/* Quicksort function implimentation */
void quicksort(vector<int> array, int low, int high) {
    if (low < high) {
        /* Partition array */
        int x = partition(array, low, high) ;

        /* Recursive call on quicksort */
        quicksort(array, low, x - 1) ;
        quicksort(array, x + 1, high) ;
    }
    for (int x = 0; x < array.size(); x++) {
        cout << array[x] ;
        cout << "\n" ;
    }
    cout << "\n\n" ;
}


int main(int argc, char *argv[]) {
    vector<int> vector_Array ;
    int x, vec_size ;

    /* Check for bash file input */
    if (argc != 2) {
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
            while ( int_File >> x) {
                vector_Array.push_back(x) ;
            }
            vec_size = vector_Array.size() ;
            int_File.close() ;
            /* Call quicksort */
            quicksort(vector_Array, 0, vec_size - 1) ;
            for (int x = 0; x < vec_size; x++) {
                cout << vector_Array[x] ;
                cout << "\n" ;
            }
        }
    }
}

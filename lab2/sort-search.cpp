/* Aleksandr Sergeev
01/31/2019

CS-345 Lab2
Quicksort Implimentation */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


/* Partition function implimentation */
int partition(int array[], int low, int high) {
    return 0 ;
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
            quicksort(vector_Array, 1, vec_size)
        }
    }
}

/* Aleksandr Sergeev
01/31/2019

CS-345 Lab2
Quicksort Implimentation */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    vector<int> vector_Array ;
    int x, vec_size ;

    /* Check for bash file input */
    if (argc != 2) {
        cout << "Incorrect bash input.\n" ;
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
        }

    }
}

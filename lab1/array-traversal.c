/* CS320 Software Engineering
 * Lab 1
 * Aleksandr Sergeev
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

    int i, j, k;
    /* Get dimension size of array from argv */
    int dimension = atoi(argv[1]);
    /* Define array local to function */
    char myArray[dimension][dimension];

    /* Row major traversal */
    for (i = 0; i < sizeof(myArray); i++) {
        for (j = 0; j < dimension; j++) {
            for (k = 0; k < dimension; k++) {
                myArray[j][k] = 'r';
            }
        }
    }

    /* Column major traversal */
    for (i = 0; i < sizeof(myArray); i++) {
        for (j = 0; j < dimension; j++) {
            for (k = 0; k < dimension; k++) {
                myArray[k][j] = 'c';
            }
        }
    }

    return 0;
}

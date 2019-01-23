/* CS320 Software Engineering
 * Lab 1
 * Aleksandr Sergeev
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

    /* Get dimension size of array from argv */
    int size = atoi(argv[1]);
    /* Define array local to function */
    char myArray[size][size];

    printf("%d \n", size);
    return 0;
}

/* CS345 Software Engineering
 * Lab 1
 * Aleksandr Sergeev
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


int main(int argc, char* argv[]) {

    int i, j;
    float total_time;
    struct timeval start, end;
    /* Get dimension size of array from argv */
    int dimension = atoi(argv[1]);
    /* Define array local to function */
    char myArray[dimension][dimension];

    /* Row major traversal */
    for (i = 0; i < dimension; i++) {
        for (j = 0; j < dimension; j++) {
                gettimeofday(&start, NULL);
                myArray[i][j] = 'r';
                gettimeofday(&end, NULL);
                total_time += end.tv_sec - start.tv_sec + (end.tv_usec - start.tv_usec)*0.000001;
        }
    }

    /*  Print to stdout row traversal time */
    printf("Row traversal total time was %f seconds.\n", total_time);


    /* Column major traversal */
    for (i = 0; i < dimension; i++) {
        for (j = 0; j < dimension; j++) {
                gettimeofday(&start, NULL);
                myArray[j][i] = 'c';
                gettimeofday(&end, NULL);
                total_time += end.tv_sec - start.tv_sec + (end.tv_usec - start.tv_usec)*0.000001;
        }
    }

    /* Compute and print to stdout column traversal time */
    printf("Column traversal total time was %f seconds.\n", total_time);

    return 0;
}

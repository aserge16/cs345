/* CS345 Software Engineering
 * Lab 1
 * Aleksandr Sergeev
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char* argv[]) {



    int i, j;
    float total_time;
    struct timeval start, end;
    /* Get dimension size of array from argv */
    int dimension = atoi(argv[1]);

    /* Get host name, set max array size*/
    int gethostname(char *name, size_t len);
    char host[64];
    gethostname(host, sizeof host);
    if (strcmp(host, "tools") == 0 || strcmp(host, "goldwasser") == 0) {
        if (dimension > 2890) {
            dimension = 2890;
        }
    }
    else if (strcmp(host, "hopper") == 0) {
        if (dimension > 3235) {
            dimension = 3235;
        }
    }

    /* Define array local to function */
    char myArray[dimension][dimension];

    gettimeofday(&start, NULL);
    /* Row major traversal */
    for (i = 0; i < dimension; i++) {
        for (j = 0; j < dimension; j++) {
                myArray[i][j] = 'r';
        }
    }
    gettimeofday(&end, NULL);

    /* Compute and print to stdout row traversal time */
    total_time = end.tv_sec - start.tv_sec + (end.tv_usec - start.tv_usec)*0.000001;
    printf("Row traversal total time was %f seconds.\n", total_time);


    gettimeofday(&start, NULL);
    /* Column major traversal */
    for (i = 0; i < dimension; i++) {
        for (j = 0; j < dimension; j++) {
                myArray[j][i] = 'c';
        }
    }
    gettimeofday(&end, NULL);

    /* Compute and print to stdout column traversal time */
    total_time = end.tv_sec - start.tv_sec + (end.tv_usec - start.tv_usec)*0.000001;
    printf("Column traversal total time was %f seconds.\n", total_time);

    return 0;
}

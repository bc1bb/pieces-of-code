#include <stdio.h>
#include <string.h>

double pi() {
    return 3.14159265;
}

int one() {
    return 1;
}

int main(int argc, char *argv[]) {
    printf("How did you call this program: %s\n", argv[0]);
    // argv[0] = 0th argument of the calling command

    if (argc >= 2) {
        printf("First argument: %s\n", argv[1]);
        // argv[1] = first argument
        if (argc >= 3) {
            printf("Second argument: %s\n", argv[2]);
            // argv[2] = second argument
        }
    }
    // let's just show args because why not lol

    printf("Command result: ");
    if (strcmp(argv[0], "pi") == 0 || strcmp(argv[0], "./pi") == 0) {
        printf("%f\n", pi());
    } else if (strcmp(argv[0], "one") == 0 || strcmp(argv[0], "./one") == 0) {
        printf("%d\n", one());
    } else {
        printf("%s is unknown\n", argv[0]);
    }
    // here we just give function results using 0th argument

    return 0;
}


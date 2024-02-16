#include <stdio.h>

// Function prototype
int recursiveSearch(int arr[], int l, int r, int x);

int main() {
    int arr[] = {33, 47, 12, 98, 59, 23, 77, 85, 66, 5, 39, 71, 88, 16, 45};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 23; // Value to search for
    int result = recursiveSearch(arr, 0, n - 1, x);

    if (result != -1)
        printf("Element %d is present at index %d.\n", x, result);
    else
        printf("Element %d is not present in the array.\n", x);

    return 0;
}

int recursiveSearch(int arr[], int l, int r, int x) {
    // Your implementation goes here
}


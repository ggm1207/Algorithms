#include <stdio.h>
#define MAX(X, Y) ((X) > (Y) ? (X) : (Y))

int main()
{
    int arr[3];
    int i, result, a = 0;
    for (i = 0; i < 3; i++)
        scanf("%d", &arr[i]);

    result = MAX(arr[1] - arr[0], arr[2] - arr[1]);

    printf("%d", result - 1);
    return 0;
}

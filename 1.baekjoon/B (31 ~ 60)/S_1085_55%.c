#include <stdio.h>

int main()
{
    int x = 0, y = 0, w = 0, h = 0;
    int result1 = 0, result2 = 0;

    scanf("%d", &x);
    scanf("%d", &y);
    scanf("%d", &w);
    scanf("%d", &h);

    if (x > w / 2)
        result1 = w - x;
    else
        result1 = x;
    if (y > h / 2)
        result2 = h - y;
    else
        result2 = y;

    if (result1 > result2)
        printf("%d\n", result2);
    else
        printf("%d\n", result1);

    return 0;
}
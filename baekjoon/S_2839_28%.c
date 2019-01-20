#include <stdio.h>
int main()
{
    int i = 0, j = 0;
    int a = 0, b = -1;
    scanf("%d", &a);

    if (a == 4 || a == 7)
        printf("%d", b);

    for (i = 0; i < 10; i++)
    {
        for (j = 0;; j++)
        {
            if (3 * i + 5 * j > a)
                break;
            if (a == 3 * i + 5 * j)
            {
                printf("%d\n", i + j);
                return 0;
            }
        }
    }
}
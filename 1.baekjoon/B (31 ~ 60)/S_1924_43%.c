#include <stdio.h>

int main()
{
    int a = 0, b = 0, c = 0;
    int i = 0;
    scanf("%d %d", &a, &b);

    for (i = 2; i < a + 1; i++)
    {
        if (i == 5 || i == 7 || i == 10 || i == 12)
        {
            c += 30;
        }
        else if (i == 3)
        {
            c += 28;
        }
        else
        {
            c += 31;
        }
    }

    c += b;

    switch (c % 7)
    {
    case 0:
        printf("SUN");
        break;
    case 1:
        printf("MON");
        break;
    case 2:
        printf("TUE");
        break;
    case 3:
        printf("WED");
        break;
    case 4:
        printf("THU");
        break;
    case 5:
        printf("FRI");
        break;
    default:
        printf("SAT");
        break;
    }
}
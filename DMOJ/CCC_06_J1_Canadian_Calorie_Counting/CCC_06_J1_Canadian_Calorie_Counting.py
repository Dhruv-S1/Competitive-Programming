#include <stdio.h>
#include <stdlib.h>

int main()
{
    int food1 = 0;
    int food2 = 0;
    int food3 = 0;
    int food4 = 0;
    int tot = 0;
    scanf("%d", &food1);
    if (food1 == 1)
    {
    tot = tot+461;
    }
    if (food1 == 2)
    {
    tot = tot+431;
    }
    if (food1 == 3)
    {
    tot = tot+420;
    }
    scanf("%d", &food2);
    if (food2 == 1)
    {
        tot = tot+100;
    }
    if (food2 == 2)
    {
        tot = tot+57;
    }
    if (food2 == 3)
    {
        tot = tot + 70;
    }

    scanf("%d", &food3);
    if (food3 == 1)
    {
        tot = tot+130;
    }
    if (food3 == 2)
    {
        tot = tot+160;
    }
    if (food3 == 3)
    {
        tot = tot + 118;
    }
    scanf("%d", &food4);
    if (food4 == 1)
    {
        tot = tot+ 167;
    }
    if (food4 == 2)
    {
        tot = tot + 266;
    }
    if (food4 == 3)
    {
        tot = tot + 75;
    }
    printf("Your total Calorie count is %d.", tot);

}

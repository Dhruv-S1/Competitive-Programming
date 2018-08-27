#include <bits/stdc++.h>
#include<math.h>
#include<cmath>
using namespace std;
int a[501][501];
int under[501][501];
int over[501][501];
int r, c, up, right, hold1, hold2, hold3;
long long g, smallest;
int main()
{
    for(int i = 1; i<501; i++)
    {
        for(int j = 1; j<501; j++)
        {
        a[i][j] = 999;
        over[i][j] = 999;
        under[i][j] = 999;
        }
    }
    cin>>r>>c;
    for(int i = 1; i<r+1; i++)
    {
        for(int j = 1; j<c+1;j++)
        {
            char hold;
            scanf(" %c", &hold);
            if(hold == 'x')
            {
                for(int k = 1; k<r+1;k++)
                {
                    if(i-k>0) over[k][j] = min(i-k, over[k][j]);
                    else if(i-k<0) under[k][j] = min(k-i, under[k][j]);
                    else
                    {
                        over[k][j] = 0;
                        under[k][j] = 0;
                    }
                }
            }
        }
    }

    scanf("%d", &g);
    for(long long i = 0; i<g; i++)
    {
        scanf("%d%d", &hold1, &hold2);

        smallest = 9999999;
        for(int k = 1; k<c+1;k++)
        {
            hold3 = (pow(abs(k-hold2),2))+(pow(min(under[hold1][k],over[hold1][k]), 2));
            if (smallest>hold3) smallest = hold3;
        }

        printf("%d\n", smallest);
        for(int k = 1; k<r+1; k++)
        {
            if(hold1-k>0) over[k][hold2] = min(hold1-k, over[k][hold2]);
            else if(hold1-k<0) under[k][hold2] = min(k-hold1, under[k][hold2]);
            else
            {
                over[k][hold2] = 0;
                under[k][hold2] = 0;
            }
        }
    }

}

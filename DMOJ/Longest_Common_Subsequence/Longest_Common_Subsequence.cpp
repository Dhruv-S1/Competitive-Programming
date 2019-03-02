#include <bits/stdc++.h>
using namespace std;
int a[1001][1001];
int str1[1001];
int str2[1001];
int n, m;
int main()
{
    scanf("%d %d", &n, &m);
    for(int i =0; i<n;i++)
    {
        scanf("%d", &str1[i]);
    }
    for(int i =0; i<m;i++)
    {
        scanf("%d", &str2[i]);
    }
    for(int i =1;i<n+1;i++)
    {
        for(int j =1; j<m+1; j++)
        {
            if(str1[i-1] ==str2[j-1]) a[i][j] = a[i-1][j-1]+1;
            else a[i][j] = max(a[i-1][j], a[i][j-1]);
        }
    }
    printf("%d", a[n][m]);
}

#include <iostream>

using namespace std;
long long x = 0;
char a[2001][2001];
long long vals[2001][2001];
char hold1;
long long total;
int main()
{
    cin>>x;
    for(int i = 1; i<x+1; i++)
    {
        for(int j = 1; j<x+1; j++)
        {
            cin>>hold1;
            a[i][j] = hold1;
        }
    }
    for(int i = 1; i<=x; i++)
    {
        for(int j = 0; j<=x; j++)
        {
            if(a[i][j] == '#') vals[i][j] = 1;
        }
    }
    for(int i = x; i>0;i--)
    {
        for(int j = x; j>0; j--)
        {
            if(a[i][j] == '#'&& i+1<=x && j-1>0 &&j+1<=x &&a[i+1][j] == '#' && a[i+1][j-1] == '#' && a[i+1][j+1] == '#')
            {
                vals[i][j] = min(min(vals[i+1][j], vals[i+1][j-1]), vals[i+1][j+1]) + 1;
            }
        }
    }
    for(int i = 0; i<=x; i++)
    {
        for(int j = 0; j<=x; j++)
        {
            total +=vals[i][j];
        }
    }
    cout<<total<<endl;
}

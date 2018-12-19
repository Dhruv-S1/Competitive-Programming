#include <bits/stdc++.h>
#include <math.h>

using namespace std;
long long great(long long a, long long b)
{
    if (a >= b)
        return a;
    return b;
}
long long lesser(long long a, long long b)
{
    if (a <= b)
        return a;
    return b;
}
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	long long m = 0, n = 0, k = 0, total = 0;
	cin >> m >> n >> k;
	int a[n+1][m+2];
	for (int i = 0; i < n+1; i++)
	{
        for (int j = 0; j < m+2; j++)
            a[i][j] = 0;
	}
	long long col, row, rad, bit;
	for (int i = 0; i < k; i++)
    {
        cin >> col >> row >> rad >> bit;
        for(int j = great(1, col-rad); j < lesser(col+rad, n)+1; j++)
        {
            long long o = (long long)sqrt((rad * rad) - ((col-j)*(col-j))), up = lesser(m, row+o), down = great(1, row-o);
            a[j][down]+= bit;
            a[j][up+1]-= bit;
        }
    }
    long long maxl = 0, Count = 0;
    for (int i = 0; i < n+1; i++)
    {
        for (int j = 1; j < m+2; j++)
        {

            a[i][j] = a[i][j-1]+a[i][j];
            if(a[i][j] > maxl)
            {
                maxl = a[i][j];
                Count = 1;
            }
            else if (a[i][j] == maxl)
                Count = Count+1;
        }
    }
    long long r = maxl + total;
    cout << r << '\n' << Count;
	return 0;
}

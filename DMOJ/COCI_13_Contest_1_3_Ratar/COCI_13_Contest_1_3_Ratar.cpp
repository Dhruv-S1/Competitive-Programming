#include <iostream>
using namespace std;
long long n, hold1, total, square_sum;
long long a[52][52];
long long prefix_a[52][52];

//NOTE: This partial solution gives 60/100 points

inline long long findsum_diagonal_right(long long r1, long long c1, long long sum1)
{
    long long total1=0;
    long long right_sum=0;
    if(r1>n or c1 >n) return 0;
    for(long long i = r1; i<=n; i++)
    {
        for(long long j = c1; j<=n; j++)
        {
            right_sum = prefix_a[i][j] - prefix_a[r1-1][j]-prefix_a[i][c1-1]+prefix_a[r1-1][c1-1];
            if(right_sum == sum1) total1+=1;
        }
    }
    return total1;
}
inline long long findsum_diagonal_left(long long r1, long long c1, long long sum1)
{
    long long total1=0;
    long long left_sum=0;
    if(c1 == 0 or r1>n) return 0;
    for(long long i = r1; i<=n; i++)
    {
        for(long long j = c1; j>0; j--)
        {
            left_sum = prefix_a[i][c1]-prefix_a[r1-1][c1]-prefix_a[i][j-1]+prefix_a[r1-1][j-1];
            if(left_sum == sum1) total1+=1;
        }
    }
    return total1;
}
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    for(long long i = 1; i<=n; i++)
    {
        for(long long j = 1; j<=n; j++)
        {
            cin>>hold1;
            a[i][j] = hold1;
            prefix_a[i][j] = hold1+prefix_a[i][j-1];

        }
    }
    for(long long j = 1; j<=n; j++)
    {
        for(long long i = 1; i<=n; i++)
        {
            prefix_a[i][j] = prefix_a[i-1][j]+prefix_a[i][j];
        }
    }

    for(long long i = 1; i<=n; i++)
    {
        for(long long j = 1; j<=n; j++)
        {
            for(long long k = i; k<=n; k++)
            {
                for(long long t = j; t<=n; t++)
                {
                    square_sum = prefix_a[k][t]-prefix_a[k][j-1]-prefix_a[i-1][t] + prefix_a[i-1][j-1];
                    total += findsum_diagonal_right(k+1, t+1, square_sum) + findsum_diagonal_left(k+1, j-1, square_sum);
                }
            }
        }
    }
    cout<<total<<endl;
}

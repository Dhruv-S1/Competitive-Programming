#include <iostream>
#include<vector>
#include <iomanip>
using namespace std;
long long n, hold2;
double dp[2097152];
vector<double> jobs[21];
double hold1;

double recurse(long long i, long long b)
{
    if(i == n+1) return 1.0;
    if(dp[b]!=-1)
    {
        return dp[b];
    }
    double res = 0.0;
    double next;
    for(long long k = 0; k<n; k++)
    {
        if(not((b>>(k+1)) & 1UL))
        {
            long long hold7 = b;
            hold7 |=1 <<(k+1);
            next = jobs[i][k]*recurse(i+1, hold7);
            res = max(res, next);
        }
    }
    dp[b]= res;
    return res;

}
int main()
{
    for(long long i = 0; i<=2097151; i++)
    {
        dp[i] = -1;
    }
    cin>>n;
    for(long long i = 1; i<=n; i++)
    {
        for(long long j = 1; j<=n; j++)
        {
            cin>>hold1;
            jobs[i].push_back(hold1/100);
        }
    }
    cout<<setprecision(9)<<recurse(1, 0)*100<<endl;
}

#include <iostream>

using namespace std;
long long n, m, hold1, hold2, large, count1;
long long a[101][101];
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    large = -1;
    count1 = 0;
    for(long long i = 0; i<m; i++)
    {
        cin>>hold1>>hold2;
        a[hold1][hold2] = 1;
    }
    for(long long i = 1; i<=m; i++)
    {
        if(m%i == 0)
        {
            for(long long j = 1; j<=n-i+1; j++)
            {
                for(long long k = 1; k<=n-(m/i)+1; k++)
                {
                    count1 = 0;
                    for(long long h = j; h<=j+i-1; h++)
                    {
                        for(long long g = k; g<=k+(m/i)-1; g++)
                        {
                            count1 +=a[g][h];
                        }
                    }
                    if (count1>large) large = count1;
                }
            }

        }
    }

    cout<<m - large<<endl;

}

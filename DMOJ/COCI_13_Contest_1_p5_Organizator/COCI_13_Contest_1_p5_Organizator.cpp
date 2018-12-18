#include <iostream>
#include<math.h>
using namespace std;
long long have[2000001];
long long div1[2000001];
long long n, m, hold, total;
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold;
        have[hold] += 1;
    }
    long long k = 1;
    while(k<=(long long)ceil(sqrt(2000001)))
    {
        for(long long j = k; j<=2000000; j+=k)
        {
            if(have[j])
            {
                div1[k]+=have[j];
                if(j/k>(long long)ceil(sqrt(2000001))) div1[j/k]+=have[j];
            }
        }
        k+=1;
    }
    total = 0;
    for(long long i = 1; i<=2000000; i++)
    {
        if (i*div1[i]>total and div1[i]>=2)
        {
            total = i*div1[i];
        }
    }
    cout<<total<<endl;
}

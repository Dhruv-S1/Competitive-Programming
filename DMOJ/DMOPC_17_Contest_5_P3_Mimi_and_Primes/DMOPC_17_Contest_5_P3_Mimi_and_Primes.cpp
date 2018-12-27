#include <iostream>
#include <math.h>
using namespace std;
long long a[100001];
long long hold1, x, b;
long long gcd(long long c, long long d, long long res)
{
    if(c == d) return c*res;
    else if(c%2 == 0 and d%2 == 0) return gcd(c/2, b/2, 2*res);
    else if(c%2 ==0) return gcd(c/2, d, res);
    else if(d%2 ==0) return gcd(c, d/2, res);
    else if(c>d) return gcd(c-d, d, res);
    else return gcd(c, d-c, res);
}
long long gcf(long long j)
{
    long long big = -1;
    while(j%2 == 0)
    {
        j = j/2;
        big = 2;
    }
    for(long long i = 3; i<=sqrt(j); i+=2)
    {
        while(j%i == 0)
        {
            if (i>big) big = i;
            j = j/i;
        }
    }
    if(j>2) return j;
    return big;
}


int main()
{
    cin>>x;
    for(long long i = 0; i<x; i++)
    {
        cin>>hold1;
        a[i] = hold1;
    }
    b = a[0];
    for(long long i = 1; i<x; i++)
    {
        b = gcd(a[i],b, 1);
    }
    long long h = gcf(b);
    if(h!=-1) cout<<h<<endl;
    else cout<<"DNE"<<endl;
}

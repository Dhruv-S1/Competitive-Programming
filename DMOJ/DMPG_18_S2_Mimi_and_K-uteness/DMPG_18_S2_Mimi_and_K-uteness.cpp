#include <iostream>
using namespace std;

long long prefix[200001];
long long a[200001];
long long b[100002];
long long x, hold1, z;

int main()
{
    cin>>x;
    for(long long i = 0; i<x; i++)
    {
        cin>>hold1;
        a[i] = hold1;
    }
    prefix[0] = a[0];
    for(long long i = 1; i<x; i++)
    {
        prefix[i] = a[i]+prefix[i-1];
    }
    long long totalsum = 0;

    for(long long i = 0; i<x; i++)
    {
        totalsum+=a[i];
    }
    b[0] = totalsum;
    cout<<totalsum<<endl;
    if(x%2 == 0)
    {
        z = x-1;
    }
    else
    {
        z = x;
    }
    for(long long i = 1; i<=z/2; i++)
    {
        cout<<totalsum+(prefix[x-i-1] - prefix[i-1])<<endl;
        totalsum = totalsum+(prefix[x-i-1] - prefix[i-1]);
        b[i] = totalsum;
    }
    if (x%2 == 1) z=z-2;
    for(long long i =z/2; i>=0; i--)
    {
        cout<<b[i]<<endl;
    }
}

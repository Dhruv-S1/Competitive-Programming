#include <iostream>

using namespace std;
long long n, t, k ,v, rightmin = -1, total, count1 = 0, hold;
long long a[1000002];
int main()
{
    cin>>n>>t>>k>>v;
    for(long long i = 0; i<v; i++)
    {
        cin>>hold;
        a[hold] = 1;
    }
    for(long long i = 1; i<=t; i++)
    {
        total+= a[i];
    }
    if(total<k)
    {
        for(long long i = t; i>0; i--)
        {
            if(a[i] == 0)
            {
                a[i] = 1;
                total +=1;
                count1 +=1;
            }
            if(total == k) break;
        }
    }
    for(long long i = 1; i<=n-t; i++)
    {
        total-=a[i];
        total+=a[i+t];
        if(total<k)
        {
            a[i+t] = 1;
            total+=1;
            count1 +=1;
        }
    }
    cout<<count1<<endl;
}

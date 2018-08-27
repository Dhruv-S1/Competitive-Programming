#include <iostream>

using namespace std;
bool a[100001];
long long vals[1000001], BIT[1000001], BIT2[1000001];
long long x, t, hold, b, c, k;
long long min1 = 99999999999;

void primes()
{
    for(long long i = 0; i<100001; i++) a[i] = 0;
    long long n = 2;
    while(n<317)
    {
        if(not a[n])
        {
            for(long long i = n*2; i<100001;i+=n)
            {
                a[i] = 1;
            }
        }
        n+=1;

    a[1] = 1;
    }
}
long long update(long long BIT3[], long long index, long long val1)
{
    while(index<=x)
    {
        BIT3[index]+=val1;
        index+=index&(-index);
    }
}

long long sum(long long BIT3[], long long index)
{
    long long total = 0;
    while(index>0)
    {
        total +=BIT3[index];
        index -=index&(-index);
    }
    return total;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    primes();
    cin>>x>>t;
    for(long long i = 1; i<=x; i++)
    {
        cin>>hold;
        vals[i] = hold;
    }
    for(long long i = 1; i<=x; i++)
    {
        vals[i] +=vals[i-1];
    }

    for(long long i = 0; i<t; i++)
    {
        cin>>b>>c>>k;
        if(not a[i+1])
        {
            hold = ((((sum(BIT, c)*c-sum(BIT2, c))-(sum(BIT, b-1)*(b-1)-sum(BIT2, b-1))) + (vals[c]-vals[b-1]) + k))*(i+1);
            if(hold<min1) min1 = hold;
        }
        else
        {
            update(BIT, b, k);
            update(BIT, c+1, -k);
            update(BIT2, b, k*(b-1));
            update(BIT2, c+1, -k*c);
        }
    }
    cout<<min1<<endl;
}

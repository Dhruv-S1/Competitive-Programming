#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<long long> a;
long long bit[500001];
long long add(long long pos)
{
    long long sum1 = 0;
    while (pos>0)
    {
        sum1 +=bit[pos];
        pos -= pos&(-pos);
    }
    return sum1;
}
long long update(long long pos, long long x)
{
    while (pos<=x)
    {
        bit[pos] +=1;
        pos += pos&(-pos);
    }
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    long long x = 0;
    cin>>x;
    long long inv = 0;
    for(int i =0 ; i<x; i++)
    {
        long long y = 0;
        cin>>y;
        a.push_back(y);
    }
    for(int i = 0; i<a.size(); i++)
    {
        if (a[i] == 1)
        {
            update(a[i], x);
            continue;
        }

        if(a[i] == x)
        {
            update(a[i], x);
            continue;
        }

        int j = min(add(a[i]), (add(x) - add(a[i])));
        inv += j;
        update(a[i], x);
    }
    cout<<inv;
}

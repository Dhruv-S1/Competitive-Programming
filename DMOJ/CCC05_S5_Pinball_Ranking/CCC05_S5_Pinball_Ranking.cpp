#include<bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include<utility>
using namespace std;
long long x, counter;
pair<long long, long long> numbers[100001];
long long a[100001];
double total = 0.00;
long long BIT[100001];


void update(long long pos)
{
    while(pos<=100001)
    {
        BIT[pos] +=1;
        pos +=pos&(-pos);
    }
}

long long getsum(long long pos)
{
    long long sum = 0;

    while(pos>0)
    {
        sum+= BIT[pos];
        pos -=pos&(-pos);
    }
    return sum;
}

int main()
{
    cin>>x;
    for(long long i = 0; i<100001; i++)
    {
        numbers[i].first = -1;
        a[i] = -1;
    }
    for(long long i = 0; i<x;i++)
    {
        scanf("%lld", &numbers[i].first);
        numbers[i].second = i;
    }

    sort(numbers, numbers+100001);

    for(long long i = 0; i<100001; i++)
    {
        if(numbers[i].first != -1)
        {
            counter +=1;
            numbers[i].first = counter;
            a[numbers[i].second] = numbers[i].first;

        }
    }


    for(long long i = 0; i<x; i++)
    {
        total += (i+1) - getsum(a[i]);
        update(a[i]);
    }
    cout<<setprecision(2)<<fixed<<total/x<<endl;



}

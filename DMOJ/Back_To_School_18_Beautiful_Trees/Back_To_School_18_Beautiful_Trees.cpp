#include <iostream>
#include <vector>
#include<math.h>
#include<cmath>
using namespace std;
long long n, hold1, hold2;


struct node{
    long long value;
    long long longest_chain;
    vector<long long> connect;
} a[100002];

long long solve(long long y)
{
    if(floor((-1+sqrt(1+4*y))/2) == ceil((-1+sqrt(1+4*y))/2)) return 1;
    else if(floor((-1-sqrt(1+4*y))/2) == ceil((-1-sqrt(1+4*y))/2)) return 1;
    else return 0;
}
long long dfs(long long node, long long prevnode)
{
    long long total = 0;
    long long total1 = 0;
    for(long long i = 0;i<a[node].connect.size(); i++)
    {
        if(a[node].connect[i] == prevnode) continue;
        hold1 = dfs(a[node].connect[i], node);
        if(hold1>total)
        {
            total1 = total;
            total = hold1;
        }
        else if(hold1>total1) total1 = hold1;
    }
    if(solve(a[node].value))
    {
        a[node].longest_chain = total+total1+1;
        return total+1;
    }
    else
    {
        a[node].longest_chain = 0;
        return 0;
    }
}


int main()
{
    cin>>n;
    for(long long i= 1; i<=n; i++)
    {
        cin>>hold1;
        a[i].value = hold1;
    }
    for(long long i = 1; i<=n-1; i++)
    {
        cin>>hold1>>hold2;
        a[hold1].connect.push_back(hold2);
        a[hold2].connect.push_back(hold1);
    }
    dfs(1, -1);
    long long val = 0;
    for(long long i = 1; i<n; i++)
    {
        val = max(val, a[i].longest_chain);
    }
    cout<<val<<endl;

}

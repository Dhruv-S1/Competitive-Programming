#include <iostream>
#include <vector>
#include <set>
using namespace std;
long long arr[100001];
long long amount[100001];
vector<long long> taken;
long long num1, num2;
struct edge
{
    long long to, from;
};
vector <edge> v;
long long n, m;
long long root (long long a)
{
    while(arr[a] != a)
    {
        arr[a] = arr[arr[a]];
        a = arr[a];
    }
    return a;
}
void tog(long long a, long long b)
{
    long long roota = root(a);
    long long rootb = root(b);
    if(amount[roota]<amount[rootb])
    {
        arr[roota] = arr[rootb];
        amount[rootb] +=amount[roota];
    }
    else
    {
        arr[rootb] = arr[roota];
        amount[roota] += amount[rootb];
    }
}




int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for(long long i = 1; i<=n; i++)
    {
        arr[i] = i;
        amount[i] = 1;
    }
    for(long long i = 1; i<=m ; i++)
    {
        cin>>num1>>num2;
        if(root(num1) != root(num2))
        {
            tog(num1, num2);
            taken.push_back(i);
        }
        if(taken.size() == n-1) break;
    }
    if(taken.size() == n-1) for(long long i = 0; i<taken.size(); i++) cout<<taken[i]<<endl;
    else cout<<"Disconnected Graph"<<endl;

}

#include <iostream>
#include <vector>
using namespace std;

long long hold, hold1, hold2, n, number;
long long bit[200001];
vector<long long> par[200001];
pair<long long, long long> pos[200001];
long long ans[200001];
void update(long long index, long long val)
{
    while(index<=n)
    {
        bit[index] +=val;
        index+=index&(-index);
    }
}
long long getSum(long long index)
{
    long long sum = 0;
    while(index>0)
    {
        sum+=bit[index];
        index-=index&(-index);
    }
    return sum;
}
void dfs(long long node)
{
    number+=1;
    pos[node].first = number;
    for(long long i = 0; i<par[node].size(); i++)
    {
        dfs(par[node][i]);
    }
    pos[node].second = number;
}
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold;
        par[hold].push_back(i+1);
    }

    dfs(par[0][0]);
    for(long long i = 0; i<n; i++)
    {
        cin>>hold;
        hold1 = (getSum(pos[hold].second) - getSum(pos[hold].first)+1)%1000000007;
        update(pos[hold].first, (hold1)%1000000007);
        ans[hold] = (hold1)%1000000007;

    }
    for(long long i = 1; i<n+1; i++) cout<<ans[i]%1000000007<<" ";
}

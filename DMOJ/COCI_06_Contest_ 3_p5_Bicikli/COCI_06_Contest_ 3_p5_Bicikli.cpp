#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
long long n, m, hold1, hold2, marker, total1, marker2;
long long MOD = 1000000000;
vector<long long> a[10002];
stack<long long> cycle_node;
queue<long long> t;
long long cyc[10002];
long long vis[10002];
long long b[10002];
void cycles(long long node)
{
    if(b[node]!=-1) return;
    cycle_node.push(node);
    vis[node] = 1;
    for(long long i = 0; i<a[node].size(); i++)
    {
        if(vis[a[node][i]])
        {
            while(true)
            {
                if(cycle_node.top() == a[node][i] or !cycle_node.empty())
                {
                    hold1 = cycle_node.top();
                    cyc[hold1] = 1;
                    b[hold1] = 1;
                    cycle_node.pop();
                    break;
                }
                hold1 = cycle_node.top();
                cyc[hold1] = 1;
                b[hold1] = 1;
                cycle_node.pop();
                t.push(hold1);
            }
            while(!t.empty())
            {
                hold1= t.front();
                cycle_node.push(hold1);
                t.pop();
            }
        }
      else cycles(a[node][i]);
    }
    cycle_node.pop();
    vis[node] = 0;
    if(b[node]!= 1) b[node]= 0;
}
long long dfs( long long node)
{
    if(b[node]!= -1 or marker == 1) return b[node];
    long long total = 0;
    vis[node] = 1;
    if(node == 2)
    {
        vis[2] = 0;
        return 1;
    }
    for(long long i = 0; i<a[node].size(); i++)
    {
        if( not vis[a[node][i]])
        {
            total += dfs(a[node][i]);
            if(total>1000000000) marker2 = 1;
            total = total%MOD;
        }
    }
    vis[node] = 0;
    if(cyc[node] == 1 and total != 0)
    {
        marker = 1;
    }
    b[node] = total%MOD;
    return total%MOD;
}

int main()
{
    cin>>n>>m;
    for(long long i = 0; i<10002; i++) b[i] = -1;
    for(long long i = 0; i<m; i++)
    {
        cin>>hold1>>hold2;
        a[hold1].push_back(hold2);
    }
    cycles(1);
    for(long long i = 0; i<10002; i++) b[i] = -1;
    for(long long i = 0; i<10002; i++) vis[i] = 0;
    total1 = dfs(1);
    if(marker == 1) cout<<"inf"<<endl;
    else
    {
        if(marker2 == 1)
        {
            for(long long i = 9-to_string(total1).length(); i>0; i--)
            {
                cout<<0;
            }
            cout<<total1<<endl;
        }
        else cout<<total1<<endl;
    }
}

#include <iostream>
#include <vector>
using namespace std;
long long n, m, hold, hold1, hold2;
vector <long long> a[300001];
long long b[300001];
long long marker = 0;

long long treesearch(long long node)
{
    long long o = 0;
    long long PREV1 = 9999999999;
    long long marker1 = 0;
    for(int i =0; i<a[node].size();i++)
    {
        int o = treesearch(a[node][i]);
        if(o<PREV1)
        {
        PREV1 = o;
        marker1 = 1;
        }
    }

    if (marker1 == 1) return (b[node]+PREV1);
    else return b[node];

}


int main()
{
    cin>>n>>m;
    for(int i = 0; i<m; i++)
    {
        cin>>hold;
        cin>>hold1;
        if (hold == 1) marker = 1;
        for(int j = 0; j<hold1;j++)
        {
            cin>>hold2;
            a[hold].push_back(hold2);
        }
    }
    for(int i = 0; i<n;i++)
    {
        cin>>hold;
        b[i+1] = hold;
    }
    if(marker == 0)
    {
        cout<<b[1]<<endl;
        return 0;

    }
    cout<<treesearch(1)<<endl;

}

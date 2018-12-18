#include <iostream>
#include <vector>
#include <stack>
using namespace std;
long long freq[3][100001];
vector<vector<long long> > col;
long long arr[3][100001];
long long taken[100001] = {0};
stack<long long> tasks;
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    col.resize(100001);
    long long n = 0;
    cin>>n;
    for(int i= 0; i<3; i++)
    {
        for(int j = 0; j<n; j++)
        {
            long long t = 0;
            cin>>t;
            arr[i][j] = t;
            freq[i][t] +=1;
            col[t].push_back(j);
        }
    }
    for(int i = 1; i<=n; i++)
    {
        if (freq[1][i] == 0 || freq[2][i] == 0)
        {
            tasks.push(i);
        }
    }

    long long total = 0;
    while(!tasks.empty())
    {
        long long delete1 = tasks.top();
        tasks.pop();
        for(int i = 0; i<col[delete1].size();i++)
        {
            if (taken[col[delete1][i]] == 1) continue;
            total+=1;
            taken[col[delete1][i]] = 1;
            freq[0][arr[0][col[delete1][i]]] -=1;
            if (freq[0][arr[0][col[delete1][i]]] == 0) tasks.push(arr[0][col[delete1][i]]);

            freq[1][arr[1][col[delete1][i]]] -=1;
            if (freq[1][arr[1][col[delete1][i]]] == 0) tasks.push(arr[1][col[delete1][i]]);

            freq[2][arr[2][col[delete1][i]]] -=1;
            if (freq[2][arr[2][col[delete1][i]]] == 0) tasks.push(arr[2][col[delete1][i]]);


        }
    }
    cout<<total;
}

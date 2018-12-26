#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include<math.h>
#include<stdlib.h>
using namespace std;
string a[501];
long long vis[501];
vector<long long> b[501];
long long pre[501][501];
long long n, q, hold, hold1, hold2, num1, num2;
string hold3;
vector<long long> current;
vector<long long> start;

bool check(string str1, string str2)
{
    num1 = str1.length();
    num2 = str2.length();
    if(num1 == num2)
    {
        long long count1 = 0;
        for(long long k = 0; k<num1; k++)
        {
            if(str1[k]!=str2[k]) count1+=1;
        }
        if(count1 == 1) return 1;
        else return 0;
    }
    if(abs(num1-num2) == 1)
    {
        long long total = 0;
        long long cnt1 = 0;
        long long cnt2 = 0;
        while(true)
        {
            if(cnt1>num1 or cnt2>num2) break;
            if(str1[cnt1] == str2[cnt2])
            {
                cnt1+=1;
                cnt2+=1;
                continue;
            }
            if(str1[cnt1]!=str2[cnt2])
            {
                if(num1>num2) cnt1+=1;
                else cnt2 +=1;
                total+=1;
            }
        }
        if(total == 1) return 1;
        else return 0;
    }
    return 0;
}
long long bfs(long long source)
{
    current.clear();
    start.clear();
    for(long long i = 0; i<n; i++)
    {
        vis[i] = 0;
    }
    vis[source] = 1;
    long long total = 0;

    start.push_back(source);
    while(true)
    {
        for(long long i = 0; i<start.size();i++)
        {
            for(long long j = 0; j<b[start[i]].size(); j++)
            {
                if(not vis[b[start[i]][j]])
                {
                    current.push_back(b[start[i]][j]);
                    vis[b[start[i]][j]] = 1;
                    pre[source][b[start[i]][j]] = total+1;
                }
            }
        }
        total+=1;
        if(current.size() == 0) return -1;
        start.clear();
        for(long long k = 0; k<current.size(); k++)
        {
            start.push_back(current[k]);
        }
        current.clear();
    }

}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold3;
        a[i] = hold3;
    }

    for(long long i = 0; i<n; i++)
    {
        for(long long j = i+1; j<n;j++)
        {
            if(check(a[i], a[j]))
            {
                b[i].push_back(j);
                b[j].push_back(i);
            }
        }
    }
    for(long long i = 0; i<n; i++)
    {
        bfs(i);
    }
    cin>>q;
    for(long long i = 0; i<q; i++)
    {
        cin>>hold>>hold1;
        if(hold == hold1)
        {
            cout<<0<<endl;
            continue;
        }

        if(pre[hold-1][hold1-1] == 0)
        {
            cout<<-1<<endl;
            continue;
        }

        cout<<pre[hold-1][hold1-1]<<endl;


    }
}

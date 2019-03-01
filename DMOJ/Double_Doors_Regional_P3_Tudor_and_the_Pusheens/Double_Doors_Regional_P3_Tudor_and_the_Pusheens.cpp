#include <iostream>
#include<vector>
using namespace std;
long long m,n,s, t, hold1, hold2, count1;
vector<long long> a[1000001];
vector<long long> current;
vector<long long> start;
long long taken[1000001];
int main()
{
    cin>>n>>m;
    for(long long i =0; i<m; i++)
    {
        cin>>hold1>>hold2;
        a[hold1].push_back(hold2);
        a[hold2].push_back(hold1);

    }
    cin>>s>>t;
    if(s == t)
    {
        cout<<m<<endl;
        return 0;
    }
    start.push_back(s);
    taken[s] = 1;
    while(true)
    {
        for(long long i = 0; i<start.size(); i++)
        {
            for(long long j = 0; j<a[start[i]].size(); j++)
            {
                if(not taken[a[start[i]][j]])
                {
                    current.push_back(a[start[i]][j]);
                    taken[a[start[i]][j]] = 1;
                }
            }
        }
        count1+=1;
        if(count1 == n)
        {
            cout<<0<<endl;
            break;
        }
        if(taken[t] == 1)
        {
            cout<<m-(count1)<<endl;
            break;
        }
        start.clear();
        for(long long k = 0; k<current.size(); k++) start.push_back(current[k]);
        current.clear();


    }


}

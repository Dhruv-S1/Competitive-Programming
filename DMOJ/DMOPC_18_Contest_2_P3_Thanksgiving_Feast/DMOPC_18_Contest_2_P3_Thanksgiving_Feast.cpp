#include <iostream>
#include <vector>
using namespace std;
long long n, m, k, a, b, hold1, hold2;
long long gift_buildings[100001];
vector<long long> roads[100001];
long long from_n[100001];
long long from_m[100001];
long long vis[100001];
vector<long long> current;
vector<long long> current1;
void bfs(long long b[], long long y)
{
    b[y] = 0;
    current.push_back(y);
    long long count1 = 1;
    vis[y] = 1;
    while(true)
    {
        for(long long i = 0; i<current.size(); i++)
        {
            for(long long j = 0; j<roads[current[i]].size(); j++)
            {
                if(!vis[roads[current[i]][j]])
                {
                    b[roads[current[i]][j]] = count1;
                    current1.push_back(roads[current[i]][j]);
                    vis[roads[current[i]][j]] = 1;
                }
            }
        }
        if(current1.size() == 0) break;
        current.clear();
        for(long long i = 0; i<current1.size(); i++)
        {
            current.push_back(current1[i]);
        }
        current1.clear();
        count1+=1;
    }
}

int main()
{
    cin>>n>>m>>k>>a>>b;
    for(long long i = 0; i<k; i++)
    {
        cin>>hold1;
        gift_buildings[hold1] = 1;
    }
    for(long long i = 0; i<m; i++)
    {
        cin>>hold1>>hold2;
        roads[hold1].push_back(hold2);
        roads[hold2].push_back(hold1);
    }

    bfs(from_n, a);
    for(long long i = 0; i<100001; i++)
    {
        vis[i] = 0;
    }
    current.clear();
    current1.clear();
    bfs(from_m, b);
    long long min1 = 999999999;
    for(long long i = 0; i<100001; i++)
    {
        if(gift_buildings[i])
        {
            if(from_m[i]+from_n[i]<min1) min1 = from_m[i]+from_n[i];
        }
    }
    cout<<min1<<endl;

}

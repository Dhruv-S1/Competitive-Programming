#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct pen_side{
long long cell1;
long long cell2;
long long weight;
} a[200][200];
long long vis[103];
vector<pair<long long, long long> > edge[102];
long long n, m, hold1, hold2, total;
long long holda[204];
vector<pair<long long, long long> > pens[102];
vector<pair<long long, long long> > curarray;
int main()
{
    for(long long i = 0; i<200; i++)
    {
        for(long long j = 0; j<200; j++)
        {
            a[i][j].cell1 = -1;
            a[i][j].cell2 = -1;
        }
    }
    cin>>n;
    for(long long i = 1; i<n+1; i++)
    {
        cin>>m;
        for(long long j = 0; j<203; j++) holda[j] = 0;
        for(long long j = 0; j<m*2; j++)
        {
            cin>>hold1;
            holda[j] = hold1;
        }
        if(a[holda[0]][holda[m-1]].cell1==-1){
            a[holda[0]][holda[m-1]].cell1 = i;
            a[holda[0]][holda[m-1]].weight = holda[2*m-1];
            a[holda[m-1]][holda[0]].cell1 = i;
            a[holda[m-1]][holda[0]].weight = holda[2*m-1];
            pens[i].push_back(make_pair(holda[0], holda[m-1]));


        }
        else{
            a[holda[0]][holda[m-1]].cell2 = i;
            a[holda[0]][holda[m-1]].weight = holda[2*m-1];
            a[holda[m-1]][holda[0]].cell2 = i;
            a[holda[m-1]][holda[0]].weight = holda[2*m-1];
            pens[i].push_back(make_pair(holda[0], holda[m-1]));

        }
        for(long long j = 0; j<m-1; j++)
        {
            if(a[holda[j]][holda[j+1]].cell1==-1)
            {
                a[holda[j]][holda[j+1]].cell1 = i;
                a[holda[j]][holda[j+1]].weight = holda[m+j];
                a[holda[j+1]][holda[j]].cell1 = i;
                a[holda[j+1]][holda[j]].weight = holda[m+j];

                pens[i].push_back(make_pair(holda[j], holda[j+1]));
            }
            else
            {
                a[holda[j]][holda[j+1]].cell2 = i;
                a[holda[j]][holda[j+1]].weight = holda[m+j];
                a[holda[j+1]][holda[j]].cell2 = i;
                a[holda[j+1]][holda[j]].weight = holda[m+j];
                pens[i].push_back(make_pair(holda[j], holda[j+1]));
            }

        }
    }
    for(long long i = 1; i<=n; i++)
    {
        for(long long j = 0; j<pens[i].size(); j++)
        {
            if(a[pens[i][j].first][pens[i][j].second].cell1!=i)
            {
                if(a[pens[i][j].first][pens[i][j].second].cell1==-1)
                {
                	edge[i].push_back(make_pair(0,a[pens[i][j].first][pens[i][j].second].weight));
                	edge[0].push_back(make_pair(i,a[pens[i][j].first][pens[i][j].second].weight));
                }
                else edge[i].push_back(make_pair(a[pens[i][j].first][pens[i][j].second].cell1, a[pens[i][j].first][pens[i][j].second].weight));
            }
            if(a[pens[i][j].first][pens[i][j].second].cell2!=i)
            {
                if(a[pens[i][j].first][pens[i][j].second].cell2==-1)
                {
                	edge[i].push_back(make_pair(0, a[pens[i][j].first][pens[i][j].second].weight));
                	edge[0].push_back(make_pair(i, a[pens[i][j].first][pens[i][j].second].weight));
                }
                else edge[i].push_back(make_pair(a[pens[i][j].first][pens[i][j].second].cell2, a[pens[i][j].first][pens[i][j].second].weight));
            }
        }
    }
    hold1 = 0;
    long long curnode = 1;
    while(true)
    {
    	vis[curnode] = 1;
    	for(long long i = 1; i<=n; i++) 
    	{
    		if(vis[i]==1) hold1+=1;
    	}
    	if(hold1 == n) break;
    	hold1 = 0;
    	for(long long i = 0; i<edge[curnode].size(); i++)
    	{
    		if(!vis[edge[curnode][i].first])
    		{
    			curarray.push_back(edge[curnode][i]);
    			
    		}
    	}
    	m = 99999999;
    	
    	for(long long i = 0; i <curarray.size(); i++)
    	{
    		if(!vis[curarray[i].first])
    		{
    			if(curarray[i].second<m)
    			{
    				curnode = curarray[i].first;
    				m = curarray[i].second;
    			}
    		}
    	}
    	
    	total+=m;
    }
    cout<<total<<endl;

}

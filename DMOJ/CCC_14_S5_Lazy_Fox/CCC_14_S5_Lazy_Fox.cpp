#include <iostream>
#include <set>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;
int best[20002];
int before[20002];
int distance1[20002];
std::vector<vector<int> > points;
std::vector<vector<int> > pairs;

//NOTE that this partial solution only gives 100/150 points.

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int x = 0;
    cin>>x;
    std::vector<int> temp(3);
    points.push_back(temp);
    for(int i =0; i<x; i++)
    {
        std::vector<int> temp(3);
        cin>>temp[0];
        cin>>temp[1];
        temp[2] = i+1;
        points.push_back(temp);
    }
    for(int i =0; i<points.size();i++)
    {
        for(int j =i+1; j<points.size();j++)
        {
            int x = (points[i][0]-points[j][0])*(points[i][0]-points[j][0]);
            int y = (points[i][1] - points[j][1])*(points[i][1] - points[j][1]);
            std::vector<int> temp(3);
            temp[0] = x+y;
            temp[1] = points[i][2];
            temp[2] = points[j][2];
            pairs.push_back(temp);
        }
    }
    std::sort(pairs.begin(), pairs.end());
    for(int i = 0; i<pairs.size();i++)
    {
        int a = pairs[i][0];
        int b = pairs[i][1];
        int c = pairs[i][2];
        if (a != distance1[b])
        {
            distance1[b] = a;
            before[b] = best[b];
        }
        if(a!=distance1[c])
        {
            distance1[c] = a;
            before[c] = best[c];
        }
        if (b==0) best[b] = max(best[b], before[c]);
        else
        {
            best[b] = max(best[b], before[c]+1);
            best[c] = max(best[c], before[b]+1);
        }
    }
    cout<<best[0]+1;

}

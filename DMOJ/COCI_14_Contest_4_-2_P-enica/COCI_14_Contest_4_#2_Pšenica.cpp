#include <iostream>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;
long long count1[100001];
deque<pair<long long, long long> > a;
long long x, y, z, hold1;
int main()
{
    cin>>x;
    for(long long i = 0; i<x; i++)
    {
        cin>>z;
        count1[z]+=1;
    }
    for(long long i = 0; i<100001; i++)
    {
        if(count1[i])
        {
            a.push_back(make_pair(i, count1[i]));
        }
    }
    if(a.size()<3)
    {
        cout<<"Slavko"<<endl;
        cout<<a[0].first<<" "<<a[a.size()-1].first;
        return 0;
    }
    while(true)
    {
        if(a.front().second>a.back().second)
        {
            a.front().second -= a.back().second;
            hold1 = a.back().second;
            a.pop_back();
            a.back().second+=hold1;
            a[1].second+=hold1;
        if(a.size() == 2)
            {
                cout<<"Slavko"<<endl;
                cout<<a.front().first<<" "<<a.back().first<<endl;
                return 0;
            }
        }
        else if(a.front().second<a.back().second)
        {
            a.back().second-=a.front().second;
            hold1 = a.front().second;
            a.pop_front();
            a[0].second+=hold1;
            a[a.size()-2].second+=hold1;
            if(a.size() == 2)
            {
                cout<<"Mirko"<<endl;
                cout<<a.front().first<<" "<<a.back().first<<endl;
                return 0;
            }
        }
        else if(a.front().second == a.back().second)
        {
            if(a.size() <= 4)
            {
                cout<<"Slavko"<<endl;
                a.pop_front();
                a.pop_back();
                cout<<a.front().first<<" "<<a.back().first<<endl;
                return 0;
            }
            else
            {
                hold1 = a.front().second;
                a.pop_front();
                a.pop_back();
                a.front().second +=hold1;
                a.back().second +=hold1;
            }
        }
    }
}

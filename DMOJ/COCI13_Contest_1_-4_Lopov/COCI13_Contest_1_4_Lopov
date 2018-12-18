#include <iostream>
#include <set>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;
map<long long, long long> bags_left;
set<long long> bag_value;
vector<pair<long long, long long> >jewl;
long long n, k, hold1, hold2, total;
pair <long long, long long> hold3;
bool is_in;
int main()
{
    cin>>n>>k;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold1>>hold2;
        hold3.first = hold2;
        hold3.second = hold1;
        jewl.push_back(hold3);
    }
    for(long long i = 0; i<k; i++)
    {
        cin>>hold1;
        is_in = bag_value.find(hold1) != bag_value.end();
        if(is_in) bags_left[hold1]+=1;
        else
        {
            bag_value.insert(hold1);
            bags_left[hold1]=1;
        }
    }
    sort(jewl.begin(), jewl.end());
    set<long long>::iterator hold1;
    for(long long i = n-1; i>=0; i--)
    {
        hold1 = bag_value.lower_bound(jewl[i].second);
        if(hold1 == bag_value.end()) continue;
        hold2 = *hold1;
        if(hold2>=jewl[i].second)
        {
            total+=jewl[i].first;
            bags_left[hold2]-=1;
            if(bags_left[hold2] == 0)
            {
                bag_value.erase(hold2);
                bags_left.erase(hold2);
            }
        }
    }
    cout<<total<<endl;

}

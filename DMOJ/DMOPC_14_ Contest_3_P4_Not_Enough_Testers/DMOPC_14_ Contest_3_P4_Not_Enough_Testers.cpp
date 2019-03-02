#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
long long q, hold1, t, hold2, hold3;
long long factors[100001];
vector <long long> a[129];
vector<long long>::iterator lower, upper;
// NOTE this partial solution yields 60/100 points
int main()
{
    cin>>t;
    for(long long i = 1; i<100001; i++) factors[i] = 0;
    long long k = 0;
    while (k<100001)
    {
        k+=1;
        for(long long j = k; j<100001;j+=k)
        {
            if(j<100001)  factors[j]+=1;
        }
    }
    for(long long i = 1; i<100001; i++)
    {
        a[factors[i]].push_back(i);
    }
    for(long long i = 0; i<t; i++)
    {
        cin>>hold1>>hold2>>hold3;
        lower = lower_bound(a[hold1].begin(), a[hold1].end(), hold2);
        upper = upper_bound(a[hold1].begin(), a[hold1].end(), hold3);
        cout<<((lower-a[hold1].begin()) - (upper - a[hold1].begin()))*-1<<endl;

    }

}

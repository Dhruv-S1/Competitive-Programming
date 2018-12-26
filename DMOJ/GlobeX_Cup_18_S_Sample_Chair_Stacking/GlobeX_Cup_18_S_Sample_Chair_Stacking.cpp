#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
long long n, hold1, hold2, total;
vector<long long> x;
vector<long long> y;
int main()
{
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold1>>hold2;
        x.push_back(hold1);
        y.push_back(hold2);
    }
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    for(long long i = 0; i<n; i++)
    {
        total+= abs(x[n/2]-x[i]);
        total+= abs(y[n/2] - y[i]);
    }
    cout<<total<<endl;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long n, hold1, current;
long long a[200001];
long long b[200001];

struct electrons{
    long long dif;
    long long bval;
    long long aval;

};
bool compareByDif(const electrons &a, const electrons &b)
{
    return a.dif < b.dif;
}
electrons hold2;
vector<electrons> f;
int main()
{
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold1;
        a[i] =hold1;
        current+=hold1;
    }
    for(long long j = 0; j<n; j++)
    {
        cin>>hold1;
        b[j] = hold1;
    }
    for(long long i = 0; i<n; i++)
    {
        hold2.dif = b[i]-a[i];
        hold2.bval = b[i];
        hold2.aval = a[i];
        f.push_back(hold2);
    }
    sort(f.begin(), f.end(), compareByDif);
    for(long long i = 0; i<n; i+=2)
    {
        if(i+1<n){

            if(current-f[i].aval-f[i+1].aval+f[i].bval+f[i+1].bval<current)
            {
                current = current-f[i].aval-f[i+1].aval+f[i].bval+f[i+1].bval;
            }
        }
        else break;
    }
    cout<<current<<endl;

}

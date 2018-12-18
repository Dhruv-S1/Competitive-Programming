#include <iostream>
#include <vector>
using namespace std;
vector<long long> a;
vector<long long>temp;
vector<long long> cof;
long long MOD = 1000000007;
long long pow(long long base,long long exponent)
{
    long long result = 1;
    while(exponent>0)
    {
        if(exponent&1)
        {
        result = (result*base);
        result = result%MOD;
        }
        exponent = exponent>>1;
        base = (base*base)%MOD;
    }
    return result%MOD;
}


int main()
{
    long long x = 0;
    cin>>x;
    for(int i = 0; i<x; i++)
    {
        long long u = 0;
        cin>>u;
        a.push_back(u);
    }
    long long m = 0;
    cin>>m;
    for(int i = 0; i<x+1;i++) temp.push_back(0);
    cof.push_back(1);
    cout<<a[0]<<" ";
    for(int i = 1; i<a.size();i++)
    {
        long long hold = (((cof[i-1]*(m+i-1))%MOD)*pow(i, MOD-2))%MOD;
        cof.push_back(hold);
        for(int j = 0;j<i+1;j++)
        {
            temp[i] +=(cof[j]*a[i-j])%MOD;
        }
        cout<<temp[i]%MOD<<" ";
    }
}

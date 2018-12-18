#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

int n = 0,q = 0;

long long seg[200001*4],lazy[200001*4];

vector<long long> a;

void construct(int left, int right, int pos)
{
    if(left == right)
    {
        seg[pos] = a[left];
    }
    else
    {
	    int mid = (left+right)/2;
	    construct(left, mid, pos*2+1);
	    construct(mid+1, right, pos*2+2);
	    seg[pos] = std::min(seg[pos*2+1], seg[pos*2+2]);
    }
}
long long update(int val, int left, int right, int curleft, int curright,int pos)
{
    if (curleft>curright)
        return 0;
    int mid = (curright+curleft)/2;
    if (lazy[pos]!=0)
    {
        seg[pos]+=lazy[pos];
        seg[pos] = std::max(seg[pos], 0LL);
        if(curleft!=curright)
        {
            lazy[pos*2+1] += lazy[pos];
            lazy[pos*2+2] += lazy[pos];
        }
    	lazy[pos] = 0;
    }
    if(curleft>right || curright<left) 
    	return 0;
    if(curleft>=left && curright<=right)
    {
        seg[pos] -= val;
        seg[pos] = std::max(seg[pos], 0LL);
        if (curleft!= curright)
        {
            lazy[pos*2+1] -=val;
            lazy[pos*2+2] -= val;
        }
    	return 0;
    }
    update(val, left, right, curleft, mid, pos*2+1);
    update(val, left, right, mid+1, curright, pos*2+2);
    seg[pos] = std::min(seg[pos*2+1],seg[pos*2+2]);
    return 0;
}
long long query(int left, int right, int curleft, int curright, int pos)
{
    if (curleft>curright)
    	return 999999999;
    int mid = (curright+curleft)/2;
    if (lazy[pos]!=0)
    {
        seg[pos]+=(lazy[pos]);
        if(curleft!=curright)
        {
            lazy[pos*2+1] += lazy[pos];
            lazy[pos*2+2] += lazy[pos];
        }
    	lazy[pos] = 0;
    }
    if(curleft>right or curright<left) 
    {
    	return 999999999;
    }
    if(curleft>=left and curright<=right) return seg[pos];
    long long a = query(left, right, curleft, mid, pos*2+1);
    long long b = query(left, right, mid+1, curright, pos*2+2);
    return std::min(a,b);
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);
    for (int i = 0; i < 200001*4; ++i)
    {
        seg[i] = 0;
        lazy[i] = 0;
    }
	cin>> n >> q;
	for(int i = 0; i<n;i++)
	{
		int y = 0;
		cin>>y;
		a.push_back(y);
	}
	construct(0, a.size()-1, 0);
	for(int i = 0;i<q;++i)
	{
	    int num1 = 0,num2 = 0,num3 = 0,num4 = 0;
	    cin>>num1>>num2>>num3;
	    update(num3, num1-1, num2-1, 0, a.size()-1,0);
	    int k = query(num1-1, num2-1, 0, a.size()-1,0);
	    int g = query(0, a.size()-1, 0, a.size()-1,0);
	    k = std::max(k, 0);
	    g = std::max(g,0);
        cout << k << " "<<g<<endl;
	}
}

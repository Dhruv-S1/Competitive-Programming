#include <bits/stdc++.h>
#include <vector>
using namespace std;

int m = 0,n = 0,q = 0;

long long seg[200001*4],lazy[200001*4];

vector<long> a;

void construct(int left, int right, int pos)
{
    if(left == right)
    {
        seg[pos] = a[left]%m;
    }
    else
    {
	    int mid = (left+right)/2;
	    construct(left, mid, pos*2+1);
	    construct(mid+1, right, pos*2+2);
	    seg[pos] = (seg[pos*2+1]+seg[pos*2+2])%m;
    }
}
long long update(int val, int left, int right, int curleft, int curright,int pos)
{
    if (curleft>curright)
        return 0;
    int mid = (curright+curleft)/2;
    if (lazy[pos]!=0)
    {
        seg[pos]+=lazy[pos]%m;
        if(curleft!=curright)
        {
            lazy[pos*2+1] += ((lazy[pos]/(curright-curleft+1))*(mid-curleft+1));
            lazy[pos*2+2] += ((lazy[pos]/(curright-curleft+1))*(curright-mid));
        }
    	lazy[pos] = 0;
    }
    if(curleft>right || curright<left) 
    	return 0;
    if(curleft>=left && curright<=right)
    {
        seg[pos] += (val*(curright-curleft+1))%m;
        if (curleft!= curright)
        {
            lazy[pos*2+1] += (val*(mid-curleft+1));
            lazy[pos*2+2] += (val*(curright-mid));
        }
    	return 0;
    }
    update(val, left, right, curleft, mid, pos*2+1);
    update(val, left, right, mid+1, curright, pos*2+2);
    seg[pos] = (seg[pos*2+1]+seg[pos*2+2])%m;
    return 0;
}
long long query(int left, int right, int curleft, int curright, int pos)
{
    if (curleft>curright)
    	return 0;
    int mid = (curright+curleft)/2;
    if (lazy[pos]!=0)
    {
        seg[pos]+=(lazy[pos])%m;
        if(curleft!=curright)
        {
            lazy[pos*2+1] += ((lazy[pos]/(curright-curleft+1))*(mid-curleft+1));
            lazy[pos*2+2] += ((lazy[pos]/(curright-curleft+1))*(curright-mid));
        }
    	lazy[pos] = 0;
    }
    if(curleft>right or curright<left) 
    {
    	return 0;
    }
    if(curleft>=left and curright<=right) return seg[pos]%m;
    long a = query(left, right, curleft, mid, pos*2+1);
    long b = query(left, right, mid+1, curright, pos*2+2);
    return (a+b)%m;
}
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    for (int i = 0; i < 200001*4; ++i)
    {
        seg[i] = 0;
        lazy[i] = 0;
    }
	cin>> m >> n >> q;
	for(int i = 0; i<n;i++)
	{
		int y = 0;
		cin>>y;
		a.push_back(y%m);
	}
	construct(0, a.size()-1, 0);
	for(int i = 0;i<q;++i)
	{
	    int num1 = 0,num2 = 0,num3 = 0,num4 = 0;
	    cin>>num1;
	    if (num1 == 1)
	    {
	        cin>>num2 >> num3>> num4;
	        update(num4%m, num2-1, num3-1, 0, a.size()-1,0);
	    }
	    if (num1 == 2)
	    {
	        cin>> num2 >> num3;
	        int k = query(num2-1, num3-1, 0, a.size()-1,0);
        	int l = k%m;
        	cout << l << '\n';
	    }
	}
}

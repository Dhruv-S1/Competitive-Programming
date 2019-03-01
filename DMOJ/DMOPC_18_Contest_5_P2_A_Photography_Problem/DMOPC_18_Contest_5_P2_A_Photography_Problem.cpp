#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
long long n, m;
long double pixels[1001][1001];
long double hold1;


long double calcavg(long double adj)
{
	long double total = 0.0;
	long double y = 1.0;
	for(long long i = 1; i<=n; i++)
	{
		for(long long j = 1; j<=m; j++)
		{
			if(pixels[i][j]*adj>y) total+=y;
			else total += pixels[i][j]*adj;
		}
	}
	return total/((long double)(m*n));
}

int main() {
	cin>>n>>m;
	
	for(long long i = 1; i<=n; i++)
	{
		for(long long j = 1; j<=m; j++)
		{
			cin>>hold1;
			pixels[i][j] = hold1;
		}
	}
	
	long double high = 100001.0;
	long double low = 0.0;
	long double mid;
	if(fabs(calcavg(1.0)-0.48) <= 0.0000001)
	{
		cout<<"correctly exposed"<<endl;
		return 0;
	}
	else if(calcavg(1.0) - 0.48>0) cout<<"overexposed"<<endl;
	else cout<<"underexposed"<<endl;
	
	
	while(true)
	{
		mid = (high+low)/2.0;
		if(fabs(calcavg(mid)-0.48) <= 0.0000001)
		{
			cout<<mid<<endl;
			return 0;
		}
		else if(calcavg(mid) - 0.48>0)
		{
			high = mid;
		}
		else
		{
			low = mid;
		}
		
	}
}

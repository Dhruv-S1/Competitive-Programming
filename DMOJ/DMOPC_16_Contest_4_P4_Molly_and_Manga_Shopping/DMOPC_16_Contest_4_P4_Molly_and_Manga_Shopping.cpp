#include <iostream>
#include<math.h>
#include <vector>
#include <algorithm>  
long ansarray[100005];
long dict[100005];
long a[100005];
using namespace std;

//NOTE this partial solution yeilds 30/100 points
int main() {
long x = 0;
cin>>x;
long blocksize = sqrt(x);
for(long i = 0; i<x;i++)
{
	long u = 0;
	scanf("%d", &u);
	a[i] = u;
}
long q = 0;
cin>>q;
vector <vector<long>> qarray;
for(long i = 0; i<q;i++)
{
long num1 = 0;
long num2 = 0;
cin>>num1>>num2;
vector <long> p;
p.push_back(num1/blocksize);
p.push_back(num1-1);
p.push_back(num2-1);
p.push_back(i);
qarray.push_back(p);
}
std::sort(qarray.begin(),qarray.end());
long start = qarray[0][1];
long end = start;
long count = 0;
dict[a[start]] +=1;

for(long i = 0; i<q; i++)
{
	if (start>qarray[i][1])
	{
		for(long j = start-1; j>qarray[i][1]-1;j--)
		{
		start-=1;
		dict[a[j]]+=1;
		if(dict[a[j]] == 1) count +=0;
		else if(dict[a[j]] % 2 == 0) count+=1;
		else count -=1;
		}
	}
	if (start<qarray[i][1])
	{
		for(int j = start; j<qarray[i][1];j++)
		{
			start+=1;
			dict[a[j]] -=1;
			if (dict[a[j]] == 0) count+=0;
			else if (dict[a[j]]%2 ==0) count+=1;
			else count-=1;
		}
	}
	if(end>qarray[i][2])
	{
		for(int j = end; j>qarray[i][2]; j--)
		{
			end -=1;
			dict[a[j]] -=1;
			if(dict[a[j]] == 0) count+=0;
			else if(dict[a[j]]%2 == 0) count+=1;
			else count -=1;
		}
	}
	if(end<qarray[i][2])
	{
		for(int j = end+1;j<qarray[i][2]+1;j++)
		{
			end+=1L;
			dict[a[j]] +=1L;
			if(dict[a[j]] == 1L) count+=0L;
			else if(dict[a[j]]%2 == 0L) count+=1L;
			else count-=1L;
		}
	}
	ansarray[qarray[i][3]] = count;
}
for(int i =0; i<q;i++) cout<<ansarray[i]<<endl;

}

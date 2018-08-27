#include <iostream>
#include <vector>
#include<math.h>
using namespace std;
bool total[20000006];
bool first[100006];
vector<long long> primes;

long long findnum(long long start, long long skip)
{
    if (skip>start)
    {
        return 3;
    }
    if (start%skip == 0 and (start/skip)%2 == 1)
    {
        return start/skip;
    }
    long long hold = start%skip;
    long long hold1 = start-hold+skip;
    if((hold1/skip)%2 == 1)
    {
        return hold1/skip;
    }
    else return (hold1/skip)+1;
}

int main()
{
	for(long long i = 0; i<100006; i++)
	{
		first[i] = true;
	}
	for(long long i = 0; i <20000005; i++)
	{
		total[i] = true;
	}
    long long num1, num2;
    cin>>num1;
    cin>>num2;
    long long m = sqrt(num2);
    for(long long p = 2; p*p<=m; p++)
    {
        if(first[p])
        {
            for(long long i =p*2;i<=m;i+=p) first[i] = false;
        }
    }
    for(long long i = 2; i<=m;i++)
    {
        if (first[i])
        {
            primes.push_back(i);
        }
    }
    for(long long i =0; i<primes.size();i++)
    {
        long long a = findnum(num1, primes[i]);
        for(long long j = a; primes[i]*j<=num2;j+=2)
        {
            total[j*primes[i]-num1+1] = false;
        }
    }
    long long count1 = 0;
    for(long long i =num1; i<num2;i++)
    {
        if (total[i-num1+1])
        {
            if(i%2!=0)
            {
                count1+=1;
            }
        }
    }
    cout<<count1;
}

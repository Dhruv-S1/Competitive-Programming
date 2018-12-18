#include <iostream>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
vector<long long> a1;
vector<long long> a2;
std::map<long long, long long>cache;
int main()
{
    int num1, num2 = 0;
    cin>>num1;
    cin>>num2;
    for(int i= 0; i<num1+num2; i++)
    {
        if(i<=(num1+num2)/2)
        {
            long long hold = 0;
            cin>>hold;
            if(i<=num1-1) a1.push_back(hold);
            else a1.push_back(hold*-1);
        }
        else
        {
            long long hold = 0;
            cin>>hold;
            if(i<=num1-1) a2.push_back(hold);
            else a2.push_back(hold*-1);
        }
    }
    long long count1 = 0;
    for(int i =1; i<pow(2, a1.size()); i++)
    {
        long long sum1 = 0;
        for(int j = 0; j<a1.size(); j++)
        {
            if (i&(1<<j)) sum1 += a1[j];
        }
        if (sum1 == 0) count1+=1;
        else
        {
            if(cache.find(sum1) == cache.end()) cache[sum1] = 1;
            else cache[sum1] +=1;
        }
    }
    for(int i =1; i<pow(2, a2.size()); i++)
    {
        long long sum1 = 0;
        for(int j = 0; j<a2.size(); j++)
        {
            if (i&(1<<j)) sum1 += a2[j];
        }
        if (sum1 == 0) count1+=1;
        else
        {
            if(cache.find(sum1*-1) != cache.end()) count1+=cache[sum1*-1];
        }
    }

    cout<<count1;
}

#include <iostream>
#include <cmath>
using namespace std;
long long n, k, q, hold1, hold2, level1, level2, counter = 0;


long long findlevel(long long n1)
{
    n1 = n1*(k-1)+1;
    long long tot = 1;
    for(long long i=0; i<53; i++)
    {
        tot = tot*k;
        if(tot==n1) return i;
        else if(tot>n1) return i;
    }
}


int main()
{
    cin>>n>>k>>q;
    for(long long i = 0; i<q; i++)
    {
        cin>>hold1>>hold2;
        hold1 -=1;
        hold2 -=1;
        level1 = findlevel(hold1+1);
        level2 = findlevel(hold2+1);
        counter = 0;
        if(k==1)
        {
            cout<<max(hold1-hold2, hold2-hold1)<<endl;
            continue;
        }
        if(level1>level2)
        {
            while(true)
            {
                hold1 = ceil((hold1-1)/k);
                level1-=1;
                counter+=1;
                if(level1==level2) break;
            }
        }
        else if(level2>level1)
        {
            while(true)
            {
                hold2 = ceil((hold2-1)/k);
                level2-=1;
                counter+=1;
                if(level1==level2) break;
            }
        }
        while(true)
        {
            if (hold1 == hold2)
            {
                cout<<counter<<endl;
                break;
            }
            hold1 = ceil((hold1-1)/k);
            hold2 = ceil((hold2-1)/k);
            counter+=2;
        }
    }
}

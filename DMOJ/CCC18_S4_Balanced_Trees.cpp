#include <iostream>
#include<math.h>
using namespace std;
long long x;
long long big[31624];
long long small[31624];
long long recurse(long long k)
{
    long long hold = 0;
    long long total = 0;
    if(k<sqrt(x) and small[k]!=0) return small[k];
    else if (k>sqrt(x) and big[x/k]!=0) return big[x/k];
    if(k == 1) return 1;
    for(long long i = 1; i<=floor(sqrt(k)); i++)
    {
        total+= recurse(i)*((k/i)-(k/(i+1)));
        if(i>=2 and k/i>floor(sqrt(k)))
        {
            total+=recurse(k/i);
        }

    }
    if(k<sqrt(x))
    {
        small[k] = total;
    }
    else big[x/k] = total;
    return total;
}



int main()
{
    cin>>x;

    cout<<recurse(x)<<endl;
}

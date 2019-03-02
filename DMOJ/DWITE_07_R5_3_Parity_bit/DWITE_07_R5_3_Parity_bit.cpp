#include <iostream>

using namespace std;
long long x, count1;

int main()
{
    for(int i = 0; i<5; i++)
    {
        cin>>x;
        count1 = 0;
        while(x!=0)
        {
            if(x%2 == 1) count1++;
            if(x == 1)break;
            x = x/2;
        }
        if(count1%2 == 0) cout<<0<<endl;
        else cout<<1<<endl;
    }
}

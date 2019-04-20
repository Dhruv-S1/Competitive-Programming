#include <iostream>

using namespace std;

long long a[102], b[102];
long long h1, h2 = 0;
long long p1 = 1;
long long p2 = 100;
long long save = 101;
long long hold1, hold2, n, hold3, hold4 = 999999999;
long long marker, marker1 = 0;
long long current_max = 0;
int main()
{
    cin>>n;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold3>>hold4;
        a[hold3]+=1;
        b[hold4]+=1;
        hold1 = a[p1];
        hold2 = b[p2];
        while(true)
        {
            if(p1>100 or p2<1) break;
            if(a[p1]!=0 and b[p2]!=0)
            {
                if(p1+p2>current_max) current_max = p1+p2;
            }
            h1 = hold1 - hold2;
            h2 = hold2 - hold1;
            hold1 = max(0LL, h1);
            hold2 = max(0LL, h2);
            if(hold1 == 0 and hold2!=0)
            {
                p1+=1;
                hold1 = a[p1];
            }
            else if(hold2 == 0 and hold1!=0)
            {
                p2-=1;
                hold2 = b[p2];
            }
            else
            {
                p1+=1;
                p2-=1;
                hold1 = a[p1];
                hold2 = b[p2];
            }

        }
        cout<<current_max<<endl;
        p1 = 1;
        p2 = 100;
        current_max = 0;
        hold1, hold2 = 99999999;

    }
}

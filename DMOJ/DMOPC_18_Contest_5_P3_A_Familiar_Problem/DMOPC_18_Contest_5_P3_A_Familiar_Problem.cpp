#include <iostream>

using namespace std;
long long n, m, hold1, total, longest;
long long a[2000001];
int main()
{
    cin>>n>>m;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold1;
        a[i] = hold1;
    }

    long long i = 0;
    long long j = 0;
    total = 0;
    longest = 0;
    while(true)
    {
        total +=a[j];
        if(total>=m)
        {
            if(i == j and j!=n-1)
            {
                while(true)
                {
                    total -=a[i];
                    i+=1;
                    j+=1;
                    total+=a[i];
                    if(total<m or j==n-1) break;
                }
            }
            else
            {
                while(i!=j)
                {
                    total-=a[i];
                    i+=1;
                    if(total<m or i ==n-1) break;
                }
            }
        }
        if((j-i+1)>longest and total<m) longest = j-i+1;
        j+=1;
        if(j == n) break;
    }

    cout<<longest<<endl;
}

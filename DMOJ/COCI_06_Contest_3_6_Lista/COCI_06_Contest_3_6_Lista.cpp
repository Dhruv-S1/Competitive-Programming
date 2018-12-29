#include <iostream>
long long n, m, x, y, u, current, mid, final2;
char operation;
using namespace std;
long long b[500002];
long long M[500002];
struct node
{
    long long left;
    long long right;
}a[500002];

// NOTE: This partial solution gives 42/90 points

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for(long long i = 0; i<150001; i++)
    {
        a[i].left = i-1;
        a[i].right = i+1;
    }
    for(long long i = 0; i<m; i++)
    {
        cin>>operation>>x>>y;
        a[a[x].right].left = a[x].left;
        a[a[x].left].right = a[x].right;
        if(operation == 'A')
        {
            a[x].left = a[y].left;
            a[a[y].left].right = x;
            a[y].left = x;
            a[x].right = y;
        }
        else
        {
            a[x].left = y;
            a[a[y].right].left = x;
            a[x].right = a[y].right;
            a[y].right = x;
        }
    }
    for(long long i = 0; i<500002; i++)
    {
        if (a[i].left ==0)
        {
            u = i;
            break;
        }
    }
    long long index = 0;
    while(true)
    {
        b[index] = u;
        u = a[u].right;
        index+=1;
        if(index>500001) break;
    }
    for(long long i = 0; i<500002; i++) M[i] = 999999;
    M[0] = 0;
    for(long long i = 0; i<n; i++)
    {
    long long start = 0;
    long long head = n;
    while(true)
    {
        mid = (start+head)/2;
        if(head-start == 1)
        {
            if(M[start]>b[i]) break;
            else
            {
                if (M[head]<b[i])
                {
                    M[head+1] = b[i];
                }
                else M[start+1] = b[i];
                break;
            }
        }
        if(M[mid]<b[i])
        {
            start = mid;
        }
        if(M[mid]>b[i])
        {
            head = mid;
        }
    }
    }

for(long long i = 1; i<500002; i++)
{
    if(M[i]!=999999)final2+=1;
}
cout<<n-final2<<endl;



}

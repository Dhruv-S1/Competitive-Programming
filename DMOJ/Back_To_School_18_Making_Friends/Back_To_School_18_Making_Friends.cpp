#include <iostream>
#include <queue>
using namespace std;
long long n, m, hold1, total;
priority_queue<long long> a;
int main()
{
    cin>>n>>m;
    for(long long i = 0; i<n; i++)
    {
        cin>>hold1;
        a.push(hold1);
    }
    for(long long i = 0; i<m; i++)
    {
        hold1 = a.top();
        a.pop();
        total +=hold1;
        if(hold1!=0)
        {
            hold1-=1;
            a.push(hold1);
        }
        else a.push(hold1);
    }

    cout<<total<<endl;
}

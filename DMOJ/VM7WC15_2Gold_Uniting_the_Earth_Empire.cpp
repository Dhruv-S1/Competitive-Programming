#include <iostream>
#include <stack>
using namespace std;
long long a[400001];
long long n, hold1, total, marker, marker1;
stack<pair<long long, long long> > s;
int main()
{
 cin>>n;

 for(long long i = 0; i<n;i++)
 {
     cin>>hold1;
     a[i] = hold1;
 }
 s.push(make_pair(a[0], 0));
 for(long long i = 1; i<n;i++)
 {
     marker1 = 0;
     if(a[i]>=s.top().first)
     {
         while(a[i]>=s.top().first)
         {
             if (a[i] == s.top().first)
             {
                 marker1 = s.top().second+1;
                 total +=s.top().second+1;
                 s.pop();
             }
             else
             {
                 total+=s.top().second+1;
                 s.pop();
             }
            if(s.size()==0)
            {
                marker = 1;
                break;
            }
         }

         if(marker!=1)total+=1;
     }
    else
    {
        if(s.size()!=0)total+=1;
    }
    s.push(make_pair(a[i], marker1));
    marker = 0;
 }
 cout<<total<<endl;
}

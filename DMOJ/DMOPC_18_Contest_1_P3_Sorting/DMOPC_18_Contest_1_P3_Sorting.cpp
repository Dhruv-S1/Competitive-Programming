#include <iostream>
#include<set>
#include<vector>

//NOTE this partial solution only yields 60/100 points.

using namespace std;
int  n, m, t, j, hold1;
int a[202];
int c[202];
int d2[202];
bool ch1;
vector<long long> d;
set<int> b;
set<int> temp;
int main()
{
    cin>>n;
    for(int i =1; i<n+1; i++)
    {
        cin>>hold1;
        a[i] = hold1;
    }
    long long fir = 0;
    for(int i = 1; i<n+1; i++)
    {
        temp.clear();
        if(b.find(a[i])== b.end())
        {
            if(i==a[i]) continue;
            if(t!=0) d2[i] = t;
            t = a[i];
            j = i;
            d.push_back(j);
            if(fir ==0) fir =i;
            while(true)
            {
                temp.insert(j);
                b.insert(j);
                if(temp.find(a[j])!=temp.end() or j>n) break;

                d.push_back(t);
                c[j] = t;
                t = a[a[j]];
                j=a[j];
            }
        }
        if(i == n) d2[fir] = t;
    }
    int counter = 0;
    for(int i = 0; i<202; i++)
    {
        if(d2[i]!=0)
        {
            counter +=1;
            ch1 = 1;
        }
    }
    if(d.size()==0 and !ch1)
    {
        cout<<0<<endl;
        return 0;
    }
    if(d.size()!=0 and !ch1)cout<<1<<endl;
    else cout<<2<<endl;
    for(int i = 0; i<d.size(); i++)
    {
        if(i==0) cout<<d.size()<<" ";
        cout<<d[i]<<" ";
    }
    cout<<""<<endl;
    if(ch1)
    {
        cout<<counter<<" ";
        for(int i = 0; i<202; i++)
        {
            if(d2[i]!=0) j = i;
        }
        long long fir1 = j;
        cout<<j<< " ";
        while(true)
        {
            j = d2[j];
            if(j==fir1) break;
            cout<<j<<" ";
        }
    }

}

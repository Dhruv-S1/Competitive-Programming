#include <iostream>
#include <vector>
#include<algorithm>
#include<math.h>
using namespace std;
vector<long long> a;
long long segtree[3000005][4];

//NOTE: This partial solution only gives 65/100 points

long long findmax(long long num1, long long num2,long long num3,long long num4)
{
    int curmax = num1;
    if (num2>curmax) curmax = num2;
    if(num3> curmax) curmax = num3;
    if(num4>curmax) curmax = num4;
    return curmax;
}

void buildtree(long long curlow, long long curhigh, long long pos)
{
    if (curhigh == curlow)
    {
        segtree[pos][0] = a[curhigh];
        segtree[pos][1] = a[curhigh];
        segtree[pos][2] = a[curhigh];
        segtree[pos][3] = a[curhigh];
    }
    else
    {
    long long mid = (curlow+curhigh)/2;
    buildtree(curlow, mid, pos*2+1);
    buildtree(mid+1, curhigh, pos*2+2);
    segtree[pos][0] = findmax(segtree[pos*2+1][0], segtree[pos*2+1][3]+segtree[pos*2+2][3],segtree[pos*2+1][3]+segtree[pos*2+2][0], segtree[pos*2+1][3]);
    segtree[pos][1] = findmax(segtree[pos*2+2][1], segtree[pos*2+1][3]+segtree[pos*2+2][3],segtree[pos*2+2][3]+segtree[pos*2+1][1], segtree[pos*2+2][3]);
    segtree[pos][2] = findmax(segtree[pos*2+1][2], segtree[pos*2+2][2], segtree[pos*2+1][1]+segtree[pos*2+2][0], segtree[pos*2+2][3]);
    segtree[pos][3] = segtree[pos*2+1][3]+segtree[pos*2+2][3];
    }

}
long long findpos(long long curleft, long long curight,long long pos,long long val)
{
    if (curleft == curight && curight == val)
        return pos;
    long long mid = (curleft+curight)/2;

    if (val<=mid)
    {
        return findpos(curleft, mid, pos*2+1, val);
    }
    else
    {
        return findpos(mid+1, curight, pos*2+2, val);
    }
}
void update1(long long t)
{
    segtree[t][0] = findmax(segtree[t*2+1][0], segtree[t*2+1][3]+segtree[t*2+2][3],segtree[t*2+1][3]+segtree[t*2+2][0], segtree[t*2+1][3]);
    segtree[t][1] = findmax(segtree[t*2+2][1], segtree[t*2+1][3]+segtree[t*2+2][3],segtree[t*2+2][3]+segtree[t*2+1][1], segtree[t*2+2][3]);
    segtree[t][2] = findmax(segtree[t*2+1][2], segtree[t*2+2][2], segtree[t*2+1][1]+segtree[t*2+2][0], segtree[t*2+2][3]);
    segtree[t][3] = segtree[t*2+1][3]+segtree[t*2+2][3];
    if (t <= 0) return;
    if (t%2==0) t = (t/2)-1;
    else t = (t-1)/2;
    update1(t);
}

int main()
{
    long long x;
    cin>>x;
    for(int i = 0; i<x; i++)
    {
        long long y = 0;
        cin>>y;
        a.push_back(y);
    }
    buildtree(0, a.size()-1, 0);
    cout<<segtree[0][2]<<endl;
    long long y;
    cin>>y;
    for(int i = 0; i<y; i++)
    {
        long long num1, num2;
        cin>>num1;
        cin>>num2;
        long long t = findpos(0, a.size()-1, 0, num1);
        segtree[t][0] = num2;
        segtree[t][1] = num2;
        segtree[t][2] = num2;
        segtree[t][3] = num2;
        if (t%2==0) t = (t/2)-1;
        else t = (t-1)/2;
        update1(t);
        cout<<segtree[0][2]<<endl;


    }


}

#include <iostream>
#include<bitset>
#include<deque>
#include<unordered_map>
using namespace std;
long long n, q, hold, hold1, hold2;
bitset<1001> seg[400001];
bitset<1001> a1;
long long a[100001];
unordered_map<long long, pair<long long, long long> > b;
deque<long long> numbers;
void build(long long left, long long right, long long cur)
{
    if(left == right)
    {
        if (a[left] != 0)
        {
            seg[cur].set(b[a[left]].second);
        }
        return;
    }
    long long mid = (left+right)/2;
    build(left, mid, cur*2+1);
    build(mid+1, right, cur*2+2);
    seg[cur] = seg[cur*2+1] | seg[cur*2+2];
}

bitset<1001> query(long long left, long long right, long long curleft, long long curright, long long cur)
{
    if(left == curleft and right == curright) return seg[cur];
    long long mid = (curright+curleft)/2;
    if(right<=mid) return query(left, right, curleft, mid, cur*2+1);
    if(left>mid) return query(left, right, mid+1, curright, cur*2+2);
    return query(left, mid, curleft, mid, cur*2+1) | query(mid+1, right, mid+1, curright, cur*2+2);
}

void update(long long curleft, long long curright, long long updatepos,long long updateval, long long cur)
{
    long long mid = (curleft+curright)/2;
    if(curleft == curright and curleft == updatepos)
    {
        seg[cur].reset();
        seg[cur].set(updateval);
        return;
    }
    if(mid<updatepos) update(mid+1, curright, updatepos, updateval, cur*2+2);
    else if(mid>=updatepos) update(curleft, mid, updatepos, updateval, cur*2+1);

    seg[cur] = seg[cur*2+1] | seg[cur*2+2];
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>q;
    for(long long i = 1; i<=1000; i++)
    {
        numbers.push_back(i);
    }

    for(long long i = 0; i<n; i++)
    {
        cin>>hold;
        a[i] = hold;
        auto got = b.find(hold);
        if(got == b.end())
        {
            b[hold] = {1, numbers.front()};
            numbers.pop_front();
        }
        else b[hold].first++;
    }
    build(0, 100001, 0);
    
    for(long long i =0; i<q; i++)
    {
        cin>>hold;
        if(hold == 1)
        {
            cin>>hold1>>hold2;
            hold1--;
            b[a[hold1]].first--;
            if(b[a[hold1]].first == 0)
            {
                numbers.push_back(b[a[hold1]].second);
            }
            a[hold1] = hold2;
            auto got = b.find(hold2);
            if(got==b.end())
            {
                b[hold2] = {1, numbers.front()};
                numbers.pop_front();
            }
            else b[hold2].first++;
            update(0, 100001, hold1, b[hold2].second, 0);
        }
        if(hold == 2)
        {
            cin>>hold1>>hold2;
            hold1--;
            hold2--;
            cout<<query(hold1, hold2, 0, 100001, 0).count()<<endl;
        }
        
    }

}

#include <iostream>
#include<math.h>
using namespace std;
long long a[2097153];
long long b[1048578];
long long n, m, hold1, hold2;
char W;
void dfs(long long cur)
{
    if(a[cur*2+1] !=0 and a[cur*2+2]!=0)
    {
        if(b[a[cur*2+1]] > b[a[cur*2+2]]) a[cur] = a[cur*2+1];
        else a[cur] = a[cur*2+2];
        return;
    }
    if(a[cur*2+1]==0)
    {
        dfs(cur*2+1);
    }
    if(a[cur*2+2] == 0)
    {
        dfs(cur*2+2);
    }
    if(b[a[cur*2+1]] > b[a[cur*2+2]]) a[cur] = a[cur*2+1];
    else a[cur] = a[cur*2+2];
}

void tourney_add(long long cur)
{
    if(cur == 0)
    {
        if(b[a[cur*2+1]] > b[a[cur*2+2]]) a[cur] = a[cur*2+1];
        else a[cur] = a[cur*2+2];
        return;
    }
    if(b[a[cur*2+1]] > b[a[cur*2+2]]) a[cur] = a[cur*2+1];
    else a[cur] = a[cur*2+2];
    if(cur%2 == 0) tourney_add((cur/2)-1);
    else tourney_add(((cur+1)/2)-1);
}

long long tourney_won(long long pos, long long winner, long long count1)
{
    if(pos==0)
    {
       if(a[pos] == winner)
          {
            return count1+1;
          }
       else
          return count1;
    }
    if(a[pos] == winner)
    {
        if(pos%2 == 0) tourney_won((pos/2)-1, winner, count1+1);
        else if(pos%2 ==1) tourney_won(((pos+1)/2)-1, winner, count1+1);
    }
    else
        return count1;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    for(long long i = 1; i<=int(pow(2,n));i++)
    {
        cin>>hold1;
        b[i] = hold1;
        a[int((pow(2, n+1)-2-(pow(2, n)-i)))] = i;
    }
    dfs(0);
    for(long long i = 0; i<m;i++)
    {
        cin>>W;
        if(W == 'W') cout<<a[0]<<endl;
        if(W == 'S')
        {
            cin>>hold1;
            if(int((pow(2, n+1)-2-(pow(2, n)-hold1)))%2==0) cout<<tourney_won(int((pow(2, n+1)-2-(pow(2, n)-hold1))/2)-1, hold1, 0)<<endl;
            else cout<<tourney_won(int(((pow(2, n+1)-2-(pow(2, n)-hold1))+1)/2)-1, hold1, 0)<<endl;

        }
        if(W == 'R')
        {
            cin>>hold1>>hold2;
            b[hold1] = hold2;
            if(int((pow(2, n+1)-2-(pow(2, n)-hold1)))%2==0) tourney_add(int((pow(2, n+1)-2-(pow(2, n)-hold1))/2)-1);
            else tourney_add(int(((pow(2, n+1)-2-(pow(2, n)-hold1))+1)/2)-1);
        }
    }


}

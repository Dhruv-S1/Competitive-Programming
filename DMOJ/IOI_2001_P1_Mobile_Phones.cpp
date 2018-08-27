#include <iostream>
using namespace std;
int BIT[1025][1025];
int ASIZE, num1, num2, num3, num4, num5, i, j;
void update(int x, int y, int val)
{
    for(int i = x; i<=ASIZE;i+=(i&-i))
    {
        for(int j = y; j<=ASIZE;j+=(j&-j))
        {
            BIT[i][j] +=val;
        }
    }
}


int query(int x, int y)
{
    int sum = 0;
    for(int i = x;i>0;i-=(i&-i))
    {
        for(int j = y;j>0;j-=(j&-j))
        {
            sum+=BIT[i][j];
        }
    }
    return sum;

}

// lesson learned, watch out for what variables I am using for query, debug time around 2 hours... Also for loop works for BIT while loop not needed.
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int hold = 0;
    cin>>hold;
    cin>>ASIZE;
    while(true)
    {
        cin>>num1;
        if(num1 == 1)
        {
            cin>>num2;
            cin>>num3;
            cin>>num4;
            update(num2+1, num3+1, num4);
        }
        if(num1 == 2)
        {
            cin>>num2;
            cin>>num3;
            cin>>num4;
            cin>>num5;
            cout<<query(num4+1, num5+1)-query(num4+1, num3)-query(num2, num5+1)+query(num2, num3)<<endl;
        }
        if(num1 == 3) break;
    }
}

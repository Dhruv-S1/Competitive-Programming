#include <iostream>
using namespace std;
long long BIT[251][251][251];
long long ASIZE, num1, num2, num3, num4, num5, i, j, q, x1, y1, z1, x2, y2, z2;
char hold;
void update(long long x, long long y,long long z, long long val)
{
    for(long long i = x; i<=ASIZE;i+=(i&-i))
    {
        for(long long j = y; j<=ASIZE;j+=(j&-j))
        {
            for(long long k = z; k<=ASIZE;k+=(k&-k))
            {
                BIT[i][j][k]+=val;
            }
        }
    }
}


long long query(long long x, long long y, long long z)
{
    long long sum = 0;
    for(long long i = x;i>0;i-=(i&-i))
    {
        for(long long j = y;j>0;j-=(j&-j))
        {
            for(long long k = z; k>0; k-=(k&-k))
            {
                sum+=BIT[i][j][k];
            }
        }
    }
    return sum;

}


int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>ASIZE;
    cin>>q;
    long long finalans = 0;
    for(long long u = 0; u<q; u++)
    {
        cin>>hold;
        if (hold == 'C')
        {
            cin>>num1>>num2>>num3>>num4;
            update(num1, num2, num3,-1*(query(num1, num2, num3)-query(num1-1, num2,num3)-query(num1, num2-1, num3) + query(num1-1, num2-1, num3)-query(num1, num2, num3-1)+query(num1-1, num2, num3-1)+query(num1, num2-1, num3-1)-query(num1-1, num2-1, num3-1)));
            update(num1, num2, num3, num4);
        }
        if (hold == 'S')
        {
            cin>>x1>>y1>>z1>>x2>>y2>>z2;
            finalans += query(x2, y2, z2)-query(x1-1, y2,z2)-query(x2, y1-1, z2) + query(x1-1, y1-1, z2)-query(x2, y2, z1-1)+query(x1-1, y2, z1-1)+query(x2, y1-1, z1-1)-query(x1-1, y1-1, z1-1);
        }
    }
    cout<<finalans<<endl;



}

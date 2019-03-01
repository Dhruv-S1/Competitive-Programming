#include <iostream>
#include <algorithm>
using namespace std;
long long x, y, z, hold1, hold2, hold3, r, c, r1, c1;
long long a[1025][1025], b[1025][1025], d[1025][1025], col[1025];
long long small, smallr, smallc = 99999999999999;
long long large, larger, largec = -9999999999999;
long long total = 0;
//NOTE this partial solution yields 50/100 points

int main()
{
    for(long long i = 0; i<1024; i++) 
    {
        for(long long j = 0; j<1024; j++)
        {
            d[i][j] = 0;
        }
    }
    cin>>x;
    cin>>r>>c;
    for(long long i = 0; i<r;i++)
    {
        for(long long j = 0; j<c;j++)
        {
            cin>>hold1;
            a[i][j] = hold1;
        }
    }
    long long count1 = 0;
    while(true)
    {
        count1 +=1;
        cin>>r1>>c1;
        for(long long i = 0; i<r1;i++)
        {
            for(long long j = 0; j<c1;j++)
            {
                cin>>hold1;
                b[i][j] = hold1;
            }
        }
        for(long long i = 0; i<r; i++)
        {
            for(long long j = 0; j<c; j++)
            {
                for(long long k = 0; k<r1; k++)
                {
                    for(long long l = 0; l<c1; l++)
                    {
                        d[i*r1+k][j*c1+l] = a[i][j]*b[k][l];
                    }
                }
            }
        }
        for(long long i = 0; i<r*r1;i++)
        {
            for(long long j = 0; j<c*c1;j++)
            {
                a[i][j] = d[i][j];
            }
        }
        r = r1*r;
        c = c1*c;
        if(count1+1 == x) break;
    }
    for(long long i =0; i<r; i++)
    {
        total = 0;
        for(long long j = 0; j<c; j++)
        {
            if (d[i][j]<small) small = d[i][j];
            if(d[i][j]>large) large = d[i][j];
            total +=d[i][j];
            col[j]+=d[i][j];
        }
        if(total>larger) larger = total;
        if(total<smallr) smallr = total;
    }
    cout<<large<<endl;
    cout<<small<<endl;
    cout<<larger<<endl;
    cout<<smallr<<endl;
    for(long long i = 0; i<c; i++)
    {
	if(col[i]>largec) largec = col[i];
	if(col[i]<smallc) smallc = col[i];
    }
    cout<<largec<<endl;
    cout<<smallc<<endl;

}

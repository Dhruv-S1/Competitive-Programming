#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;
long long hold[10];
long long y, hold1, h;
struct tips{

    long long num1;
    long long num2;
    long long num3;
};
tips h1;
vector <tips> b;

int main()
{
    for(long long l = 0; l<5; l++)
    {
        cin>>y;
        b.clear();
        for(long long i = 0; i<y; i++)
        {
            for(long long j = 1; j<12; j++)
            {
                cin>>hold1;
                hold[j] = hold1;
            }

            for(long long j = hold[10]; j<=hold[11]; j++)
            {
                h1.num1 = hold[1]*pow(j, 2)+hold[2]*j+hold[3];
                h1.num2 = hold[4]*pow(j, 2)+hold[5]*j+hold[6];
                h1.num3 = hold[7]*pow(j, 2)+hold[8]*j+hold[9];
                b.push_back(h1);
            }
        }

        long long x = -99999999;
        long long x1 = 99999999;
        long long x2 = -99999999;
        long long x3 = 99999999;
        long long x4 = -99999999;
        long long x5 = 99999999;
        long long x6 = -99999999;
        long long x7 = 99999999;
        long long x8 = -99999999;
        long long x9 = 99999999;
        long long x10 = -99999999;
        long long x11 = 99999999;
        long long x12 = -99999999;
        long long x13 = 99999999;
        long long x14 = -99999999;
        long long x15 = 99999999;
        for(long long i = 0; i<b.size(); i++)
         {
           if(b[i].num1+b[i].num2+b[i].num3>x)  x = b[i].num1+b[i].num2+b[i].num3;
           if(b[i].num1+b[i].num2+b[i].num3<x1) x1 = b[i].num1+b[i].num2+b[i].num3;
           if(b[i].num1+b[i].num2-b[i].num3>x2) x2 = b[i].num1+b[i].num2-b[i].num3;
           if(b[i].num1+b[i].num2-b[i].num3<x3) x3 = b[i].num1+b[i].num2-b[i].num3;
           if(b[i].num1-b[i].num2+b[i].num3>x4) x4 = b[i].num1-b[i].num2+b[i].num3;
           if(b[i].num1-b[i].num2+b[i].num3<x5) x5 = b[i].num1-b[i].num2+b[i].num3;
           if(b[i].num1-b[i].num2-b[i].num3>x6) x6 = b[i].num1-b[i].num2-b[i].num3;
           if(b[i].num1-b[i].num2-b[i].num3<x7) x7 = b[i].num1-b[i].num2-b[i].num3;
           if(-b[i].num1+b[i].num2+b[i].num3>x8) x8 = -b[i].num1+b[i].num2+b[i].num3;
           if(-b[i].num1+b[i].num2+b[i].num3<x9) x9 = -b[i].num1+b[i].num2+b[i].num3;
           if(-b[i].num1+b[i].num2-b[i].num3>x10) x10 =-b[i].num1+b[i].num2-b[i].num3;
           if(-b[i].num1+b[i].num2-b[i].num3<x11) x11 = -b[i].num1+b[i].num2-b[i].num3;
           if(-b[i].num1-b[i].num2+b[i].num3>x12) x12 = -b[i].num1-b[i].num2+b[i].num3;
           if(-b[i].num1-b[i].num2+b[i].num3<x13) x13 = -b[i].num1-b[i].num2+b[i].num3;
           if(-b[i].num1-b[i].num2-b[i].num3>x14) x14 = -b[i].num1-b[i].num2-b[i].num3;
           if(-b[i].num1-b[i].num2-b[i].num3<x15) x15 = -b[i].num1-b[i].num2-b[i].num3;
        }
        long long a[9];
        a[0] = x-x1;
        a[1] = x2-x3;
        a[2] = x4-x5;
        a[3] = x6- x7;
        a[4] = x8-x9;
        a[5] = x10-x11;
        a[6] = x12-x13;
        a[7] = x14-x15;
        long long big = 0;
        for(long long i = 0; i<8; i++)
        {
            if(a[i]>big) big = a[i];
        }
        cout<<big<<endl;

}
}

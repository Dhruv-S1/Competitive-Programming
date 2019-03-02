#include <iostream>
#include<iomanip>
using namespace std;
long long x, y;

int main()
{
    cin>>x>>y;
    if(x*y%2 == 0) cout<<x*y/2<<".0"<<endl;
    else if(x == 1 and y == 1) cout<<0.5<<endl;
    else cout<<x*y/2<<".5"<<endl;
}

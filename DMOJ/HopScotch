#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
vector<long long>next1;
vector<long long>vals;
vector<long long>turns;
long long n, q, hold,hold1, total;

void update(long long number, long long SQRT)
{
    for(long long i = min(number*SQRT, n-1); i>=max(0LL, (number-1)*SQRT); i--)
        {
            if(i+vals[i]>=min((number*SQRT), n))
            {
                next1[i] = min(i+vals[i], n);
                turns[i] = 1;
            }
            else
            {
                next1[i] =min(next1[min(i+vals[i], n)], n);
                turns[i] = turns[min(i+vals[i], n)]+1;
            }
        }
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    const long long SQRT = (int)ceil(sqrt((double)n));
    for(long long i = 0; i<n;i++)
    {
        cin>>hold;
        vals.push_back(hold);
        next1.push_back(0);
        turns.push_back(0);
    }
    cin>>q;
    for(long long i = 1; i<=SQRT; i++) update(i, SQRT);


    for(long long i = 0; i<q;i++)
    {
        cin>>hold;
        if(hold ==1)
        {
            total = 0;
            cin>>hold;
            while(hold<n)
            {
                total+=turns[hold];
                hold = next1[hold];
            }
            cout<<total<<endl;
        }
        if(hold == 2)
        {
            cin>>hold;
            cin>>hold1;
            vals[hold] = hold1;
            update((long long)ceil((hold)/(double)SQRT), SQRT);
        }
    }
}

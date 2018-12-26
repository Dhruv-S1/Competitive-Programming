#include <iostream>
#include <stack>
using namespace std;
long long n, k, hold1, start, total;
bool chair[1000001];
bool student[1000001];
bool chair_visited[1000001];
bool student_sat[1000001];
long long studentmap[1000001];
stack<long long> current_chairs;
int main()
{
    cin>>n>>k;
    for(long long i = 0; i<k; i++)
    {
        cin>>hold1;
        chair[hold1] = 1;
        start = hold1;
    }
    for(long long i = 0; i<k+1; i++)
    {
        cin>>hold1;
        student[hold1] = 1;
        studentmap[hold1] = i+1;
    }
    while(true)
    {
        if(total==k) break;

        if(!chair_visited[start] && chair[start])
        {
            current_chairs.push(start);
            chair_visited[start] = 1;
        }
        if(student[start] && !student_sat[start])
        {
            if(current_chairs.size()>0)
            {
                current_chairs.pop();
                student_sat[start] = 1;
                total+=1;
            }
        }
        start-=1;
        if(start == 0) start = n;
    }
    for(long long i = 1; i<=n; i++)
    {
        if(student[i] && !student_sat[i]) cout<<studentmap[i]<<endl;
    }
}

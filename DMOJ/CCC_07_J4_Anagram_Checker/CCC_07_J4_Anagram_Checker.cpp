#include <iostream>
#include <map>
#include <string>
using namespace std;
map<char, int> one;
map<char, int> two;
string k, l;
string alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int main()
{
    getline(cin, k);
    for(long long i = 0; i<alp.size(); i++)
    {
        one[alp[i]] = 0;
        two[alp[i]] = 0;
    }
    for(long long i = 0; i<k.size(); i++)
    {
        if(k[i]!=' ')
        {
            if(one.find(k[i])==one.end()) one[k[i]] = 1;
            else one[k[i]] +=1;
        }
    }
    getline(cin, k);
    for(long long i = 0; i<k.size(); i++)
    {
        if(k[i]!=' ')
        {
            if(one.find(k[i])==two.end()) two[k[i]] = 1;
            else two[k[i]] +=1;
        }
    }
    for(long long i = 0; i<alp.size(); i++)
    {
        if(one[alp[i]] != two[alp[i]])
        {
            cout<<"Is not an anagram."<<endl;
            return 0;
        }
    }
    cout<<"Is an anagram."<<endl;



}

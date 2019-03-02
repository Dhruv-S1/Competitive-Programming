#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
using namespace std;

int main()
{
    for(long long u = 0; u<10; u++)
    {
        string s, hold1, eod;
        long long c2 = 0;
        vector<long long> si;
        vector<string> in;
        cin>>eod;
        cin.ignore();
        getline(cin, s);

        for(long long i = 0; i<s.size(); i++)
        {
            if (s[i] == ' ')
            {
                in.push_back(hold1);
                hold1.erase();
            }
            else hold1 = hold1+s[i];
        }
        in.push_back(hold1);
        for(long long i = 0; i<in.size(); i++)
        {
            si.push_back(in[i].size());
        }
        if(eod == "encode")
        {
            string n;
            long long count1 = 0;
            long long mark;
            while(true)
            {
                count1+=1;
                mark = 0;
                for(long long i = 0; i<in.size(); i++)
                {
                    if(si[i]>=count1)
                    {
                        mark = 1;
                        n = n+in[i][count1-1];
                    }
                }
                if(mark == 0) break;

            }
            string fin;
            count1 = 0;
            for(long long i = 0; i<n.size(); i++)
            {
                fin = fin + n[i];
                c2 +=1;
                if(c2 == si[count1])
                {
                    fin = fin + ' ';
                    count1 +=1;
                    c2 = 0;
                }
            }
            cout<<fin<<endl;
        }

        if(eod == "decode")
        {
            string a[si.size()];
            long long totalcount = 0;
            for(long long i = 0; i<si.size(); i++)
            {
                for(long long j = 0; j<in[i].size(); j++)
                {
                    if(a[totalcount%si.size()].size()<si[totalcount%si.size()])
                    {
                        a[totalcount%si.size()] += in[i][j];
                    }
                    else
                    {
                        long long k = totalcount;
                        while (true)
                        {
                            k+=1;
                            if(a[k%si.size()].size()<si[k%si.size()])
                            {
                                a[k%si.size()] += in[i][j];
                                break;
                            }
                        }
                        totalcount = k;
                    }
                    totalcount+=1;
                }
            }
            for(long long i = 0; i<si.size()-1; i++)
            {
                cout<<a[i]<<" ";
            }
            cout<<a[si.size()-1]<<endl;

        }
    }

}

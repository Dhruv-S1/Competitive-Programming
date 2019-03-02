#include <iostream>
#include <map>
#include <vector>
#include<math.h>
using namespace std;
long long n, k, hold1, total1, hold2;
map<long long, vector<long long> >pic2;
map<long long, vector<long long> >pic3;
map<long long, vector<long long> >pic4;
map<long long, vector<long long> >pic5;
map<long long, vector<long long> >pic7;
long long b[37];
long long vis[100];

//NOTE this parial solution yields 55/120 points

long long check(map<long long, vector<long long> > a, long long nodes)
{
	long long marker = 0;
	for(long long i = 1; i<=nodes; i++)
	{
		for(long long j = 0; j<a[i].size(); j++)
		if(b[i]==b[a[i][j]]) marker = 1;
	}
	if(!marker) return 1;
	else return 0;
}

long long colour_graph(long long node, long long y, map<long long, vector<long long> > a, long long nodes)
{
	for(long long i = 1; i<=y; i++)
	{
		b[node] = i;
		if(node == nodes) 
		{
			if(check(a, nodes)) total1+=1;
			continue;
		}
		colour_graph(node+1, y, a, nodes);
		
	}

}



long long choose(long long y, long long r)
{
    if(r>y) return 0;
    if(r ==2) return(((y)*(y-1))/2);
    if(r==3) return(((y)*(y-1)*(y-2))/6);
    
}
int main()
{
for(long long i = 0; i<35; i++)
{
   b[i]=0;
}
    cin>>n>>k;

    if(n == 1)
    {
        cout<<choose(k ,3)*3*pow(2, 19)+choose(k,2)*2<<endl;
    }
    if(n == 2)
    {
        pic2[1].push_back(2);
        pic2[2].push_back(1);
        for(long long i = 3; i<=6; i++) pic2[2].push_back(i);
        pic2[3].push_back(2);
        pic2[3].push_back(4);
        pic2[4].push_back(2);
        pic2[4].push_back(2);
        pic2[5].push_back(6);
        pic2[5].push_back(2);
        pic2[6].push_back(5);
        pic2[6].push_back(2);
        pic2[7].push_back(8);
        pic2[7].push_back(2);
        pic2[8].push_back(7);
        colour_graph(1, 3, pic2, 8);
        cout<<total1*choose(k, 3)<<endl;
    }
    if(n == 3)
    {
        pic3[1].push_back(2);
        pic3[2].push_back(1);
        pic3[2].push_back(3);
        pic3[2].push_back(4);
        pic3[3].push_back(2);
        pic3[4].push_back(2);
        colour_graph(1, 3, pic3, 4);
        hold2 = total1;
        cout<<2*choose(k, 2)+hold2*choose(k, 3)<<endl;
    }
    if(n==4)
    {
        pic4[14].push_back(13);
        pic4[13].push_back(10);
        pic4[10].push_back(11);
        pic4[10].push_back(12);
        pic4[10].push_back(6);
        pic4[10].push_back(13);
        pic4[11].push_back(10);
        pic4[12].push_back(10);
        pic4[6].push_back(9);
        pic4[6].push_back(8);
        pic4[6].push_back(7);
        pic4[6].push_back(5);
        pic4[6].push_back(10);
        pic4[9].push_back(6);
        pic4[8].push_back(6);
        pic4[7].push_back(6);
        pic4[1].push_back(6);
        pic4[1].push_back(5);
        pic4[1].push_back(4);
        pic4[1].push_back(3);
        pic4[1].push_back(2);
        pic4[5].push_back(1);
        pic4[4].push_back(1);
        pic4[3].push_back(1);
        pic4[2].push_back(1);
		colour_graph(1, 2, pic4, 14);
		hold1=total1;
		for(long long i = 0; i<35; i++)
		{
		    b[i]=0;
		    vis[i] = 0;
		}
		total1 = 0;
		colour_graph(1, 3, pic4, 14);
		hold2 = total1;
        cout<<hold1*choose(k, 2)+hold2*choose(k, 3);
    }
    if(n == 5)
    {
        pic5[1].push_back(2);
        pic5[1].push_back(3);
        pic5[2].push_back(1);
        pic5[2].push_back(3);
        pic5[3].push_back(1);
        pic5[3].push_back(2);
        pic5[3].push_back(4);
        pic5[3].push_back(5);
        pic5[4].push_back(3);
        pic5[4].push_back(5);
        pic5[5].push_back(4);
        pic5[5].push_back(3);
        colour_graph(1, 3, pic5, 5);
        cout<<total1*choose(k, 3)<<endl;

    }
    if(n == 6) cout<<1536*choose(k, 3)<<endl;

    if(n == 7)
    {
        pic7[1].push_back(2);
        pic7[2].push_back(1);
        pic7[2].push_back(3);
        pic7[2].push_back(4);
        pic7[2].push_back(5);
        pic7[2].push_back(6);
        pic7[2].push_back(7);
        pic7[7].push_back(2);
        pic7[7].push_back(8);
        pic7[8].push_back(7);
        pic7[4].push_back(3);
        pic7[4].push_back(2);
        pic7[3].push_back(4);
        pic7[3].push_back(2);
        pic7[6].push_back(2);
        pic7[6].push_back(5);
        pic7[5].push_back(6);
        pic7[5].push_back(2);
        colour_graph(1, 3, pic7, 8);
        cout<<total1*choose(k, 3)<<endl;
    }
    if(n==8) cout<<(pow(2, 30)+pow(-1, 30)*(2))*choose(k, 3)+(pow(1, 30)+pow(-1, 30)*(1))*choose(k, 2)<<endl;


}

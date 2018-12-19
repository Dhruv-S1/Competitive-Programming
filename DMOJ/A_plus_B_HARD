#include <iostream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;
// a+b HARD code.
int a[100002];
int i = 0;
int convert(char k)
{
    if (k=='0')
        return 0;
    else if (k=='1')
        return 1;
    else if (k=='2')
        return 2;
    else if (k=='3')
        return 3;
    else if (k=='4')
        return 4;
    else if (k=='5')
        return 5;
    else if (k=='6')
        return 6;
    else if (k=='7')
        return 7;
    else if (k=='8')
        return 8;
    return 9;
}
bool bigger(string num1, string num2)
{
    if (num1.length()>num2.length())
        return false;
    if (num2.length()>num1.length())
        return true;
    for(int i=num1.length()-1; i>=0;i--)
    {
        if (convert(num1[i])>convert(num2[i]))
            return false;
        if(convert(num1[i])<convert(num2[i]))
            return true;
    }
}


int add(string num1, string num2, int sign)
{
    for(int i = 0; i<100002;i++)
        a[i] = -1;

	int carry = 0, sum = 0,h = 0;
	for(int i = 0; i < num2.length(); i++)
	{
        sum = convert(num1[i]) + convert(num2[i]) + carry;
        a[i] = ((sum % 10));
        carry = sum / 10;
        h = i;
	}

	for (int j = num2.length(); j < num1.length(); j++)
	{
		sum = convert(num1[j]) + carry;
        a[j] = ((sum % 10));
        carry = sum / 10;
		h = j;
	}

	if (carry!=0)
		a[h+1] = carry;
    if (sign == 0)
            cout<<"-";
	for (int j = (sizeof(a)/sizeof(*a))-1;j>=0; j--)
	{
	    if (a[j]==0 && j ==(sizeof(a)/sizeof(*a))-1)
            continue;
        else
        {
	        if (a[j] != -1)
                cout << a[j];
        }
	}

	cout<<"\n";
	return 0;
}

int sub(string num1, string num2, int finalmark)
{
    for(int i = 0; i<100002;i++)
        a[i] = -1;
    int carry = 0, sum = 0,h = 0;
	for(int i = 0; i < num2.length(); i++)
	{
        sum = convert(num1[i]) - convert(num2[i]) - carry;
        if (sum<0)
        {
            a[i] = sum+10;
            carry = 1;
        }
        else
        {
            a[i] = sum;
            carry = 0;
        }
	}

	for (int j = num2.length(); j < num1.length(); j++)
	{
        sum = convert(num1[j]) - carry;
        if (sum<0)
        {
            a[j] = sum+10;
            carry = 1;
        }
        else
        {
            a[j] = sum;
            carry = 0;
        }
        h = j;
	}

	if (finalmark == 1)
        cout<<"-";
    int marker = 0;
	for (int j =(sizeof(a)/sizeof(*a))-1;j>=0;j--)
	{
	    if (a[j]==0 && marker == 0)
            continue;
	        if(a[j]!= -1)
	        {
                marker = 1;
		        cout << a[j];
	        }
        }

	cout<<"\n";

	return 0;
}

int main()
{
    int x = 0;
    cin>>x;
    for(int q=0;q<x;q++)
    {
        string num1;
        string num2;
        cin >> num1 >> num2;
        string num3;
        if (num1[0] == '-' && num2[0] != '-')
        {
            num3 = num1.substr(1, num1.length());
            if (num3 == num2)
            {
                cout<<0<<endl;
                continue;
            }
        }
        if(num2[0] == '-' && num1[0] != '-')
        {
            num3 = num2.substr(0, num2.length());
            if (num3 == num1)
            {
                cout<<0<<endl;
                continue;
            }
        }

        std::reverse(num1.begin(), num1.end());
        std::reverse(num2.begin(), num2.end());
        if (num2[num2.length()-1] != '-' && num1[num1.length()-1] != '-')
        {
            if (num2.length()>num1.length())
                swap(num1, num2);
            add(num1, num2, 1);
        }
        if (num2[num2.length()-1] == '-' && num1[num1.length()-1] == '-')
        {
            if (num2.length()>num1.length())
                swap(num1, num2);
            num2 = num2.substr(0, num2.size()-1);
            num1 = num1.substr(0, num1.size()-1);
            add(num1, num2, 0);
        }
        int marker = -1, marker1 = -1, marker2 = -1, finalmark = 0;
        if ((num2[num2.length()-1] == '-' && num1[num1.length()-1] != '-') || (num2[num2.length()-1] != '-' && num1[num1.length()-1] == '-'))
        {
            if ((num2[num2.length()-1]) == '-')
            {
                num2 = num2.substr(0, num2.size()-1);
                marker1= 0;
            }
            else
            {
                num1 = num1.substr(0, num1.size()-1);
                marker2= 1;
            }
            if (bigger(num1, num2))
            {
                swap(num1, num2);
                marker = 0;
            }

            if(marker == 0 and marker1 == 0)
                finalmark = 1;

            if(marker == -1 and marker2 == 1)
                finalmark = 1;

            sub(num1, num2, finalmark);
        }
    }
}

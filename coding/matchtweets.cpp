
/*
	Credits: This problem is one of the hacker rank practice + regEx problems
	HackerRank Tweets -- find in an input list of tweets -- the number of hacker rank hashtags or metinos that come up
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int numLines=0;
    std::string str;
    std::string strL = "hackerrank";
    std::string strH = "HACKERRANK";
    
    cin >> numLines;
    getline(cin, str);
    int count = 0;
    bool found;

    for (int i = 0; i < numLines; i++)
    {
        found = false;
        getline(cin, str);
        //cout << str;
        for (int j = 0; j < str.length(); j++)
        {
            if ((str[j] == strL[0]) || (str[j] == strH[0]))
            {
                if ((j + strL.length() -1) < str.length())
                {
                    //cout << "H found and verifying .. " << str << endl;
                    for (int k = 0; k < strL.length(); k++)
                    {
                        if ((str[j+k] == strL[k])||(str[j+k] == strH[k]))
                        {
                            found = true;
                        }
                        else
                        {
                            found = false;
                        }
                    }                    
                }
            }
            if (found)
            {
                break;
            }
        }
        if (found)
        {
            count ++;
            //cout << str << endl;
        }
    }
    cout << count;
    return count;
}



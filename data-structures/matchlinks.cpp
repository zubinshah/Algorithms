


/*
Detect HTML links
Credits : This problem was found at HackerRank practice tests. Here is one of the solutions that was submitted there. 
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
    int lines, link_s, link_e, name_s, name_e, count_tags=0;
    std::string str1;

    // assuming number of lines is always the first line as a numeric input
    std::cin >> lines;
    getline(cin,str1);

    for (int i = 0; i < lines; i++)
    {
        std::string str;
        std::string namestr;
        link_s = link_e = name_s = name_e = count_tags = 0;
        getline(cin, str);
        link_s = str.find("<a href=", 0);

        while (link_s != -1)
        {
            link_s = link_s + 9;
            link_e = str.find("\"", link_s);
            // Name String Search..        
            name_s = str.find(">", link_e) + 1;
            name_e = str.find("</a>", link_e);
            
            while ((name_s < name_e) && (str[name_s] == ' '))
            {
                name_s++;
            }
            namestr = str.substr(name_s, name_e-name_s);
          
            count_tags = std::count(namestr.begin(), namestr.end(), '>');
            name_s = 0;
            name_e = namestr.length();
            if (count_tags != 0)
            {
                int m1=0, m2=0;
                for (int j = 0; j < namestr.length(); j++)
                {
                    if (namestr[j] == '>')
                    {
                        m1++;
                        if (m1 == (count_tags/2))
                        {
                            name_s = j+1;
                            break;
                        }
                    }   
                }
                name_e = namestr.find("<", name_s);
            }

            cout << str.substr(link_s, link_e-link_s) << "," <<  namestr.substr(name_s, name_e-name_s) << endl;
            link_s = str.find("<a href=", link_e+name_e);
        }
        //cout << str.substr(link_s, link_e-link_s) << "," <<  namestr.substr(name_s, name_e-name_s) << endl;
    }
    return 0;
}
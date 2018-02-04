/******************************************************************************
C program to reverse a string input from the console
        #1 - reverse a given string (with or without string libs
        #2 - reverse a string with markers \r\n


 Test inputs : this command will compile, as well as execute on a linux command
                line 
      --> gcc string_reverse.c && ./a.out 'zubinzubinzubin1234zefksljkl

******************************************************************************/


#include <stdio.h>
#include <stdlib.h>

char *strrev(char* s)
{
    int len=0, i, j;
    char temp;
    while (s[len] != 0)
    {
        len++;
    }

    i = 0;
    j = len-1;
    while (i < j)
    {
        temp = s[j];
        s[j] = s[i];
        s[i] = temp;
        i++;
        j--;
    }
    return s;

    //1. dont use a new string to reverse
    //2. dont use extra space, as a library function it isn't optimized
    //3. compromize a bit on time -to find end of string, or use strlen for len
}

char *strrev2(char* s)
{
    int len=0, i, j;
    char chari, chari1;
    while (s[len] != 0)
    {
        len++;
    }
    i = 0;
    j = len-1;
    while (i < j)
    {
        chari = s[i];
        if (s[i] == '\r' && s[i+1] == '\n')
        {
            chari1 = s[i+1];
            if (s[j] == '\n' && s[j-1] == '\r')
            {
                s[i] = s[j-1];
                s[i+1] = s[j];
                s[j-1] = chari;
                s[j] = chari1;
                i+=2;
                j-=2;
            }
            else
            {
                s[i] = s[j];
                s[i+1] = s[j-1];
                s[j-1] = chari1;
                s[j] = chari;
                i+=2;
                j-=2;
            }
        }
        else if (s[j] == '\n' && s[j-1] == '\r')
        {
            chari1 = s[i+1];
            s[i] = s[j-1];
            s[i+1] = s[j];
            s[j-1] = chari1;
            s[j] = chari;
            i+=2;
            j-=2;
        }
        else
        {
            s[i] = s[j];
            s[j] = chari;
            i++;
            j--;
        }
    }
    return s;
}

int main (int argc, char **argv)
{
    char *str = argv[1];
    char str1[32] = "\r\nzubinzubin123435\r\nzubinzubin\r\n";
    if (argc != 2)
    {
        return 1;
    }
    printf ("(%s)\n", str);
    printf ("(%s)\n", strrev2(str));

    printf ("(%s)\n", str1);
    printf ("(%s)\n", strrev2(str1));

    return 1;
}

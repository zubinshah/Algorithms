//this program checks the ip mask 
#include <stdio.h>

#define IS_NETMASK_VALID(m) (m & (~m >> 1))

int
main(int argc, char** argv)
{
    unsigned int ipaddr = 0xFFFFFF00;
    printf("%x is %d\n", ipaddr, !IS_NETMASK_VALID(ipaddr));
    ipaddr = 0xFF000000;
    printf("%x is %d\n", ipaddr, !IS_NETMASK_VALID(ipaddr));
    ipaddr = 0xFF00FF00;
    printf("%x is %d\n", ipaddr, !IS_NETMASK_VALID(ipaddr));
    ipaddr = 0x00000000;
    printf("%x is %d\n", ipaddr, !IS_NETMASK_VALID(ipaddr));
    return 0;
}

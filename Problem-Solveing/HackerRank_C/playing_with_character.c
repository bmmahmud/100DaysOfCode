/*"Playing With Characters */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char ch;
    char s[100];
    char sen[100];
    scanf("%c",&ch);
    scanf(" %[^\n]s",s); //  in palce of scanf("%s", &s);
    scanf(" %[^\n]s",sen); // in palce of scanf(" %[^\n]%*c", &sen);


    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("%c\n",ch);
    printf("%s",s);
    return 0;
}




//Sum of Digits of a Five Digit Number
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    int sum=0,num,temp,r;
    //printf("Enter Number: ");
    scanf("%d",&num);

    temp=num;
    while(temp != 0){
        r = temp%10; // take the last digit
        sum += r; // add the last digit
        temp = temp/10; // reduce the last digit
    }
    printf("%d\n",sum);

    return 0;
}



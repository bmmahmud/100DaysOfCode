/******************************************************************************
                           52 Programming Problem-tamim Shahriar Subeen
                           Problem No: 5
*******************************************************************************/

#include <stdio.h>

int main()
{
    int Number,i,j,k,num;
    printf("Enter Number:");
    scanf("%d",&Number);
    for(i=1;i<=Number;i++)
    {

    scanf("%d",&num);
    for(j=1;j<=num;j++){

            for(k=1;k<=num;k++)
            {
                printf("* ");
            }
             printf("\n");
        }
        printf("\n");
    }

    return 0;
}

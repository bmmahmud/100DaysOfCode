/******************************************************************************
                           52 Programming Problem-tamim Shahriar Subeen
                           Problem No: 4
*******************************************************************************/

#include <stdio.h>

int main()
{
    int Number,i,j,num;
    printf("Enter Number:");
    scanf("%d",&Number);
    for(i=1;i<=Number;i++)
    {
        scanf("%d",&num);
        printf("Case %d: ",i);

        for(j=1;j<=num;j++){
            if(num%j==0)
            {
                printf("%d ",j);
            }
        }
        printf("\n");
    }

    return 0;
}

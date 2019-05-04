/*
           *
          ***
         *****
        *******
*/
#include<stdio.h>
void main(){
int row,space,colm,n;
printf("Number of Rows: ");scanf("%d",&n);

for(row=1;row<=n;row++){
     for(space=1;space<=n-row;space++)
       printf(" ");
       for(colm=1;colm<=2*row-1;colm++)
            printf("*");
           //  printf("%d",colm);
          //printf("%c",colm+64);
       printf("\n");
}
for(row=n-1;row>=1;row--){
     for(space=1;space<=n-row;space++)
       printf(" ");
       for(colm=1;colm<=2*row-1;colm++)
            printf("*");
           //  printf("%d",colm);
          //printf("%c",colm+64);
       printf("\n");
}

}


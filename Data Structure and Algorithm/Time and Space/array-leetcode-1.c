#include<stdio.h>

void main(){
int target,i,value,j;
int mark[5] = {1, 3, 7, 9, 2};
target = 11;
for(i=0;i<5;i++){
 value = target - mark[i] ;
     for(j=i+1;j<5;j++){
        if(value == mark[j]){
           printf("%d %d",mark[j],mark[i]);
        }
   }
   return 0;
 }
}

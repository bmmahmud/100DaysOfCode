#include<stdio.h>
int main(){
int first=0,second=1,fibo,n,count=0;
printf("Enter Range: ");
scanf("%d",&n);

//check range
while(count<n){
    if(count<=1){
        fibo=count;
    }else{
        fibo=first+second;
        first=second;
        second=fibo;
    }
    printf("%d ",fibo);
    count++;
}
}

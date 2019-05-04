#include<stdio.h>
void main(){

int array[10],n,i,j,temp;
// insert integers
printf("Enter N integers: ");
scanf("%d",&n);
printf("Enter %d integers: ",n);
for(i=0;i<n;i++){
scanf("%d",&array[i]);}

// Bubble sort
for(i=0;i<n;i++){
    for(j=0;j<n-i-1;j++){
        if(array[j]>array[j+1]){
            temp=array[j];
            array[j]=array[j+1];
            array[j+1]=temp;
        }
    }
}
// Print sorted list
printf("Sorted inters: ");
for(i=0;i<n;i++){
    printf(" %d ",array[i]);
}

}

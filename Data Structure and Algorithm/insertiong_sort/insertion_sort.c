// Insertion Sort from Subeens Books
#include<stdio.h>
void main(){

int array[10],n,i,j,item;
// insert integers
printf("Enter N integers: ");
scanf("%d",&n);
printf("Enter %d integers: ",n);
for(i=0;i<n;i++){
scanf("%d",&array[i]);}

// Bubble sort
for(i=0;i<n;i++){
    item=array[i];
    j=i-1;

    while(j>=0 && array[j]<item){
        array[j+1]=array[j];
        j=j-1;
    }
    array[j+1]=item;
}
// Print sorted list
printf("Sorted inters: ");
for(i=0;i<n;i++){
    printf(" %d ",array[i]);
}

}


#include<iostream>
using namespace std;
int main(){

int A[5]={1,2,3,4,5};
int left,right,mid,x;
left=0;right=4,x=4;
while(left<=right){
    mid=(left+right)/2;

    if(A[mid]==x){
        cout<<mid+1;break;
    }
    else if(A[mid]< x){
        left=mid+1;
    }
    else{
        right=mid-1;
    }
}
   if (left>right)
      cout<<"Not found!"<<x <<" isn't present in the list.\n";
   return 0;
}

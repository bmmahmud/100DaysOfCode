#include<iostream>
using namespace std;
int linear_search(int A[],int n,int x);
int main(){
int A[100];
int n,i,x,result;
cout<<"Enter number of elements: ";
cin>>n;
for(i=0;i<n;i++){
    cin>>A[i];
}
cout<<"All the elements Are: ";
for(i=0;i<n;i++){
    cout<<A[i]<<" ";
}
cout<<"\n Find location of the Element: ";
cin>>x;
result = linear_search(A,n,x);
if(result== -1){
    cout<<x<<" is not Exist";
} else{
    cout<<x <<" is located at "<<result+1;
    }
}
//function
int linear_search(int A[],int n,int x){

int i;
for(i=0;i<n;i++){
    if(A[i]==x){
        return i;
    }
}
i=-1;
return i;
}


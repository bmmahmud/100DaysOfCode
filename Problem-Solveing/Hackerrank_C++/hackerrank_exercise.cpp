#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d){
int A[4]={a,b,c,d};
int i,j,item;
for(i=0;i<4;i++){
    item=A[i];
    j=i-1;

    while(j>=0 && A[j]<item){
        A[j+1]=A[j];
        j=j-1;
    }
    A[j+1]=item;
}
return A[0];
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}


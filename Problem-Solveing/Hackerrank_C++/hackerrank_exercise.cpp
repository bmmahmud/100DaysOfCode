/*
Arrays Introduction: reverse order in a single line separated by a space.
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main() {

  int n, number, i;
  int arr[1000];
  //scanf("%d", &n);
  cin>>n;
  for (i = 0; i < n; i++) {
    //scanf("%d", &arr[i]);
    cin>>arr[i];
  }
//   for (i = 0; i < n; i++) {
//     printf("%d ", arr[i]);
//   }
//   printf("\nreverse order in a single line separated by a space: \n");
  for (i =n-1; i>= 0; i--) {
   // printf("%d ", arr[i]);
   cout<<arr[i]<<" ";
  }

  return 0;
}

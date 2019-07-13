/******************************************************************************

Hi,I am B.M. ASHIK MAHMUD.
PROBLEM: DCP-544: GAMORA Confusion 
FROM DEVSKILL

*******************************************************************************/
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,i;
	char str[100];
	char Q[10]="Quill";
	char S[10]="Stark";
	char D[10]="Drax";
	cin>>t;
	for(i=0;i<t;i++){
        cin>>str;
        //cout<<str;
        if(strcmp(str, Q)==0){ //compare two string 
            cout<<"I am going to ask you this one time, where is Gamora?\n";
        }
        else if(strcmp(str, S)==0){
            cout<<"I will do you one better, who is Gamora?\n";
        }
        else if(strcmp(str, D)==0){
            cout<<"I will do you one better, why is Gamora?\n";
        }
        else{
            cout<<"What is Gamora?\n";
        }
    }

	return 0;
}

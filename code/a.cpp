#include<iostream>
#include<string>
using namespace std;

int main(){
	string s="abcdefg";
	for(auto &ch:s){
		cout<<ch;
	}
	system("pause");
	return 0;
}
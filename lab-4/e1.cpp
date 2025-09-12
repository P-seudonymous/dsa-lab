#include <iostream>
using namespace std;
int rfact(int n); //recursive func
int fact(int n);//interative func

int main(){
  int a;
  cout << "enter a number: ";
  cin >> a;
  cout << "factorial(recursive): " << rfact(a )<<endl;
  cout << "factorial(iterative): " << fact(a) <<endl;
}

int rfact(int n){
  if(n==0){return 1;}
  else{return n*rfact(n-1);}
}

int fact(int n){
  int a=1;
  for(int i=1;i<=n;i++){
    a*=i;
  }
  return a;
}

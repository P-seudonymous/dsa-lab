#include <iostream>
using namespace std;

int pow(int n, int pwr);

int main(){
    cout << "enter number and power respectively(both should be separate integers: ";
    int a, b;
    cin >> a >> b;
    cout << a << "^" << b << " = " << pow(a, b);
}

int pow(int n, int pwr){
    if(pwr==0){
        return 1;
    }else{
        return n*pow(n, pwr-1);
    }
}

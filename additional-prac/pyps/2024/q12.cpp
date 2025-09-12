#include <iostream>
using namespace std;

int mul(int a, int b);

int main(){
    cout << "input a & b: ";
    int x, y;
    cin >> x >> y;
    cout << "product: " << mul(x, y);
}

int mul(int a, int b){
    if(a==0||b==0){
        return 0;
    }else{
        return a+mul(a,b-1);
    }
}

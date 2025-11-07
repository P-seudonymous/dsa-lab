#include <iostream>

int cmp(int a, int b);
using namespace std;



int main(){

    int x, y;
    cout << "input numbers: ";
    cin >> x >> y;
    
    cmp(x, y);
    
}


int cmp(int a, int b){
    if(a>b){
        cout << a << " is greater\n";
        return a;
    }
    else{
        cout << b << " is greater\n";
        return b;
    }
}

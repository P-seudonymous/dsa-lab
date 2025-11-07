#include <iostream>
using namespace std;

//tribonaci sequence

int main(){

    int x, first, second, third;
    first = 0;
    second = 0;
    third = 1;

    cout << "input number of terms: ";
    cin >> x;

    if(x>=1){
        cout << first << " ";
    }
    if(x>=2){
        cout << second << " ";
    }
    if(x>=3){
        cout << third<< " ";
    }

    for(int i=3;i<x;i++){
        int next = first + second+third;
        cout << next << " ";

        first = second;
        second = third;
        third = next;
    }
    
}

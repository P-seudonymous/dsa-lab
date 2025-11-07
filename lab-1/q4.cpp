#include <iostream>

using namespace std;

int main(){
    
    int a;
    cin >> a; 
    int *ptr = new int; //allocating memory on heap.
    *ptr = a; 
    cout << *ptr << "\n"; // value that ptr is pointing to
    cout << ptr << "\n"; // addr of ptr

    delete ptr;
    cout << ptr << " " << *ptr; //addr of ptr will be same, but the vaue would be garbage.


}


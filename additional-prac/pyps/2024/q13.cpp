#include <iostream>
using namespace std;

class base{
    protected:
        int a, b;
    public:
        base(){
            cout << "input 2 integers: ";
            cin >> a>>b;
        }
};

class derived:public base{
    public:
        void sum(){
            int sum = a+b;
            cout << "sum: " << sum;
        }
};

int main(){
    derived d;
    d.sum();
}

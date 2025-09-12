#include <iostream>
using namespace std;

class A{
    protected:
    int a;
    public:
    void get_a(){
        cout << "input a: ";
        cin >> a; 
    }
};

class B:public A{
    protected:
    int b;
    public:
    void get_b(){
        cout << "input b: ";
        cin >> b;
    }
};

class C:public B{
    public:
        void square(){
            cout << "value of ((a+b)^2): " << ((a+b)*(a+b));
        }
};

int main(){
    C c;
    c.get_a();
    c.get_b();
    c.square();
}

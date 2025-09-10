#include <iostream>
using namespace std;

class base{
  protected:
    int a, b;
  public:
    void get(){
      cout << "input 2 int values: ";
      cin >> a >> b;
    }
};

class derived:public base{
  int c;
  public:
    void add(){c=a+b;cout << a<< "+"<< b << "="<< c;}
};

int main(){
  derived d;
  d.get();
  d.add();
}

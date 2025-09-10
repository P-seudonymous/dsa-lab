#include <iostream>
using namespace std;

class printdata{
  public:
    void print(int i){cout << "int: "<< i << endl;}
    void print(double i){cout << "double: "<< i << endl;}
    void print(char *i){cout << "string : "<< i << endl;}
};

int main(){
  printdata p;
  p.print(5);
  p.print(97.924882);
  p.print("hello world");
}

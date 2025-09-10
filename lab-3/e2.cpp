#include <iostream>
using namespace std;

class base{
  public:
    int x;
    void getdata_x(){cout << "enter val of x="; cin >> x;}
};

class derive1:public base{
  public:
    int y;
    void getdata_y(){cout << "enter val of y="; cin >> y;}
};

class derive2:public derive1{
  int z;
  public:
    void getdata_z(){cout << "enter val of z="; cin >> z;}
    void prod(){cout << "product: " << x*y*z;}
};


int main(){
  derive2 d2;
  d2.getdata_x();
  d2.getdata_y();
  d2.getdata_z();
  d2.prod();
}

#include <iostream>
using namespace std;

class complex{
  float real, img;

  public:
  complex();
  complex(float x, float y);
  void read_complex();
  void display();
}

complex::complex(){
  real = img = 0;
}

complex::complex(float x, float y){
  real = x;
  img = y;
}

void complex::display(){
  char sign;
  if(img<0){
    sign = '-';
    img = -img;
  }
  else{
    sign = '+';
  }
  cout<<real<<sign<<"i"<<img<<endl;
}

complex complex::operator+(complex c){
  complex r;
  r.real=real+c.real;
  r.img=img+c.img;
  return r;
}

complex complex::operator-(complex c){
  complex r;
  r.real=real-c.real;
  r.img=img-c.img;
  return r;
}

void complex::read_complex(){
  cout<<"Enter real part of complex number;";
  cin>>real;
  cout<<"Enter Imaginary part of complex number:";
  cin>>img;
}

int main(){
  complex a;
  a.read_complex();
  complex b;
  b.read_complex();
  complex c, d;
  c=a+b;
  cout<<"After Addition of two complex numbers";
  c.display();
  d=a-b;
  cout<<"Difference of two complex numbers";
  d.display();
  return 0;
}


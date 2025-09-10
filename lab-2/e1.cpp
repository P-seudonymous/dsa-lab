// use operator overloading to use + and - in Complex addition/sub resp.

#include <iostream>
using namespace std;


class Complex{
  float real, img;
  public:
  Complex();
  Complex(float x, float y);
  void read_Complex();
  Complex operator+(Complex);
  Complex operator-(Complex);
  void display();
};

int main(){
  
  Complex a;
  a.read_Complex();
  Complex b;
  b.read_Complex();
  Complex c, d;
  c=a+b;
  cout << "after addition: ";
  c.display();
  d = a-b;
  cout << "after sub: ";
  d.display();
}

Complex::Complex(){real=img=0;}
Complex::Complex(float x, float y){real = x; img=y;}
void Complex::display(){
  char sign;
  if(img<0){
    sign = '-';
  }else {
    sign='+';
  }
  cout << real << sign << img << "i" << endl;
}
Complex Complex::operator+(Complex c){
  Complex r;
  r.real=real+c.real;
  r.img=img+c.img;
  return r;
}
Complex Complex::operator-(Complex c){
  Complex r;
  r.real=real-c.real;
  r.img=img-c.img;
  return r;
}
void Complex::read_Complex(){
  cout << "enter real part of Complex number: ";
  cin >> real;
  cout << "enter img part of Complex number: ";
  cin >> img;
}

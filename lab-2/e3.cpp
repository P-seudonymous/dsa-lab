#include <iostream>
using namespace std;

class sample2;
class sample1{
  int x;
  public:
    sample1(int a);
    friend void max(sample1 s1, sample2 s2);
};

sample1::sample1(int a){x=a;}

class sample2{
  int y;
  public:
    sample2(int b);
    friend void max(sample1 s1, sample2 s2);
};

sample2::sample2(int b){y=b;}

void max(sample1 s1, sample2 s2){
  if(s1.x>s2.y){
    cout << "data_member in object of sample1 is greater\n";
  }else{
    cout << "data_member in object of sample2 is greater\n";
  }
}


int main(){
  int a, b;
  cout << "input 2 numbers: ";
  cin >> a >> b;
  sample1 obj1(a);
  sample2 obj2(b);
  max(obj1,obj2);
}


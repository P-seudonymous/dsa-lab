#include <iostream>
using namespace std;

class counter{
  private:
    int value;

  public:
    counter(int v = 0) : value(v){}

    void display() const{
      cout << "value: "<< value << endl;
    }

    counter& operator++(int){
      counter temp = *this;
      value++;
      return temp;
    }

    counter& operator--(int){
      counter temp = *this;
      value--;
      return temp;
    }
};


int main() {
    counter c(5);

    cout << "Initial: ";
    c.display();

    c++;
    cout << "After postfix ++: ";
    c.display();

    c--;
    cout << "After postfix --: ";
    c.display();

    return 0;
}


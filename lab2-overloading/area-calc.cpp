#include <iostream>
using namespace std;

class areaCalc{
  public:
    float area(float side){
      return side*side;
    }
    int area(float len, float breadth){
      return len*breadth;
    }
    int area(double base, double height){
      return 0.5*base*height;
    }
};

int main(){
  areaCalc calc;

  float side, len, breadth; 
  double base, height;

  cout << "side of square: ";
  cin >> side;
  cout << "area: " << calc.area(side) <<endl;
}

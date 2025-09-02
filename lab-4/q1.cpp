// Using the infinite series of ‘sine’, write a C++ program to find the approximate value of sin(x) for the first ‘n’ terms of the series. 
// (Enter the value of ‘x’ in degrees)



#include <iostream>
#include <cmath>
using namespace std;

long long fact(int n){
  if (n<=1){
    return 1;
  }
  return n*fact(n-1);
}

double power(double base, int exp){
  if(exp==0){
    return 1;
  }
  return base*power(base, exp-1);
}

double sine_series(double x_rad, int n, int k=0){
  if (k==n){
    return 0;
  }
  int powerExp = 2*k+1;
  double term = power(-1, k) * power(x_rad, powerExp) / fact(powerExp);

  return term + sine_series(x_rad, n, k + 1);

}

int main() {
    double x_deg;
    int n;

    cout << "Enter angle in degrees: ";
    cin >> x_deg;

    cout << "Enter number of terms: ";
    cin >> n;

    double x_rad = x_deg * M_PI / 180.0;

    double approx = sine_series(x_rad, n);

    cout << "Approximate sin(" << x_deg << ") using " << n << " terms = " << approx << endl;
    cout << "Actual value(from library) = " << sin(x_rad) << endl;

    return 0;
}


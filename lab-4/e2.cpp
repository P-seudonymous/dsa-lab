#include <iostream>
using namespace std;

template<class T>
void maxmin(T a[], int n){
  T temp;
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      if(a[i]>a[j]){
          a[i]=a[i]^a[j];
          a[j]=a[i]^a[j];
          a[i]=a[i]^a[j];
      }
    }
  }
  cout << "max= "<<a[n-1]<<"\n"<<"min= "<<a[0]<<"\n";
  cout << "sorted list: \n";
  for(int i=0;i<n;i++){cout<<a[i]<<" ";}
}

int main(){

}

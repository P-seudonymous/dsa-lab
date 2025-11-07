#include <iostream>
using namespace std;

int main(){
    
    int a;
    cout << "input a number: ";
    cin >> a;

    int arr[a];
    

    cout <<  "input an array: ";
    for(int i=0;i<a;i++){
        cin >> arr[i];
    }

    cout << "\n";

    int small = arr[0];
    int large = arr[0];

    for(int i=1;i<a;i++){
        if(small > arr[i]){
            small = arr[i]; 
        }
        if(large < arr[i]){
            large = arr[i];
        }
    }
    
    cout << "smallest ele: " << small;
    
    cout << "\nlargest ele: " << large;

}

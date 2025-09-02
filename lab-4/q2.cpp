#include <iostream>
using namespace std;

void generate(int start, int n, int k, int arr[], int idx) {
    if (idx == k) {
        for (int i = 0; i < k; i++) {
            cout << arr[i];
            if (i < k - 1) cout << ",";
        }
        cout << "   ";
        return;
    }

    for (int i = start; i <= n; i++) {
        arr[idx] = i; 
        generate(i + 1, n, k, arr, idx + 1);
    }
}

int main() {
    int n, k;
    cout << "input n: ";
    cin >> n;
    cout << "input k: ";
    cin >> k;

    int arr[100];

    cout << "sequences " << k << " from first " << n << " natural numbers:\n";

    generate(1, n, k, arr, 0);
    cout << endl;

    return 0;
}

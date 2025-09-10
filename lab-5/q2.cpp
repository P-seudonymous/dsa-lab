#include <iostream>
using namespace std;

struct Node{ int data; Node* next; Node(int v):data(v),next(0){} };

int countNodes(Node* h){ int c=0; for(;h;h=h->next) c++; return c; }

int main(){
    Node* h=new Node(1); h->next=new Node(2); h->next->next=new Node(3);
    cout<<countNodes(h)<<"\n";
}


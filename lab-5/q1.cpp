#include <iostream>
using namespace std;

struct Node { int data; Node* next; Node(int v):data(v),next(0){} };

void insertEnd(Node*& head,int v){
    Node* n=new Node(v);
    if(!head){ head=n; return; }
    Node* p=head; while(p->next) p=p->next; p->next=n;
}

void deletePos(Node*& head,int pos){
    if(!head) return;
    if(pos==1){ head=head->next; return; }
    Node* p=head; for(int i=1;i<pos-1 && p;i++) p=p->next;
    if(p && p->next) p->next=p->next->next;
}

void print(Node* h){ for(;h;h=h->next) cout<<h->data<<" "; cout<<"\n"; }

int main(){
    Node* h=0;
    for(int i=1;i<=5;i++) insertEnd(h,i);
    print(h);
    deletePos(h,3);
    print(h);
}


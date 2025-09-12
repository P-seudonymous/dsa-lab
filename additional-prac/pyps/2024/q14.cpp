#include <iostream>
using namespace std;

class Node{
    public:
        int data;
        Node* prev;
        Node* next;
};

class LinkedList{
    Node* head;
    public:
        LinkedList(){
            head = nullptr;
        }
        void push_front(int ele){
            Node* newnode = new Node();
            newnode->data= ele;
            newnode->prev=nullptr;
            newnode->next=nullptr;
            if(head==nullptr){
                head=newnode;
            }else{
                head->prev=newnode;
                newnode->next=head;
                head=newnode;
            }
        }
};










int main(){}

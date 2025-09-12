#include <iostream>
using namespace std;

class Node{
  public:
    int data;
    Node* next;
};

class LinkedList{
  Node* head;
  public:
  LinkedList(){
    head = nullptr;
  }
  void insert_begin(int ele){
    Node* newnode = new Node();
    newnode->data = ele;
    newnode->next = head;
    head = newnode;
  }
  void insert_end(int ele){
      Node* newnode = new Node();
      newnode->data = ele;
      newnode->next = nullptr;
      if(head==nullptr){
          head=newnode;
      }else{
          Node* temp = head;
          while(temp->next!=nullptr){
              temp=temp->next;
          }

      temp->next=newnode;
    }
  }

    void printlist(){
      Node *temp = head;
      if(temp!=nullptr){
        cout << "list -> ";
        while(temp!=nullptr){
          cout << temp->data<<" ";
          temp = temp->next;
        }
        cout << endl;
      }
      else{
        cout << "empty list.\n";
      }
    }
};

int main(){
    LinkedList list;
    list.insert_end(50);
    list.insert_end(40);
    list.insert_end(30);
    
    list.printlist();
}

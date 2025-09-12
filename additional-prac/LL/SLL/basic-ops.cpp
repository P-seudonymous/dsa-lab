#include <iostream>
using namespace std;

class Node{
  public:
    int data;
    Node* next;
};

class LinkedList{
  private:
    Node *head;
  public:
    LinkedList(){
      head = nullptr;
    }
    void insertAtEnd(int element){
      
      Node* newnode = new Node();
      newnode->data = element;
      newnode->next = nullptr;
      
      if(head==nullptr){
        head=newnode;
      }else{
        Node* temp = head;
        while(temp->next !=nullptr){
          temp = temp->next;
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
  int n, val;
  cout << "input number of nodes: ";
  cin >> n;
  
  for(int i=0;i<n;i++){
    cout << "\ninput value of node: ";
    cin >> val;
    list.insertAtEnd(val);
  }

  list.printlist();
}

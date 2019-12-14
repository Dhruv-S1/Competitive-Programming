#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

// Traverses a linkedlist.
// traverse: Node -> (output of integers)

void traverse (Node* linkedlist)
{
	while(true)
	{
		cout<<linkedlist->data<<" ";
		if(linkedlist->next == NULL){
			break;
		}
		linkedlist = linkedlist->next;
	}
	cout<<""<<endl; // Starts new line.
}


// Reverses a linkedlist using a three pointer approach.
// See: https://www.geeksforgeeks.org/reverse-a-linked-list/  for details. 
// Node -> Node

Node* reverse (Node* linkedlist)
{
    Node* prev;
    Node* curr;
    Node* next;
    curr = linkedlist;
    prev = NULL;
	while (curr!=NULL)
	    {
	        next = curr->next;
	        curr->next = prev;
	        prev = curr;
	        curr = next;
	    }
	return prev;
}

int main()
{
    // Creating a sample linkedlist.
    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;

    head = new Node();
    second = new Node();
    third = new Node();
    head->data = 5;
    head->next = second;

    second->data = 10;
    second->next = third;

    third->data = 15;
    third->next = NULL;

    traverse(reverse(head));
    
}

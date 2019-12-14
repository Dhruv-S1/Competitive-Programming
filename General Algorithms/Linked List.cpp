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


// Reverses a linkedlist.
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


// Inserts a Node so that it has the nth position in the
// linkedlist, counting from 0. If n is larger than the length
//  of the list, then it is inserted at the end.
// insert: Node Node int -> Node

Node* insert (Node* linkedlist, Node* node, int pos)
{
	if (pos == 0)
	{
		node->next = linkedlist;
		return node;
	}
	Node* head = linkedlist;
	int counter = 0;
	while(true){
		if (pos-1 == counter)
		{
			node->next = linkedlist->next;
			linkedlist->next = node;
			return head;
		}
		if(linkedlist->next == NULL) break;
		counter++;
		linkedlist = linkedlist->next;
	}
	linkedlist->next = node;
	node->next = NULL;
	return head;
	
}

int main()
{
	// Creating a sample linkedlist.
    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;
    Node* fourth = NULL;

    head = new Node();
    second = new Node();
    third = new Node();
    fourth = new Node();
    
    head->data = 5;
    head->next = second;

    second->data = 10;
    second->next = third;

    third->data = 15;
    third->next = NULL;
    
    fourth->data = 20;
    
	
    traverse(reverse(insert(head, fourth, 2)));
    
}

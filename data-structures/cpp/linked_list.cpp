/*  Linked List Implementation
    Implementing the list container class , and a testing *main* function
    to operate as STL list. 

        Constructor, build a dummy/empty list 
        Constructor, build a list from another list reference
        Destructor, free all allocated nodes
        Operator=
        Insert : constant O(1) operation
        Remove : O(n) worst case operation - remove elem with specific value
        RemoveFirst : remove first occuring element
        Unique : remove duplicates
        Sort
        Reverse
        Front
        Back
        Size
        Empty
        Clear
   
    #1 - implement using simple integers
    #2 - update using Templates
 */

#include <iostream>
#include <cstddef>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node (int value)
    {
        this->data = value;
        this->next = NULL;
    }
};

class LinkedList
{
private:
    Node *rNode;
    int count;
public:
    LinkedList () : rNode(NULL), count (0)
    {

    }

    LinkedList (LinkedList &ll) : rNode(NULL), count (0)
    {
        //TBD
        //Construct the same list from another list
    }
 
    ~LinkedList ()
    {
        while(rNode)
        {
            Node *temp = rNode;
            rNode = rNode->next;
            delete temp;
        }
    }

    void insert(int data)
    {
        Node *root = this->rNode;
        if (!root)
        {
            root = new Node(data);
            rNode = root;
            //cout << "inserting " << root->data << " , @" << root << endl;
            return;
        }
        while(root->next)
        {
            root = root->next;
        }
        root->next = new Node(data);
        return;
    }

    int remove (int data)
    {
        Node *root = this->rNode;
        if (!root)
        {
            return 1; // key not found
        }

        if (root->data == data)
        {
            //remove root node
            this->rNode = root->next;
            delete root;
            return 0; // success 
        }
          
        while (root->next)
        {
            if (root->next->data == data)
            {
                //found first node to delete 
                Node *node = root->next;
                root->next = root->next->next;
                delete node;
                return 0; //success
            }
            root = root->next;
        }
        return 1; //key not found
    }

    void print (char *str)
    {
        Node *root = this->rNode;
        int i = 1;
        cout << "Printing Linked List: ";
        if (str)
        {
            cout << "(" << str << ")" << endl;
        }
        else
        {
            cout << endl;
        }
        while (root)
        {
            cout << root->data << ", ";
            root = root->next;
            if ( (i > 0) && (i++%16 == 0) )
            {
                cout << endl;
            }
        }
        cout << endl;
    }

    /*
        Constructor, build a dummy/empty list 
        Constructor, build a list from another list reference
        Destructor, free all allocated nodes
        Operator=
        Insert : constant O(1) operation
        Remove : O(n) worst case operation - remove elem with specific value
        RemoveFirst : remove first occuring element
        Unique : remove duplicates
        Sort
        Reverse
        Front
        Back
        Size
        Empty
        Clear
 
    */
};

int
main (int argc, char **argv)
{
    LinkedList *ll = new LinkedList();
    int numInputs = 0;
    int data;

    cout << "Enter the number of nodes to enter: ";
    cin >> numInputs;

    Node *head = 0;
    while (numInputs-- > 0)
    {
        cin >> data;
        cout << "\b";
        ll->insert(data);
    }
    ll->print((char*)"original linked list");

    cout << "remove one node: ";
    cin >> data;
    ll->remove(data);
    ll->print((char*)"after removing one node");
    delete ll; 

    //cout << "remove all nodes with key: ";
    //cin >> data;
    //ll->remove_all(data);
    //ll->print((char*)"after removing all nodes");
    //delete ll; 

    //cout << "Cleaned up all variables" << endl;
    return 0;
}

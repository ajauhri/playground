#include<stdio.h>

typedef struct node {
    char data;
    struct node* next;
}
node;

void print_list(node *root) 
{
    while(root) {
        printf("%c", root->data);
        root = root->next;
    }
    printf("\n");
}

void* reverse(node *root)
{
    node *new_root = '\0';
    while(root) {
        node *next = root->next;
        root->next = new_root;
        new_root = root;
        root = next;
    }
    return new_root;
}


int main()
{
    node a = {'a', 0};
    node b = {'b', &a};
    node c = {'c', &b};
    node d = {'d', &c};

    node *root = &d;
    print_list(root);
    root = reverse(root);
    print_list(root);

    return 0;
}



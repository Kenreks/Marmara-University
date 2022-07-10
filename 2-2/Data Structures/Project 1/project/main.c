/*  CSE 2025 Data Structures Project 1
    E-Commerce System
    Ahmet Faruk Güzel   150119659
    Hüseyin Kerem Mican 150119629
    Muhammet Eren Atala 150119904
*/





#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <stdbool.h>

#define ELEMENT 50
#define LINE 256
//Prototype of some functions and structs
struct CustomerNode;
struct ProductNode;
struct BasketNode;
void productCompare(struct ProductNode *root);
void swapNode(struct ProductNode *ptr1, struct ProductNode *ptr2);
void listProduct(struct ProductNode *root);
void listCustomer(struct CustomerNode *root);
bool customerSearchByName(struct CustomerNode *root, const char *name, int *id);
void removeCustomer(struct CustomerNode **rootPtr, struct CustomerNode *root, int id);

struct CustomerNode
{ 
    //Structure for customer Linkedlist
    int id;
    char *name;
    char *surname;
    struct BasketNode *basketHead;  
    struct CustomerNode *next;
};

struct ProductNode
{
    //Structure for product Linkedlist
    int id;
    char *name;
    char *category;
    int price;
    struct ProductNode *next;
};

struct BasketNode
{
    //Structure for basket Linkedlist
    int id;
    int amount;
    struct ProductNode *productListHead;
    struct BasketNode *next;
};

struct CustomerNode *newCustomer(int id, const char *name, const char *surname)
{
    /*  Returns a struct type customerNode. It has an algorithm to create a new customer node in memory.
        This function’s parameters are id (created by program), name and surname (taken from user input).
    */
    struct CustomerNode *customerNode = (struct CustomerNode *)malloc(sizeof(struct CustomerNode)); 

    customerNode->id = id;

    customerNode->name = (char *)calloc(strlen(name), sizeof(char));
    strcpy(customerNode->name, name);

    customerNode->surname = (char *)calloc(strlen(surname), sizeof(char));
    strcpy(customerNode->surname, surname);

    customerNode->next = NULL;
    customerNode->basketHead = NULL;
    return customerNode;
}

int isCustomerEmpty(struct CustomerNode *root)
{
    /*  The function checks given linked list is empty or not.
        If it is empty, it returns true. It has a struct parameter to check the linked list.
    */
    return !root;
}

void pushCustomer(struct CustomerNode **root, int id, const char *name, const char *surname)
{
    /*  The function pushes new created customer node to the customer linked list which comes from newCustomer function.
        It has id, name and surname.
    */
    struct CustomerNode *customerNode = newCustomer(id, name, surname);
    customerNode->next = *root;
    *root = customerNode;
}

int popCustomer(struct CustomerNode **root)
{   /*  This method pops out the first element of stack type linked list and remove it from memory.
    */
    if (isCustomerEmpty(*root))
        return INT_MIN;
    struct CustomerNode *temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
}

void removeCustomer(struct CustomerNode **rootPtr, struct CustomerNode *root, int id) 
{   /*  This function able user to remove the customer by given input which includes name and surname. 
        It takes three parameters which are rootPtr (to change our linked list), root (root of linked list), id (integer). 
        The id is an integer found by another function through name and surname.
    */
    struct CustomerNode *popList = NULL;
    //  Transfer nodes data to temporary linked list until find given id
    while (root->id != id)
    {
        pushCustomer(&popList, root->id, root->name, root->surname);
        popList->basketHead = root->basketHead;
        popCustomer(&root);
    }
    //  Remove the customer with given id
    popCustomer(&root);
    //  Push temporary linked list back to customer linked list
    while (!isCustomerEmpty(popList))
    {
        pushCustomer(&root, popList->id, popList->name, popList->surname);
        root->basketHead = popList->basketHead;
        popCustomer(&popList);
    }
    *rootPtr = root;
}

struct ProductNode *newProduct(int id, const char *name, const char *category, int price)
{   /*  Returns a struct type productNode. 
        It has an algorithm to create a new product node in memory. 
        Parameters are: id (integer, unique for every item), name (constant char pointer), category (constant char pointer) and price (integer).
    */

    struct ProductNode *productNode = (struct ProductNode *)malloc(sizeof(struct ProductNode));

    productNode->id = id;

    productNode->name = (char *)calloc(strlen(name), sizeof(char));
    strcpy(productNode->name, name);

    productNode->category = (char *)calloc(strlen(category), sizeof(char));
    strcpy(productNode->category, category);

    productNode->price = price;
    productNode->next = NULL;

    return productNode;
}

int isProductEmpty(struct ProductNode *root)
{   /*  The function checks given linked list is empty or not. If it is empty, it returns true. 
        It has a struct parameter to check the linked list.
    */
    return !root;
}

void pushProduct(struct ProductNode **root, int id, const char *name, const char *category, int price)
{   /*  This function pushes new created product node to the product linked list which comes from newProduct. 
        It takes root, id, name, category and price as parameters.
    */

    struct ProductNode *productNode = newProduct(id, name, category, price);
    productNode->next = *root;
    *root = productNode;
}

int popProduct(struct ProductNode **root)
{   /*  This method pops out the first element of stack type linked list and remove it from memory, has a struct type paramater named root.
    */
    if (isProductEmpty(*root))
        return INT_MIN;
    struct ProductNode *temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
    return popped;
}

struct BasketNode *newBasket(int id)
{   /*  Returns a struct type basketNode. 
        It has an algorithm to create a new basket node in memory. 
        There is only one parameter which is the id of the basket.
    */

    struct BasketNode *basketNode = (struct BasketNode *)malloc(sizeof(struct BasketNode));

    basketNode->id = id;
    basketNode->next = NULL;
    basketNode->amount = 0;
    basketNode->productListHead = NULL;
    return basketNode;
}

int isBasketEmpty(struct BasketNode *root)
{
    /*  The function checks given linked list is empty or not. 
        If it is empty, it returns true. It has a struct parameter to check the linked list.
    */
    return !root;
}

void pushBasket(struct BasketNode **root, int id)
{   
    /*  This function pushes new created basket node to the basket linked list which comes from newBasket. 
        It takes only root and id as parameter.
    */

    struct BasketNode *basketNode = newBasket(id);
    basketNode->next = *root;
    *root = basketNode;
}

int popBasket(struct BasketNode **root)
{
    /*  This method pops the first element of stack type linked list, has a struct type parameter named root.
    */

    if (isBasketEmpty(*root))
        return INT_MIN;
    struct BasketNode *temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
}

struct CustomerNode *CustomerSearch(struct CustomerNode *root, int id)
{   
    /*  This function helps user to reach specific customer with given ID. 
        It returns the found customer id and takes root as parameter beside ID.
    */

    struct CustomerNode *current = root;

    //  Traverse linked list
    while (current != NULL)
    {
        if (current->id == id)
        {   
            return current;
        }
        current = current->next;
    }
    //  Return null customer if given id does not exist in linked list
    current = NULL;
    return current;
}

struct BasketNode *BasketSearch(struct BasketNode *root, int id)
{
    /*  This function helps user to reach specific basket of customer with given basket ID. 
        It returns the customer's basket with given id and takes root as parameter beside basket ID.
    */

    struct BasketNode *current = root;

    //  Traverse linked list
    while (current != NULL)
    {
        if (current->id == id)
        {
            return current;
        }
        current = current->next;
    }
    current = NULL;
    return current;
}

struct ProductNode *ProductSearch(struct ProductNode *root, int id)
{
    /*  This function helps user to reach specific product with given product ID. 
        It returns the found product and takes root as parameter beside product ID.
    */

    struct ProductNode *current = root;

    //  Traverse linked list
    while (current != NULL)
    {
        if (current->id == id)
        {
            return current;
        }
        current = current->next;
    }
    current = NULL;
    return current;
}

bool createBasket(struct CustomerNode *customerRoot, struct ProductNode *productRoot, int personId, int basketId, int productId)
{
    /*  Checks whether the basket exists or not through given basket id by program.  
        If the customer exists it checks whether that customer has basket with given id. 
        If basket does not exist, firstly it creates basket with given basket id then it pushes given product to the baskets ProductList. 
        Then it increments the current basket amount parameter by one.
    */

    struct CustomerNode *customerTemp = CustomerSearch(customerRoot, personId);
    struct ProductNode *productInfo = ProductSearch(productRoot, productId);
    struct BasketNode *currentBasket = BasketSearch(customerTemp->basketHead, basketId);

    if (customerTemp == NULL)
    {
        printf("Customer does not exist\n");
        return false;
    }

    if (currentBasket == NULL)
    {
        pushBasket(&customerTemp->basketHead, basketId);
    }
    currentBasket = BasketSearch(customerTemp->basketHead, basketId);

    pushProduct(&(currentBasket->productListHead), productInfo->id, productInfo->name, productInfo->category, productInfo->price);
    currentBasket->amount++;
}

void listProduct(struct ProductNode *root)
{
    //  Lists every single product in alphabetical order. 

    struct ProductNode *temp = root;
    while (temp != NULL)
    {

        printf("%d %s \n", temp->id, temp->name);
        temp = temp->next;
    }
    printf("\n");
}

void productCompare(struct ProductNode *root)
{
    /*  Compares every product read from text file given by user. 
        It sorts them in alphabetical order using bubble sort. 
    */

    int swapped, i;
    struct ProductNode *current = NULL;
    struct ProductNode *lptr = NULL;

    if (root == NULL)
        return;
    do
    {
        swapped = 0;
        current = root;

        while (current->next != lptr)
        {   
            // Compare every single character in customers name
            for (i = 1; i < strlen(current->name); i++)
            {
                if (strncmp(current->name, current->next->name, i) > 0)
                {
                    swapNode(current, current->next);
                    swapped = 1;
                    continue;
                }
            }

            current = current->next;
        }
        lptr = current;

    } while (swapped);
    return;
}

void swapNode(struct ProductNode *ptr1, struct ProductNode *ptr2)
{
    /*  This function is a part of productCompare function, helps to swap datas of given nodes in linked list. 
    */

    int tempId = ptr1->id;
    char *tempName;
    tempName = (char *)calloc(strlen(ptr1->name), sizeof(char));
    strcpy(tempName, ptr1->name);

    char *tempCategory;
    tempCategory = (char *)calloc(strlen(ptr1->category), sizeof(char));
    strcpy(tempCategory, ptr1->category);

    int tempPrice = ptr1->price;

    ptr1->id = ptr2->id;
    ptr2->id = tempId;

    strcpy(ptr1->name, ptr2->name);
    strcpy(ptr2->name, tempName);

    strcpy(ptr1->category, ptr2->category);
    strcpy(ptr2->category, tempCategory);

    ptr1->price = ptr2->price;
    ptr2->price = tempPrice;
}

void listCustomer(struct CustomerNode *root)
{
    //Lists every single customer in numerical order.

    struct CustomerNode *temp = root;
    if (temp == NULL)
        return;
    else
    {
        listCustomer(temp->next);
        printf("%d %s %s\n", temp->id, temp->name, temp->surname);
        return;
    }
}

void findProduct(struct CustomerNode *root, int productId)
{
    /*  Looks for specific product id given by user. 
        It searches every basket of all customers and print customer names who bought that specific product.
    */

    struct CustomerNode *customerTemp = root;
    struct BasketNode *basketTemp = NULL;
    bool check = false;

    //  Traverse customers
    while (customerTemp != NULL)
    {
        basketTemp = customerTemp->basketHead;
        //  Traverse baskets of customer
        while (basketTemp != NULL)
        {
            if (ProductSearch(basketTemp->productListHead, productId))
            {
                printf("%d. %s %s\n", customerTemp->id, customerTemp->name, customerTemp->surname);
                check = true;
                break;
            }
            basketTemp = basketTemp->next;
        }

        customerTemp = customerTemp->next;
    }
    //if product does not exist in any of customer
    if(!check)
        printf("No product found\n");
}

void listAmount(struct CustomerNode *root)
{
    /*  Prints the total amount of bought product of every single customer. 
        If customer didn’t buy any product it shows as customer didn’t buy anything. 
    */
    struct CustomerNode *customerTemp = root;
    struct BasketNode *basketTemp = NULL;
    int amount = 0;

    if (customerTemp == NULL)
        return;
    else
    {
        listAmount(customerTemp->next);
        basketTemp = customerTemp->basketHead;

        if (basketTemp == NULL)
        {
            printf("%d. %s %s did not buy any product\n", customerTemp->id, customerTemp->name, customerTemp->surname);
            customerTemp = customerTemp->next;
            return;
        }

        while (basketTemp != NULL)
        {
            amount += basketTemp->amount;
            basketTemp = basketTemp->next;
        }
        printf("%d. %s %s amount = %d\n", customerTemp->id, customerTemp->name, customerTemp->surname, amount);
        amount = 0;
    }
}

bool customerSearchByName(struct CustomerNode *root, const char *name, int *id)
{
    /*  This function checks whether given name already exists or not. 
        If it exists it returns false, if not, returns true. 
    */
    struct CustomerNode *current = root;
    int i;
    bool check;

    while (current != NULL)
    {
        check = false;
        for (i = 0; i < strlen(name); i++)
        {

            if ((*(name + i) != *(current->name + i)) && (((*(name + i) + 32) != *(current->name + i))) && (((*(name + i)) != (*(current->name + i) + 32))))
            {
                check = true;
                break;
            }
        }
        if (check == false)
        {
            *id = current->id;
            return false;
        }
        current = current->next;
    }
    return true;
}

void UI(struct CustomerNode *customerRoot, struct ProductNode *productRoot)
{
    /*  This function is user interface. 
        There are 6 cases such as Add Customer, Add Basket, Remove Customer, 
        List the customers who bought a specific product, List the total shopping amounts of each customer and exit. 
    */
    int choice;
    char name[ELEMENT], surname[ELEMENT];
    int personId = 0;
    int productId = 0;
    int basketId = 0;
    int garbage = 0;

    struct CustomerNode *customerTemp = NULL;
    printf("\n--------------------\n");
    printf("1. Add a customer\n2. Add Basket\n3. Remove customer\n");
    printf("4. List the customers who bought a specific product\n5. List the total shopping amounts of each customer\n6. Exit\n");
    scanf(" %d", &choice);
    printf("--------------------\n");

    switch (choice)
    {
    case 1:
        personId = customerRoot->id + 1;
        listCustomer(customerRoot);
        printf("Please enter a name and surname (Name Surname): ");
        scanf(" %s %s", name, surname);
        //check for unique name
        if (customerSearchByName(customerRoot, name, &garbage))
        {
            pushCustomer(&customerRoot, personId, name, surname);
            printf("\nCustomer added\n");
            listCustomer(customerRoot);
            break;
        }
        printf("%s is already exist", name);
        break;
    case 2:
        listCustomer(customerRoot);
        printf("Please enter customer id: ");
        scanf(" %d", &personId);
        listProduct(productRoot);
        customerTemp = CustomerSearch(customerRoot, personId);
        if (customerTemp->basketHead == NULL)
        {
            //if basket does not exist create a basket first
            pushBasket(&customerTemp->basketHead, 1);
            //new basket's id is 1
            basketId = customerTemp->basketHead->id;
        }
        //if at least 1 basket exist new basket's id is last basket + 1
        else
            basketId = customerTemp->basketHead->id + 1;

        while (1)
        {
            printf("Please enter product id: ");
            scanf(" %d", &productId);
            if (productId == -1)
                break;
            createBasket(customerRoot, productRoot, personId, basketId, productId);
            printf("Product added to basket\n");
        }
        break;
    case 3:

        listCustomer(customerRoot);
        printf("\n");
        printf("Please enter a name and surname (Name Surname): ");
        scanf(" %s %s", name, surname);
        customerSearchByName(customerRoot, name, &personId);
        removeCustomer(&customerRoot, customerRoot, personId);
        listCustomer(customerRoot);
        break;
    case 4:
        //list customers's specific product
        listProduct(productRoot);
        printf("Please enter product id: ");
        scanf(" %d", &productId);
        findProduct(customerRoot, productId);
        break;
    case 5:

        listAmount(customerRoot);
        break;
    case 6:

        return;
    default:
        printf("Please enter a valid integer");
        break;
    }
    UI(customerRoot, productRoot);
    return;
}

int main()
{
    /*  In main function there are three while loop to read given text files and take them as input
    */
    int i, j;
    int rows = 0;
    int columns = 0;

    struct CustomerNode *customerRoot = NULL;
    struct ProductNode *productRoot = NULL;
    struct BasketNode *basketNode = NULL;
    struct CustomerNode *customerTemp = NULL;

    FILE *product = fopen("product.txt", "r");
    FILE *customer = fopen("customer.txt", "r");
    FILE *basket = fopen("basket.txt", "r");

    while (!feof(customer))
    {
        int id;
        char name[ELEMENT], surname[ELEMENT];
        fscanf(customer, "%d %s %s", &id, name, surname);
        if (customerRoot != NULL)
        {
            if (customerRoot->id == id)
                continue;
        }
        pushCustomer(&customerRoot, id, name, surname);
    }

    fclose(customer);

    while (!feof(product))
    {
        int id, price;
        char name[ELEMENT], category[ELEMENT];
        fscanf(product, "%d %s %s %d", &id, name, category, &price);

        if (productRoot != NULL)
        {
            if (productRoot->id == id)
                continue;
        }
        pushProduct(&productRoot, id, name, category, price);
    }

    fclose(product);

    productCompare(productRoot);

    while (!feof(basket))
    {
        int personId, basketId, productId;
        fscanf(basket, "%d %d %d", &personId, &basketId, &productId);
        createBasket(customerRoot, productRoot, personId, basketId, productId);
    }

    fclose(basket);

    UI(customerRoot, productRoot);
    return 0;
}
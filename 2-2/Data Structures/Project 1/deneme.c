#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <stdbool.h>

#define ELEMENT 50
#define LINE 256

struct CustomerNode;
struct ProductNode;
struct BasketNode;


//1.add customer to the end , create empty basket for new customer, After adding new customer, print all customers again.
//2.Products must be inserted to product linked list alphabetically ordered according to product name.



struct CustomerNode
{ //customer stack
    int id;
    char *name;
    char *surname;
    //Basket Linkedlist -->
    struct BasketNode *basketHead;
    struct CustomerNode *next;
};

struct ProductNode{
    int id;
    char *name;
    char *category;
    int price;
    struct ProductNode *next;
};

struct BasketNode{
    int id;
    int amount;
    struct ProductNode *productListHead;
    struct BasketNode *next;
};

struct CustomerNode *newCustomer(int id,const char *name,const char *surname)
{ //Function to create new customer node

    struct CustomerNode *customerNode = (struct CustomerNode *)malloc(sizeof(struct CustomerNode));

    customerNode->id = id;

    customerNode->name = (char*) calloc(strlen(name),sizeof(char));
    strncpy(customerNode->name,name,strlen(name));

    customerNode->surname = (char*)calloc(strlen(surname),sizeof(char));
    strncpy(customerNode->surname,surname,strlen(surname));

    //add basket list
    customerNode->next = NULL;
    customerNode->basketHead = NULL;
    return customerNode;
}

int isCustomerEmpty(struct CustomerNode *root)
{
    return !root;
}

void pushCustomer(struct CustomerNode** root, int id, const char *name,const char *surname)
{
    struct CustomerNode* customerNode = newCustomer(id, name,surname);
    customerNode->next = *root;

    *root = customerNode;
}

int popCustomer(struct CustomerNode **root)
{
    if (isCustomerEmpty(*root))
        return INT_MIN;
    struct CustomerNode* temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
}

struct ProductNode *newProduct(int id,const char *name, const char *category, int price){

    struct ProductNode *productNode = (struct ProductNode *)malloc(sizeof(struct ProductNode));

    productNode->id = id;

    productNode->name = (char*)calloc(strlen(name),sizeof(char));
    strncpy(productNode->name,name,strlen(name));

    productNode->category = (char*)calloc(strlen(category),sizeof(char));
    strncpy(productNode->category,category,strlen(category));

    productNode->price = price;
    productNode->next =NULL;

    return productNode;

}

int isProductEmpty(struct ProductNode* root){
    return !root;

}

void pushProduct(struct ProductNode** root, int id, const char *name,const char *category, int price){

    struct ProductNode* productNode = newProduct(id,name,category,price);
    productNode->next = *root;
    *root = productNode;
}

int popProduct(struct ProductNode** root){
    if(isProductEmpty(*root))
        return INT_MIN;
    struct ProductNode* temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
    return popped;
}

struct BasketNode *newBasket(int id){

    struct BasketNode *basketNode = (struct BasketNode *)malloc(sizeof(struct BasketNode));

    basketNode->id = id;
    basketNode->next = NULL;
    basketNode->productListHead = NULL;
    return basketNode;
}

int isBasketEmpty(struct BasketNode *root){
    return !root;
}

void pushBasket(struct BasketNode** root, int id){

    struct BasketNode* basketNode = newBasket(id);
    basketNode->next = *root;

    *root = basketNode;
}

int popBasket(struct BasketNode **root){

    if(isBasketEmpty(*root))
        return INT_MIN;
    struct BasketNode* temp = *root;
    *root = (*root)->next;
    int popped = temp->id;
    free(temp);
}

struct CustomerNode *CustomerSearch(struct CustomerNode* root, int id){

    struct CustomerNode* current = root;

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

struct BasketNode *BasketSearch(struct BasketNode* root,int id){

    struct BasketNode* current = root;

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

struct ProductNode *ProductSearch(struct ProductNode* root,int id){

    struct ProductNode* current = root;

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

bool createBasket(struct CustomerNode* customerRoot,struct ProductNode* productRoot, int personId, int basketId, int productId){
    struct CustomerNode* customerTemp = CustomerSearch(customerRoot,personId);
    struct ProductNode* productInfo = ProductSearch(productRoot,productId);
    //customerTemp'de ki değişiklik fonksiyon parametresi customerRoot üzerinde gözükmüyor

    if(customerTemp == NULL){
        printf("Customer does not exist\n");
        return false;
    }
    if(customerTemp->basketHead == NULL){
        printf("basket yok\n");
        pushBasket(&customerTemp->basketHead,basketId);
        printf("basket id: %d", customerTemp->basketHead->id);
    }
    printf("basket id: %d", customerRoot->basketHead->id); // burda yazdırmıyor
    struct BasketNode* currentBasket = BasketSearch(customerTemp->basketHead,basketId);
    printf("struct sonra");
    pushProduct(&(currentBasket->productListHead),productInfo->id,productInfo->name,productInfo->category,productInfo->price);
    printf("puşttan sonra\n");


}

int main() {
    int i,j;
    int rows = 0;
    int columns = 0;

    struct CustomerNode* customerRoot = NULL;
    struct ProductNode* productRoot = NULL;
    struct BasketNode* basketNode = NULL;


    FILE *product = fopen("product.txt", "r");
    FILE *customer = fopen("customer.txt", "r");
    FILE *basket = fopen("basket.txt", "r");

    while(!feof(customer)) {
        int id;
        char name[ELEMENT], surname[ELEMENT];
        fscanf(customer, "%d %s %s",  &id, name, surname);
        if (customerRoot != NULL){
            if(customerRoot->id == id)
                continue;
        }

        pushCustomer(&customerRoot,id,name,surname);
    }

    fclose(customer);

    /* customerTemp = CustomerSearch(root,3);
     printf("%s",customerTemp->name);*/

    while(!feof(product)) {
        int id, price;
        char name[ELEMENT], category[ELEMENT];
        fscanf(product, "%d %s %s %d",  &id, name, category, &price);
        //printf("%d %s %s %d\n",	id, name, category, price);
        if(productRoot != NULL){
            if (productRoot->id == id)
                continue;
        }

        pushProduct(&productRoot,id,name,category,price);
        //printf("%d %s %s %d\n",productRoot->id,productRoot->name,productRoot->category,productRoot->price);
    }

    fclose(product);


    /*productTemp = ProductSearch(productRoot,4);
    printf("Product Found -> %d %s",productTemp->id,productTemp->name);
	*/

    /*while(!feof(basket)) {
        int personId, basketId, productId;
        fscanf(basket, "%d %d %d",  &personId, &basketId, &productId);
        createBasket(customerRoot,personId,basketId,productId);
    }

    fclose(basket);*/

    createBasket(customerRoot,productRoot,1,1,1);
    //printf("hello");
    //printf("customer id: %d, basket id: %d, product id: %d, product name: %s\n ",customerRoot->id,customerRoot->basketHead->id,customerRoot->basketHead->productListHead->id,customerRoot->basketHead->productListHead->name);
    //customer var mı ?
    //customer'ın o sepeti var mı? yoksa sepeti oluştur  varsa o sepete id si verilen product'ı ekle-- productlist'e eklicek


    /*char bla[] = "hello";
    char blabla[] = "world";
    pushCustomer(&root,1,bla,blabla);*/
}
// 도서 관리 프로그램을 만들어보자.
#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct Book
{
    int booknum;
    char *bookname;
    char *author;
    char *publisher;
} Book;

Book **myptr;
Book **bookptr;
int booknum = 0;
int len = 0;

void init()
{
    bookptr = (Book **)malloc(sizeof(Book *) * 100);
    myptr = (Book **)malloc(sizeof(Book *) * 100);
}

void addbook(const char *bookname, const char *author, const char *publisher)
{
    if (booknum > 100){
        printf("book over...\n");
        return;
    }
    bookptr[booknum] = (Book *)malloc(sizeof(Book));
    bookptr[booknum]->bookname = (char *)malloc(sizeof(char) * (strlen(bookname) + 1));
    bookptr[booknum]->author = (char *)malloc(sizeof(char) * (strlen(author) + 1));
    bookptr[booknum]->publisher = (char *)malloc(sizeof(char) * (strlen(publisher) + 1));

    bookptr[booknum]->booknum = booknum;
    strcpy(bookptr[booknum]->bookname, bookname);
    strcpy(bookptr[booknum]->author, author);
    strcpy(bookptr[booknum++]->publisher, publisher);
}

void searchig_bookname(const char *bookname)
{
    for (int i = 0; i < booknum; i++)
    {
        if (!strcmp(bookptr[i]->bookname, bookname)){
            printf("BookName: %s exist in library\n", bookname);
            break;
        }
    }
}

void searching_author(const char *author)
{
    for (int i = 0; i < booknum; i++)
    {
        if (!strcmp(bookptr[i]->author, author)){
            printf("BookAuthor: %s exist in library\n", author);
            break;
        }
    }
}

void searching_publisher(const char *publisher)
{
    for (int i = 0; i < booknum; i++)
    {
        if (!strcmp(bookptr[i]->publisher, publisher)){
            printf("BookPublisher: %s exist in library\n", publisher);
            break;
        }
    }
}

void show_all_bookinfo()
{
    for (int i = 0; i < booknum; ++i)
    {
        printf("Book ID       : %d\n", bookptr[i]->booknum);
        printf("Book Name     : %s\n", bookptr[i]->bookname);
        printf("Book Author   : %s\n", bookptr[i]->author);
        printf("Book Publihser: %s\n\n", bookptr[i]->publisher);
    }
}

int main(void)
{
    init();
    for (int i=0; i< 103; i++)
        addbook("Say your story", "Goo", "ScalaWox");
    // searchig_bookname("Say your story");
    // searching_author("Goo");
    // searching_publisher("ScalaWox");
    // show_all_bookinfo();
    return 0;
}
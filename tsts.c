#include<stdio.h>
#include<string.h>

int main()
{
    char a[100];
    char * b;
    strcpy(a,"this is a test");
    b=a;
    b = b + strlen(b)-3 ;
    printf("%s ",b);
    return 0;
}
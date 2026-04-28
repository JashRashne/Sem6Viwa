%{
#include <stdio.h>
#include <string.h>

char str[100];
%}

%%
[a-zA-Z]+     { strcpy(str, yytext); }
\n            {
                 int i, len, flag = 1;
                 len = strlen(str);

                 for(i = 0; i < len/2; i++) {
                     if(str[i] != str[len-i-1]) {
                         flag = 0;
                         break;
                     }
                 }

                 if(flag)
                     printf("Palindrome\n");
                 else
                     printf("Not Palindrome\n");
              }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a string: ");
    yylex();
    return 0;
}
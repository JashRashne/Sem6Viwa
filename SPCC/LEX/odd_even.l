%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]+    {
             int num = atoi(yytext);
             if(num % 2 == 0)
                 printf("Even Number\n");
             else
                 printf("Odd Number\n");
          }

[ \t\n]+  { /* ignore whitespace */ }

.         { printf("Invalid input\n"); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a number: ");
    yylex();
    return 0;
}
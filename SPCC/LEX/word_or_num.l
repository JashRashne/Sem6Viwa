%{
#include <stdio.h>
%}

%%
[0-9]+          { printf("Number\n"); }
[a-zA-Z]+       { printf("Word\n"); }
.|\n            { printf("Invalid input\n"); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a string: ");
    yylex();
    return 0;
}
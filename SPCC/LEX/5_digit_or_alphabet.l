%{
#include <stdio.h>
%}

%%
[0-9]          { printf("Digit\n"); }
[a-zA-Z]       { printf("Alphabet\n"); }
.              { printf("Invalid input\n"); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a character: ");
    yylex();
    return 0;
}
%{
#include <stdio.h>

int vowels = 0;
%}

%%
[aAeEiIoOuU]    { vowels++; }
.|\n            { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a string (Ctrl+D to end):\n");
    yylex();
    
    printf("Number of vowels: %d\n", vowels);
    return 0;
}
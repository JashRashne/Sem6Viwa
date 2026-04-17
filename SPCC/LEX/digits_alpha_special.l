%{
#include <stdio.h>

int digits = 0;
int alphabets = 0;
int special = 0;
%}

%%
[0-9]              { digits++; }
[a-zA-Z]           { alphabets++; }
[ \t\n]            { /* ignore whitespace */ }
.                  { special++; }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter input (Ctrl+D to end):\n");
    yylex();

    printf("\nDigits: %d\n", digits);
    printf("Alphabets: %d\n", alphabets);
    printf("Special Symbols: %d\n", special);

    return 0;
}
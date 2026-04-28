%{
#include <stdio.h>
%}

%%
[a-zA-Z0-9 \t\n]     { /* Ignore alphabets, digits, whitespace */ }

[^a-zA-Z0-9 \t\n]    { printf("Special Character: %s\n", yytext); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter input (Ctrl+D to end):\n");
    yylex();
    return 0;
}
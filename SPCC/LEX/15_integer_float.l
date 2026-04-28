%{
#include <stdio.h>
%}

%%
[0-9]+"."[0-9]+      { printf("Floating Point Number: %s\n", yytext); }

[0-9]+               { printf("Integer: %s\n", yytext); }

[ \t\n]+             { /* ignore whitespace */ }

.                    { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter input (Ctrl+D to end):\n");
    yylex();
    return 0;
}
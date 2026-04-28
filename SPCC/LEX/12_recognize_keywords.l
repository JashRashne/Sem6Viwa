%{
#include <stdio.h>
%}

%%
"int"|"float"|"char"|"if"|"else"|"while"|"return"   { printf("Keyword: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*                             { printf("Identifier: %s\n", yytext); }

[ \t\n]+                                           { /* ignore whitespace */ }

.                                                  { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter input (Ctrl+D to end):\n");
    yylex();
    return 0;
}
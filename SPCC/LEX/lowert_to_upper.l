%{
#include <stdio.h>
%}

%%
[a-z]      { printf("%c", yytext[0] - 32); }
[A-Z]      { printf("%c", yytext[0]); }
\n         { printf("\n"); }
.          { printf("%c", yytext[0]); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter text (Ctrl+D to end):\n");
    yylex();
    return 0;
}
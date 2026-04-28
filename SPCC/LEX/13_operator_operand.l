%{
#include <stdio.h>

int operators = 0;
int operands = 0;
%}

%%
"+"|"-"|"*"|"/"|"="|"%"    { operators++; }

[0-9]+                    { operands++; }   /* numbers */

[a-zA-Z_][a-zA-Z0-9_]*    { operands++; }   /* identifiers */

[ \t\n]+                  { /* ignore whitespace */ }

.                         { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter expression (Ctrl+D to end):\n");
    yylex();

    printf("\nOperators: %d\n", operators);
    printf("Operands: %d\n", operands);

    return 0;
}
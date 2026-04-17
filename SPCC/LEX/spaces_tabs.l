%{
#include <stdio.h>

int spaces = 0;
int tabs = 0;
%}

%%
" "        { spaces++; }
"\t"       { tabs++; }
\n         { /* ignore newline */ }
.          { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter text (Ctrl+D to end):\n");
    yylex();

    printf("\nNumber of spaces: %d\n", spaces);
    printf("Number of tabs: %d\n", tabs);

    return 0;
}
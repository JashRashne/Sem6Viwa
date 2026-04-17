%{
#include <stdio.h>
%}

%%
[aAeEiIoOuU]    { printf("Vowel\n"); }
[a-zA-Z]        { printf("Consonant\n"); }
.               { printf("Not an alphabet\n"); }
%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter a character: ");
    yylex();
    return 0;
}
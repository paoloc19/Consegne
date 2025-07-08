#include <stdio.h>
int main(){
    int numero1;
    int numero2;
    int somma;
    int media;

    printf("Scegli il primo numero: ");
    scanf("%d", &numero1);
    printf("\nPerfetto, ora dammi il secondo numero: ", numero1);
    scanf("%d", &numero2);

    somma = numero1 + numero2;

    printf("\nOttimo la somma è: %d", somma);

    printf("\nSe sei interessato la media aritmetica dei tuoi numeri è: %0.1f", (float)somma / 2);
    
    return 0;
}
#include <stdio.h>

int main(){
    int i, quantidades;
    int velocidades[100];
    int duracao;
    int limite;
    int vel_maxima = 0;

    scanf("%d", &quantidades);

    for (i = 0; i < quantidades; i++){
        scanf("%d", &velocidades[i]);
    }

    scanf("%d", &duracao);

    if (duracao == 1){
        limite = 100;
    }
    else if (duracao == 2){
        limite = 20;
    }
    else{
        limite = 10;
    }

    for (i = 0; i < quantidades; i++){
        if (velocidades[i] > vel_maxima && velocidades[i] <= limite){
            vel_maxima = velocidades[i];
        }
    }

    printf("%d\n", vel_maxima);
}
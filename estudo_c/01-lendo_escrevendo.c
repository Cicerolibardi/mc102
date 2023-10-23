#include <stdio.h>

void main(){
    float operando1, operando2;
    float resultado;
    char operador;
    int repeticoes;
    int i;

    scanf("%d", &repeticoes);
    for (i = 0; i < repeticoes; i++){
        scanf("%f %c %f", &operando1, &operador, &operando2);
        if (operador == '/') {
            resultado = operando1 / operando2;
            printf("%.1f\n", resultado);
        }
        else if (operador == '+'){
            resultado = operando1 + operando2;
            printf("%.1f\n", resultado);
        }
        else if (operador == '-'){
            resultado = operando1 - operando2;
            printf("%.1f\n", resultado);
        }
        else if (operador == '*'){
            resultado = operando1 * operando2;
            printf("%.1f\n", resultado);
        }
    }
}
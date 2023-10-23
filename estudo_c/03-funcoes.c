#include <stdio.h>

#define MAX_ALUNOS 100

float ler_media(int m){
    int i;
    float media, nota;
    media = 0;
    for (i = 0; i < m; i++){
        scanf("%f", &nota);
        media += nota;
    }
    media = media / m;
    return media;
}

void ler_notas_P(float P[MAX_ALUNOS], int n){
    int i;
    for (i = 0; i < n; i++){
        P[i] = ler_media(3);
    }
}

void ler_notas_T(float T[MAX_ALUNOS], int n){
    int i;
    for (i = 0; i < n; i++){
        T[i] = ler_media(2);
    }
}

void multiplicar_fator(float vetor_notas[MAX_ALUNOS], float fator, int num_notas){
    int i;
    for (i = 0; i < num_notas; i++){
        vetor_notas[i] = vetor_notas[i] * fator;
    }
}

float achar_maxima(float vetor_notas[MAX_ALUNOS], int num_notas){
    float maxima;
    int i;
    maxima = 0;
    for (i = 0; i < num_notas; i++){
        if (vetor_notas[i] > maxima){
            maxima = vetor_notas[i];
        }
    }
    return maxima;
}   

void imprimir_medias_finais(float T[MAX_ALUNOS],float P[MAX_ALUNOS], int num_notas){
    int i;
    float nota_final;
    for (i = 0; i < num_notas; i++){
        nota_final = (P[i] + T[i])/2;
        printf("%.1f\n", nota_final);
    }
}

float achar_media(float vetor_notas[MAX_ALUNOS], int num_notas){
    int i;
    float media;
    media = 0;
    for (i = 0; i < num_notas; i++){
        media += vetor_notas[i];
    }
    media = media / 2;

    return media;
}

int main(){
    int num_notas;
    float P[MAX_ALUNOS];
    float T[MAX_ALUNOS];
    float max_T, max_P, media_P, media_T;
    
    scanf("%d", &num_notas);

    ler_notas_P(P, num_notas);
    ler_notas_T(T, num_notas);

    multiplicar_fator(P, 1.1, num_notas);
    
    max_T = achar_maxima(T, num_notas);
    multiplicar_fator(T, (10/max_T), num_notas);

    imprimir_medias_finais(T, P, num_notas);

    max_T = achar_maxima(T, num_notas);
    max_P = achar_maxima(P, num_notas);

    media_P = achar_media(P, num_notas);
    media_T = achar_media(T, num_notas);

    printf("MAX P: %.1f\n", max_P);
    printf("MAX T: %.1f\n", max_T);
    printf("MEDIA P: %.1f\n", media_P);
    printf("MEDIA T: %.1f\n", media_T);

}
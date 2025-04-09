#include "processamento.h"

// calcular a media (pontos de jogos) // 
float calcular_media(int* pontos, int tamanho) {
    if (tamanho <= 0) {
        return 0.0; //manda 0.0 se estiver zerado ou invalido //
    }

    int soma = 0;
    for (int i = 0; i < tamanho; i++) {
        soma += pontos[i]; // somar todos os pontos // 
    }

    return (float)soma / tamanho;
}

// maior valor em uma lista

int encontrar_maximo(int* pontos, int tamanho) {
    if (tamanho <= 0) {
        return -1;
    }

    int maximo = pontos[0];
    for (int i=1; i < tamanho; i++) {
        if (pontos[i] > maximo) {
            maximo = pontos[i];
        }
    }
    return maximo;
}


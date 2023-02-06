#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "qAgenda.h"
#include "listas.h"

struct no
{
    // Geral
    char nome[128];
    char setor[128];
    int senha;
    // Cliente
    int cpf_cnpj;
    int idade;
    // Empresa
    int horario;

    struct no *prox;
};

struct lista
{
    No *inicio;
    No *fim;
    int tam;
};
/*
    CriarNo() ao chamada retorna um novo nó
*/
No *criarNo(void){
    No *ptr = (No*)malloc(sizeof(No)); // Aloca o novo no
    if(ptr == NULL){ 
        printf("Erro de Alocação\n");
        exit(-1);
    }else{ // retorta o no
        return ptr;
    }
}

List *criarListaVazia(void){
    List *l = (List*)malloc(sizeof(List)); // Aloca a lista
    // Zera os valores da Lista
    l->inicio = NULL;
    l->fim = NULL;
    l->tam = 0;
    return l;
}

List *criarListaChave(No *ptr){
	List *l = (List *)malloc(sizeof(List)); // Aloca a lista
    if(l != NULL){
        // Atualiza os valores da lista
        l->inicio = ptr;
        l->fim = ptr;
        l->tam++;
    }
    return l;
}

void addInicio(List *l, No *ptr){
    ptr->prox = NULL; // Verifica ele como null
    if(l->inicio == NULL){
        l->inicio = ptr;
        l->fim = ptr;
    }else{
        ptr->prox = l->inicio; // O novo nó vai apontar para o primeiro da lista
        l->inicio = ptr; // A lista é atualizada com o novo nó
    }
    l->tam++;
}

void addFim(List *l, No *ptr){
    ptr->prox = NULL;
    if(l->fim == NULL){
        l->inicio = ptr;
    }else{
        l->fim->prox = ptr; // O ultimo da lista aponta para o novo
    }
    l->fim = ptr; // O ultimo é atualizado
    l->tam++;
}

void addChaveAntes(List *l, int id, No *ptr){ // Passa a lista, a determinada célula e o novo nó
    No *anterior, *aux;
    aux = l->inicio;
    anterior = aux;

    while (aux->cpf_cnpj != id){ // procura o nó passado
        anterior = aux;
        aux = aux->prox;
        if(aux == NULL){
            printf("Erro no identificador: %d \n", id);
            exit(-1);
        }
    }
    ptr->prox = aux; // atualiza o novo Nó na lista
    anterior->prox = ptr; // Faz o anterior apontar para o Novo
    l->tam++;
}

void addChaveDepois(List *l, int identidade, No *ptr){
    No *posterior, *aux;
    aux = l->inicio;
    posterior = aux->prox;

    while(aux->cpf_cnpj != identidade){
        aux = aux->prox; // Atualiza o auxiliar
        posterior = aux->prox; // Descobre o o proximo nó
        if(aux == NULL){
            printf("Erro no identificador: %d \n", identidade);
            exit(-1);
        }
    }
    ptr->prox = posterior->prox; // O novo nó é inserido na lista
    posterior->prox = ptr; // O posterior aponta para o novo
    l->tam++;
}

No* retornarValor(List *l, int chave){
    No *aux = l->inicio;
    while(aux->cpf_cnpj != chave){ // procura a chave passada
        aux = aux->prox;
    }
    return aux; // retornar o nó encontrado;
}

void removerCelula(List *l, int chave){
    No *antes, *depois, *ptr;
    ptr = l->inicio;
    while(ptr->cpf_cnpj != chave){ // Procura a celula
        antes = ptr;
        ptr = ptr->prox;
        depois = ptr->prox;
        if(ptr == NULL){ // Se ela não tiver na lista, nada acontece
            return;
        }
    }
    antes->prox = depois; // Retira ela da lista
    ptr = NULL; // Apaga ela
    free(ptr);
}

void removerInicio(List *l){
    No *ptr = l->inicio;

    if(ptr->prox == NULL){
        ptr = NULL;
        free(ptr);
    }else{
        l->inicio = ptr->prox; // O primeiro vai apontar para o segundo
        ptr = NULL; // o primeiro é liberado
        free(ptr);
    }
    l->tam--;
}

void removerFim(List *l){
    No *penultimo, *ptr = l->inicio;

    if(ptr->prox == NULL){ // Verifica se só existe um nó na fila
        ptr = NULL;
        free(ptr);
    }else{
        while(ptr != l->fim){ // procura o ultimo e penultimo
            penultimo = ptr;
            ptr = ptr->prox;
        }
        penultimo->prox = NULL; // Faz o penultimo apontar para NULL
        l->fim = penultimo;
        free(ptr); // Libera o ultimo no
    }
}

List* concatenarListas(List *a, List *b){
    No *ptr, *aux;
    aux = criarNo();
    if(a->fim == b->fim){ // a ultima é igual a primeira
        return a;
    }
    a->fim->prox = b->inicio; // associo o ultimo nó da a ao inicio da b
    ptr = a->fim->prox;
    while (ptr->prox != NULL){ // procuro o ultimo nó da lista
        ptr = ptr->prox;
    }
    a->fim = ptr; // faço ele ser o final
    a->tam = a->tam + b->tam; // somo os tamanhos
    return a;
}


void printLista(List *l){
    No *aux;
    aux = l->inicio;
    while (aux != NULL){ // percorre a lista printando cada item
        printf("%s ", aux->cpf_cnpj);
        aux = aux->prox;
    }
    printf("\n");
}

int tamanhoLista(List *l){
    return l->tam;
}

void destruirLista(List *l){
    No *aux = l->inicio;
    while(aux != NULL){
        removerFim(l);
        aux = aux->prox;
    }
    free(l);
}


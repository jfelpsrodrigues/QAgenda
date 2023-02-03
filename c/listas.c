#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "qAgenda.h"
#include "listas.h"

struct endereco
{
    char rua[128];
    char setor[128];
    char cidade[128];
    char estado[128];
    char cep[10];
};

struct cadastro
{
    char nome[128];
    End *endereco;
};

struct no
{
    Cad *chave;
    char servico[128];
    char horario[5];
    char str[10]; // A string armazenada no nó
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

List *criarListaChave(int chave, char str[]){
	List *l = (List *)malloc(sizeof(List)); // Aloca a lista
    No *ptr = criarNo();
    if(l != NULL){
        // Atualiza os valores do no criado
        ptr->chave = chave;
        strcpy(ptr->str, str);
        // Atualiza os valores da lista
        l->inicio = ptr;
        l->fim = ptr;
        l->tam++;
    }
    return l;
}

void addInicio(List *l, int chave, char str[]){
    // Criando um No
    No* ptr = criarNo();
    ptr->chave = chave;
    strcpy(ptr->str, str);
    ptr->prox = NULL;    
    if(l->inicio == NULL){
        l->inicio = ptr;
        l->fim = ptr;
    }else{
        ptr->prox = l->inicio; // O novo nó vai apontar para o primeiro da lista
        l->inicio = ptr; // A lista é atualizada com o novo nó
    }
    l->tam++;
}

void addFim(List *l, int chave, char str[]){
    No *ptr = criarNo();
    ptr->chave = chave;
    strcpy(ptr->str, str);
    ptr->prox = NULL;

    if(l->fim == NULL){
        l->inicio = ptr;
    }else{
        l->fim->prox = ptr; // O ultimo da lista aponta para o novo
    }
    l->fim = ptr; // O ultimo é atualizado
    l->tam++;
}

void addOrdemCres(List *l, int num, char str[]){
    No *ptr, *aux = l->inicio;
    ptr = criarNo();
    ptr->chave = num;
    strcpy(ptr->str, str);

    if(l->inicio == NULL || ptr->chave < l->inicio->chave){
        addInicio(l, num, str);
    }else{
        while(aux->prox != NULL && ptr->chave > aux->prox->chave){
            aux = aux->prox;
        }
        ptr->prox = aux->prox;
        aux->prox = ptr;
        while(aux->prox != NULL) aux = aux->prox;
        l->fim = aux;
    }
}

void addChaveAntes(List *l, int identidade, int novo, char str[]){ // Passa a lista, a determinada célula e o novo nó
    No *anterior, *aux, *ptrNovo = criarNo();
    ptrNovo->chave = novo;
    strcpy(ptrNovo->str, str);
    aux = l->inicio;
    anterior = aux;

    while (aux->chave != identidade){ // procura o nó passado
        anterior = aux;
        aux = aux->prox;
        if(aux == NULL){
            printf("Erro no identificador: %d \n", identidade);
            exit(-1);
        }
    }
    ptrNovo->prox = aux; // atualiza o novo Nó na lista
    anterior->prox = ptrNovo; // Faz o anterior apontar para o Novo
    l->tam++;
}

void addChaveDepois(List *l, int identidade, char novo[]){
    No *posterior, *aux, *ptrNovo = criarNo();
    strcpy(ptrNovo->str, novo);
    aux = l->inicio;
    posterior = aux->prox;

    while(aux->chave != identidade){
        aux = aux->prox; // Atualiza o auxiliar
        posterior = aux->prox; // Descobre o o proximo nó
        if(aux == NULL){
            printf("Erro no identificador: %d \n", identidade);
            exit(-1);
        }
    }
    ptrNovo->prox = posterior->prox; // O novo nó é inserido na lista
    posterior->prox = ptrNovo; // O posterior aponta para o novo
    l->tam++;
}

char* retornarValor(List *l, int chave){
    No *aux = l->inicio;
    while(aux->chave != chave){ // procura a chave passada
        aux = aux->prox;
    }
    return aux->str; // retornar o que está no nó;
}

void removerCelula(List *l, int chave){
    No *antes, *depois, *ptr;
    ptr = l->inicio;
    while(ptr->chave != chave){ // Procura a celula
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

List* ordenarLista(List *l){
    List *laux = criarListaVazia();
    No *ptr = l->inicio; // No para percorrer a lista
    while(ptr != NULL){
        addOrdemCres(laux, ptr->chave, ptr->str);
        ptr = ptr->prox;
    }
    free(l);
    return laux;
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
        printf("%s ", aux->str);
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


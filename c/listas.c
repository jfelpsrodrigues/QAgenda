#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "qAgenda.h"
#include "listas.h"

struct cadastro{
    // Geral
    char nome[128];
    char bairro[128];
    int senha;
    // Cliente
    long int cpf_cnpj;
    int idade;
    // Estabelecimento
    char ramo[128];
    int horario;
    int dia;
};

struct no
{
    Cad dados;
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

List *criarListaChave(Cad a){
	List *l = (List *)malloc(sizeof(List)); // Aloca a lista
    No *ptr = criarNo();
    ptr->dados = a;
    if(l != NULL){
        // Atualiza os valores da lista
        l->inicio = ptr;
        l->fim = ptr;
        l->tam++;
    }
    return l;
}

void addInicio(List *l, Cad a){
    No *ptr = criarNo();
    ptr->prox = NULL; // Verifica ele como null
    ptr->dados = a;
    if(l->inicio == NULL){
        l->inicio = ptr;
        l->fim = ptr;
    }else{
        ptr->prox = l->inicio; // O novo nó vai apontar para o primeiro da lista
        l->inicio = ptr; // A lista é atualizada com o novo nó
    }
    l->tam++;
}

void addFim(List *l, Cad a){
    No *ptr = criarNo();
    ptr->dados = a;
    ptr->prox = NULL;
    if(l->fim == NULL){
        l->inicio = ptr;
    }else{
        l->fim->prox = ptr; // O ultimo da lista aponta para o novo
    }
    l->fim = ptr; // O ultimo é atualizado
    l->tam++;
}

void addChaveAntes(List *l, int id, Cad a){ // Passa a lista, a determinada célula e o novo nó
    No *anterior, *aux, *ptr = criarNo();
    ptr->dados = a;
    aux = l->inicio;
    anterior = aux;

    while (aux->dados.cpf_cnpj != id){ // procura o nó passado
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

void addChaveDepois(List *l, int identidade, Cad a){
    No *posterior, *aux, *ptr = criarNo();
    aux = l->inicio;
    posterior = aux->prox;

    while(aux->dados.cpf_cnpj != identidade){
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

Cad retornarValor(List *l, int chave){
    No *aux = l->inicio;
    while(aux->dados.cpf_cnpj != chave){ // procura a chave passada
        aux = aux->prox;
    }
    return aux->dados; // retornar o nó encontrado;
}

Cad retornarValorInicial(List *l){
    return l->inicio->dados;
}

void removerCelula(List *l, long int chave){
    No *aux, *ptr = NULL;
    if(l->inicio){
        if(l->inicio->dados.cpf_cnpj == chave){
            ptr = l->inicio;
            l->inicio = ptr->prox;
            free(ptr);
            l->tam--;
        }else{
            aux = l->inicio;
            while (aux->prox && aux->prox->dados.cpf_cnpj != chave)
            {
                aux = aux->prox;
            }
            if(aux->prox){
                ptr = aux->prox;
                aux->prox = ptr->prox;
                free(ptr);
                l->tam--;
            }
        }
    }
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

void printLista(List *l){
    No *aux;
    aux = l->inicio;
    while (aux != NULL){ // percorre a lista printando cada item
        printf("CPF/CNPJ: %ld - Nome: %s\n", aux->dados.cpf_cnpj, aux->dados.nome);
        aux = aux->prox;
    }
}

void printListaAgenda(List *l){
    No *aux;
    aux = l->inicio;
    while (aux != NULL){ // percorre a lista printando cada item
        printf("CPF/CNPJ: %ld - Dia: %d - Hora: %d\n", aux->dados.cpf_cnpj, aux->dados.dia, aux->dados.horario);
        aux = aux->prox;
    }
}

int tamanhoLista(List *l){
    return l->tam;
}

void destruirLista(List *l){
    free(l);
}

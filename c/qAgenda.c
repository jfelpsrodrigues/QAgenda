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

List *LeListaLojas(){
    Cad estabelecimento;
    List *l = criarListaVazia();
    FILE *file = fopen("files/estabelecimentos.csv", "r+");
    if(file == NULL) exit(1);

    while(fscanf(file, "%[^,],%ld,%[^,],%[^,],%d\n", estabelecimento.nome, &estabelecimento.cpf_cnpj, estabelecimento.ramo, estabelecimento.bairro, &estabelecimento.senha) != EOF){
        addFim(l, estabelecimento);
    }
    
    fclose(file);
    return l;
}

List *LeListaClientes(){
    Cad cliente;
    List *l = criarListaVazia();
    FILE *file = fopen("files/clientes.csv", "r+");
    if(file == NULL) exit(1);

    while(fscanf(file, "%[^,],%ld,%d,%[^,],%d\n", cliente.nome, &cliente.cpf_cnpj, &cliente.idade, cliente.bairro, &cliente.senha) != EOF){
        addFim(l, cliente);
    }
    
    fclose(file);
    return l;
}

void EscreveListaClientes(List *l){
    Cad a;
    FILE *arq = fopen("files/clientes.csv", "a+");
    if(arq == NULL) exit(1);

    a = retornarValorInicial(l);
    fprintf(arq, "%s,%ld,%d,%s,%d\n", a.nome, a.cpf_cnpj, a.idade, a.bairro, a.senha);
    fclose(arq);
}

void EscreveListaLojas(List *l){
    Cad a;
    FILE *arq = fopen("files/estabelecimentos.csv", "a+");
    if(arq == NULL) exit(1);

    a = retornarValorInicial(l);
    fprintf(arq, "%s,%ld,%s,%s,%d\n", a.nome, a.cpf_cnpj, a.ramo, a.bairro, a.senha);
    fclose(arq);
}

void CadastroLoja(List *t, char *name, char *bairro, char *ramo, long int cnpj, int senha){
    Cad a;

    strcpy(a.nome, name);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cnpj;
    strcmp(a.ramo, ramo);
    
    addFim(t, a);
}

void CadastroCliente(List *t, char *nome, char *bairro, int senha, long int cpf, int idade) {
    Cad a;

    strcpy(a.nome, nome);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cpf;
    a.idade = idade;
    
    addFim(t, a);
}

void RealizarAgendamento();

void OrdenacaoCliente();

void OrdenacaoLoja() {

    FILE* CL = fopen("files/estabelecimentos.csv", "r+");
    char buffer[100];
    char *temp;             //String para ordernamento
    char **registro;        //Matriz completa a ordenar
    char **ord_registro;    //matriz de informacoes ordenadas
    int n_linhas=0, count=0, count2=0, i, j;  //Variaveis de contagem

    if(CL == NULL) exit(1);

    //Contagem de linhas do arquivo para alocar dinamicamente
    while(fgets(buffer, 100, CL)) n_linhas++;

    //alocacao dinamica da matriz de linhas e colunas
    registro = (char**) calloc(n_linhas, sizeof(char*));
    for(i=0; i<n_linhas; i++) {
        registro[i] = (char*) calloc(100, sizeof(char));
    }

    ord_registro = (char**) calloc(n_linhas, sizeof(char*));
    for(i=0; i<n_linhas; i++) {
        ord_registro[i] = (char*) calloc(100, sizeof(char));
    }
    //--------------------------------------------------
    rewind(CL);                             //Retorna ao inicio do arquivo
    while(fgets(buffer, 100, CL)) {
        strcpy(registro[count], buffer);    //Matriz principal recebe a linha completa
        count++;
        temp = strtok(buffer, ",");         //Variavel recebe o parametro
        strcpy(ord_registro[count2], temp); //Matriz secundaria recebe o primeiro parametro
        count2++;
    }

    memset(temp, 0, sizeof(char));      //Limpar string
    for(j=1; j<n_linhas-1; j++) {       //Bubble sort para ordenar matrizes
        for(i=j+1; i<n_linhas; i++) {
            if(strcmp(ord_registro[j], ord_registro[i]) > 0) {
                strcpy(temp, ord_registro[j]);                  //Matriz secundaria 
                strcpy(ord_registro[j], ord_registro[i]);
                strcpy(ord_registro[i], temp);

                memset(temp, 0, sizeof(char));
                strcpy(temp, registro[j]);                      //Matriz principal
                strcpy(registro[j], registro[i]);
                strcpy(registro[i], temp);
            }
        }
    }

    rewind(CL);                         //Retorna ao inicio do arquivo
    for(i=0; i<n_linhas; i++) {         //Escrita no arquivo 
        fprintf(CL, "%s", registro[i]);
    }

    //--------------------------------------------------
    fclose(CL);

    //liberar matrizes
    for(i=0; i<n_linhas; i++) {
        free(registro[i]);
        free(ord_registro[i]);
    }
    free(registro);
    free(ord_registro);

}

void OrdenacaoAgendamento();

void RemoverAgendamento();

void RemoverLoja();

void RemoverCliente();

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
    int i, tam;
    FILE *arq = fopen("files/clientes.csv", "w");
    if(arq == NULL) exit(1);

    tam = tamanhoLista(l);
    for(i = 0; i < tam; i++){
        a = retornarValorInicial(l);
        fprintf(arq, "%s,%ld,%d,%s,%d\n", a.nome, a.cpf_cnpj, a.idade, a.bairro, a.senha);
        removerInicio(l);
    }
    fclose(arq);
}

void EscreveListaLojas(List *l){
    Cad a;
    int i, tam;
    FILE *arq = fopen("files/estabelecimentos.csv", "w");
    if(arq == NULL) exit(1);
    
    tam = tamanhoLista(l);
    for(i=0; i<tam; i++){
        a = retornarValorInicial(l);
        fprintf(arq, "%s,%ld,%s,%s,%d\n", a.nome, a.cpf_cnpj, a.ramo, a.bairro, a.senha);
        removerInicio(l);
    }
    fclose(arq);
}

void CadastroLoja(List *t, char *name, char *bairro, char *ramo, long int cnpj, int senha){
    Cad a;
    printf("tests\n");

    strcpy(a.nome, name);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cnpj;
    strcpy(a.ramo, ramo);
    
    addFim(t, a);
}

void CadastroCliente(List *t, char *nome, char *bairro, int senha, long int cpf, int idade) {
    Cad a;

    strcpy(a.nome, nome);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cpf;
    a.idade = idade;
    printf("%s\n", bairro);
    addFim(t, a);
}

void RealizarAgendamento();

void OrdenacaoCliente();

void OrdenacaoLoja();

void OrdenacaoAgendamento();

void RemoverAgendamento();

void RemoverLoja();

void RemoverCliente();

#include <stdio.h>
#include <stdlib.h>
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

void arquivo_cad_estabelecimento(){
    Cad estabelecimento;
    List *l = criarListaVazia();
    FILE *file;
    
    file = fopen("cad_estabelecimento.csv", "r+");
    if(file == NULL) return 1;

    while(fscanf(file, "%[^,],%ld,%[^,],%[^,],%d\n", estabelecimento.nome, &estabelecimento.cpf_cnpj, &estabelecimento.ramo, estabelecimento.bairro, &estabelecimento.senha) != EOF){
        addFim(l, estabelecimento);
    }
    
    escrita_arquivo(l, file);
    destruirLista(l);
    fclose(file);
}

void escrita_arquivo(List *l, FILE *arq);

void CadastroLoja();

void CadastroCliente(List *t,char *nome,char *bairro, int *senha, long int *cpf_cnpj, char *ramo) {
    Cad a;
    a.nome = nome;
    a.bairro = bairro;
    a.senha = senha;
    a.cpf_cnpj = cpf_cnpj;
    a.ramo = ramo;
   

    addFim(t, a);
    printf("\n");
}

void RealizarAgendamento();

void OrdenacaoCliente();

void OrdenacaoLoja();

void OrdenacaoAgendamento();

void RemoverAgendamento();

void RemoverLoja();

void RemoverCliente();

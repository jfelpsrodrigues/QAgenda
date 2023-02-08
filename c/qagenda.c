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

void CadastroCliente();

void RealizarAgendamento();

void OrdenacaoCliente();

void OrdenacaoLoja();

void OrdenacaoAgendamento();

void RemoverAgendamento();

void RemoverLoja();

void RemoverCliente();
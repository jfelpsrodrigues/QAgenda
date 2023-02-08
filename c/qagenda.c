#include <stdio.h>
#include <stdlib.h>
#include "qAgenda.h"

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

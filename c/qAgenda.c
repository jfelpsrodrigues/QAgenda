#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "qAgenda.h"
#include "listas.h"
#include "listas.c"

// struct cadastro{
//     // Geral
//     char nome[128];
//     char bairro[128];
//     int senha;
//     // Cliente
//     long int cpf_cnpj;
//     int idade;
//     // Estabelecimento
//     char ramo[128];
//     int horario;
//     int dia;
// };

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

void OrdenacaoLoja();

int compare(Cad dado1, Cad dado2) {         //Compara os dados passados
    if(dado1.dia < dado2.dia) return (1);
    if(dado1.dia == dado2.dia && dado1.horario < dado2.horario) return (1);

    return 0;
}

void inserir_ordenado(List *l, Cad dado) {  //Insere dados na lista ordenadamente
    No *aux, *novo = criarNo();     //No(s) auxiliar(es)

    if(novo) {                      //Caso o No tenha sido criado
        novo->dados = dado;         //No recebe os dados do parametro da funcao
        if(l->inicio == NULL) {     //Caso a lista esteja vazia
            novo->prox = NULL;
            l->inicio = novo;       //Passa os dados para o inicio
        }
        else if(compare(novo->dados, l->inicio->dados)) {   //Caso o valor dos dados passados sejam menores
            novo->prox = l->inicio;                         //que os do começo da lista
            l->inicio = novo;                               //Adiciona ao inicio
        }else{                      //Caso o valor dos dados passados sejam maiores
            aux = l->inicio;

            while((aux->prox) && (compare(novo->dados, aux->prox->dados) == 0)) {   //Enquanto os novos dados forem menores
                aux = aux->prox;    //Avanca a posicao na lista
            }

            novo->prox = aux->prox;
            aux->prox = novo;
        }
        l->tam++;
    }else{
        exit(1);
    }
}

void OrdenacaoAgendamento(char *fileName) {

    FILE *arq = fopen(fileName, "r+");
    Cad Agendamento;                    //Variavel de dados para registro
    No *aux = criarNo();                //No auxiliar para manipulacao da posicao na lista
    List *l = criarListaVazia();        //Lista principal

    if(arq == NULL) exit(1);                    //Finaliza caso o arquivo nao possa ser aberto

    while(fscanf(arq, "%d,%d,%ld,%[^\n]", &Agendamento.dia, &Agendamento.horario, &Agendamento.cpf_cnpj, Agendamento.nome) != EOF){
        inserir_ordenado(l, Agendamento);       //Insere os dados do arquivo na lista
    }
    aux = l->inicio;                            //No auxiliar recebe o inicio da lista

    rewind(arq);                                //Retorna ao inicio do arquivo
    while(aux) {
        fprintf(arq, "%02d, %04d, %ld, %s\n", aux->dados.dia, aux->dados.horario, aux->dados.cpf_cnpj, aux->dados.nome);
        aux = aux->prox;                        //Avanca a posicao da lista
    }

    destruirLista(l);                           //Libera a lista
    fclose(arq);                                //Fechamento do arquivo para finalizacao

}

void RemoverAgendamento();

void RemoverLoja();

void RemoverCliente();

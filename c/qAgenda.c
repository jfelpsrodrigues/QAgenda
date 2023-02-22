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

List *LeListaAgenda(char *file_name){
    Cad estabelecimento;
    List *l = criarListaVazia();
    FILE *file = fopen(file_name, "r+");
    if(file == NULL) exit(1);
    while(fscanf(file, "%d, %d, %ld,%s\n", &estabelecimento.dia, &estabelecimento.horario, &estabelecimento.cpf_cnpj, estabelecimento.nome) != EOF){
        addFim(l, estabelecimento);
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

void EscreveListaAgenda(char *file_name, List *l){
    Cad a;
    int i, tam;
    FILE *arq = fopen(file_name, "w");
    if(arq == NULL) exit(1);
    
    tam = tamanhoLista(l);
    for(i=0; i<tam; i++){
        a = retornarValorInicial(l);
        fprintf(arq, "%d,%d,%ld,%s\n", a.dia, a.horario, a.cpf_cnpj, a.nome);
        removerInicio(l);
    }
    fclose(arq);
}

void CadastroLoja(char *name, char *bairro, char *ramo, long int cnpj, int senha){
    List *t = LeListaLojas();
    Cad a;

    strcpy(a.nome, name);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cnpj;
    strcpy(a.ramo, ramo);
    
    addFim(t, a);
    EscreveListaLojas(t);
    destruirLista(t);
}

void CadastroCliente(char *nome, char *bairro, int senha, long int cpf, int idade) {
    List *t = LeListaClientes();
    Cad a;

    strcpy(a.nome, nome);
    strcpy(a.bairro, bairro);
    a.senha = senha;
    a.cpf_cnpj = cpf;
    a.idade = idade;
    addFim(t, a);
    EscreveListaClientes(t);
    destruirLista(t);
}

void RealizarAgendamento(char *file_name, int dia, int horario, long int cpf, char *name){
    List *l = LeListaAgenda(file_name);
    Cad a;
    a.dia = dia;
    a.horario = horario;
    a.cpf_cnpj = cpf;
    strcpy(a.nome, name);
    addFim(l, a);
    EscreveListaAgenda(file_name, l);
    destruirLista(l);
}

void OrdenacaoCliente() {

    FILE* CC = fopen("files/clientes.csv", "r+");
    char buffer[100];
    char *temp;             //String para ordernamento
    char **registro;        //Matriz completa a ordenar
    char **ord_registro;    //Matriz do primeiro parametro(nome)
    int n_linhas=0, count=0, count2=0, i, j;  //Variaveis de contagem

    if(CC == NULL) exit(1);

    //Contagem de linhas do arquivo para alocar dinamicamente
    while(fgets(buffer, 100, CC)) n_linhas++;

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
    rewind(CC);                         //Retorna ao inicio do arquivo
    while(fgets(buffer, 100, CC)) {
        strcpy(registro[count++], buffer);
        temp = strtok(buffer, ",");
        strcpy(ord_registro[count2++], temp);
    }

    memset(temp, 0, sizeof(char));      //Limpar string
    for(j=0; j<n_linhas-1; j++) {       //Bubble sort para ordenar matrizes
        for(i=j+1; i<n_linhas; i++) {
            if(strcmp(ord_registro[j], ord_registro[i]) > 0) {
                strcpy(temp, ord_registro[j]);           //Matriz secundaria com nome
                strcpy(ord_registro[j], ord_registro[i]);
                strcpy(ord_registro[i], temp);

                memset(temp, 0, sizeof(char));
                strcpy(temp, registro[j]);              //Matriz principal com todos os dados
                strcpy(registro[j], registro[i]);
                strcpy(registro[i], temp);
            }
        }
    }

    rewind(CC);                         //Retorna ao inicio do arquivo
    for(i=0; i<n_linhas; i++) {         //Escrita no arquivo 
        fprintf(CC, "%s", registro[i]);
    }

    //--------------------------------------------------
    fclose(CC);

    //liberar matrizes
    for(i=0; i<n_linhas; i++) {
        free(registro[i]);
        free(ord_registro[i]);
    }
    free(registro);
    free(ord_registro);

}

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
    for(j=0; j<n_linhas-1; j++) {       //Bubble sort para ordenar matrizes
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

void OrdenacaoAgendamento(char *file_name) {
    FILE *arq = fopen(file_name, "r+");
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

void RemoverAgendamento(char *file_name, long int cpf){
    List *l = LeListaAgenda(file_name); // Tranformo o aquivo em lista
    removerCelula(l, cpf); // Removo a celula da lista
    EscreveListaAgenda(file_name, l); // Escrevo a lista de volta no arquivo
    destruirLista(l); // Destruo a Lista
}

void RemoverLoja(long int cnpj){
    List *l = LeListaLojas(); // Tranformo o aquivo em lista
    removerCelula(l, cnpj);// Removo a celula da lista
    EscreveListaLojas(l); // Escrevo a lista de volta no arquivo
    destruirLista(l); // Destruo a Lista
}

void RemoverCliente(long int cpf){
    List *l = LeListaClientes(); // Tranformo o aquivo em lista
    removerCelula(l, cpf); // Removo a celula da lista
    EscreveListaClientes(l); // Escrevo a lista de volta no arquivo
    destruirLista(l); // Destruo a Lista
}

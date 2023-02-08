#include "listas.h"
// Funções principais do Agendamento

List *LeListaLojas();
List *LeListaClientes();
void EscreveListaClientes(List *l);
void EscreveListaLojas(List *l);
void CadastroLoja(List *t, char *name, char *bairro, char *ramo, long int cnpj, int senha);
void CadastroCliente(List *t, char *nome, char *bairro, int senha, long int cpf, int idade);
void RealizarAgendamento();
void OrdenacaoCliente();
void OrdenacaoLoja();
void OrdenacaoAgendamento();
void RemoverAgendamento();
void RemoverLoja();
void RemoverCliente();
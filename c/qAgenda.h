#include "listas.h"
// Funções principais do Agendamento


/// @brief Le o aquivo e tranforma em lista 
/// @return Uma lista
List *LeListaLojas();

/// @brief Le o aquivo e tranforma em lista 
/// @return Uma lista
List *LeListaClientes();

/// @brief Le o aquivo e tranforma em lista 
/// @param name_file Nome do arquivo
/// @return Uma lista
List *LeListaAgenda(char *name_file);

/// @brief Escreve a lista no arquivo de clientes
/// @param l A lista a ser escrita
void EscreveListaClientes(List *l);

/// @brief Escreve a lista no arquivo das lojas
/// @param l A lista a ser escrita
void EscreveListaLojas(List *l);

/// @brief Escreve a lista na agenda
/// @param l Lista a ser escrita
/// @param name Nome do arquivo da agenda
void EscreveListaAgenda(List *l, char *name_file);

/// @brief Cadastro da loja no sistema
/// @param t A lista da loja
/// @param name O nome da loja
/// @param bairro O bairro da loja
/// @param ramo O ramo de atuação da loja
/// @param cnpj O cnpj da loja
/// @param senha A senha do usuário loja
void CadastroLoja(List *t, char *name, char *bairro, char *ramo, long int cnpj, int senha);

/// @brief Cadastra o clinte no sistema
/// @param t A lista do cliente
/// @param nome O nome do cliente
/// @param bairro O bairro do cliente
/// @param senha A senha do cliente
/// @param cpf O cpf do cliente
/// @param idade A idade do cliente
void CadastroCliente(List *t, char *nome, char *bairro, int senha, long int cpf, int idade);
void RealizarAgendamento();

/// @brief Ordenar os clientes por ordem alfabetica
void OrdenacaoCliente();

/// @brief Ordenar as lojas por ordem alfabetica
void OrdenacaoLoja();
void OrdenacaoAgendamento();

/// @brief Remover o Agendamento
/// @param name_file O nome do arquivo
/// @param cpf O cpf do cliente
void RemoverAgendamento(char *name_file, long int cpf);

/// @brief Remover a loja da lista
/// @param cnpj CNPJ da loja
void RemoverLoja(long int cnpj);

/// @brief Remover o cliente da lista
/// @param cpf Cpf do cliente
void RemoverCliente(long int cpf);
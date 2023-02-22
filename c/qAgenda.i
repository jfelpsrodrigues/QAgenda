%module qAgenda

%include cstring.i

%{
#define SWIG_FILE_WITH_INIT
#include "qAgenda.h"
#include "listas.h"
%}

%cstring_mutable(char *file_name);
%cstring_mutable(char *name);
%cstring_mutable(char *nome);
%cstring_mutable(char *bairro);
%cstring_mutable(char *ramo);
%include "qAgenda.h"

typedef struct no No;
typedef struct cadastro Cad;
typedef struct lista List;

/// @brief Le o aquivo e tranforma em lista 
/// @return Uma lista
List *LeListaLojas();

/// @brief Le o aquivo e tranforma em lista 
/// @return Uma lista
List *LeListaClientes();

/// @brief Le o aquivo e tranforma em lista 
/// @param name_file Nome do arquivo
/// @return Uma lista
List *LeListaAgenda(char *file_name);

/// @brief Escreve a lista no arquivo de clientes
/// @param l A lista a ser escrita
void EscreveListaClientes(List *l);

/// @brief Escreve a lista no arquivo das lojas
/// @param l A lista a ser escrita
void EscreveListaLojas(List *l);

/// @brief Escreve a lista na agenda
/// @param l Lista a ser escrita
/// @param name Nome do arquivo da agenda
void EscreveListaAgenda(char *file_name, List *l);

/// @brief Cadastro da loja no sistema
/// @param name O nome da loja
/// @param bairro O bairro da loja
/// @param ramo O ramo de atuação da loja
/// @param cnpj O cnpj da loja
/// @param senha A senha do usuário loja
void CadastroLoja(char *name, char *bairro, char *ramo, long int cnpj, int senha);

/// @brief Cadastra o clinte no sistema
/// @param nome O nome do cliente
/// @param bairro O bairro do cliente
/// @param senha A senha do cliente
/// @param cpf O cpf do cliente
/// @param idade A idade do cliente
void CadastroCliente(char *nome, char *bairro, int senha, long int cpf, int idade);

/// @brief Realiza o cadastro do agendamento no banco de dados
/// @param dia Dia do agendamento
/// @param horario Hora do agendamento
/// @param cpf CPF do cliente
/// @param name Nome do cliente
void RealizarAgendamento(char *file_name, int dia, int horario, long int cpf, char *name);

/// @brief Ordenar os clientes por ordem alfabetica
void OrdenacaoCliente();

/// @brief Ordenar as lojas por ordem alfabetica
void OrdenacaoLoja();

/// @brief Ordena o aquivo do agendamento
/// @param file_name Nome do arquivo do agendamento
void OrdenacaoAgendamento(char *file_name);

/// @brief Remover o Agendamento
/// @param cpf O cpf do cliente
/// @param file_name O nome do arquivo
void RemoverAgendamento(char *file_name, long int cpf);

/// @brief Remover a loja da lista
/// @param cnpj CNPJ da loja
void RemoverLoja(long int cnpj);

/// @brief Remover o cliente da lista
/// @param cpf Cpf do cliente
void RemoverCliente(long int cpf);

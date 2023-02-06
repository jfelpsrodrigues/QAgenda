#ifndef LIST_H
#define LIST_H

// Variaveis Globais
typedef struct no No;
typedef struct lista List;

No *criarNo(void);

/// @brief Cria uma lista Vazia
/// @return Uma lista Vazia
List *criarListaVazia(void);

/// @brief Cria uma lista com o primeiro nó alocado
/// @param ptr Um nó da lista já com informações 
/// @return Lista com o primeiro nó alocado
List *criarListaChave(No *ptr); 

/// @brief Adiciona um nó no inicio da lista
/// @param l Lista já alocada
/// @param ptr Um nó já com informações
void addInicio(List *l, No *ptr);

/// @brief Adiciona um nó no fim da lista
/// @param l Lista já alocada
/// @param ptr Um nó ja com informações
void addFim(List *l, No *ptr);

/// @brief Adiciona um nó antes de um especificado
/// @param l Lista já alocada
/// @param id CPF/CNPJ do nó ao qual você deseja que seja o posterior
/// @param ptr Novo nó da lista
void addChaveAntes(List *l, int id, No *ptr);

/// @brief Adiciona um nó depois do nó referenciado
/// @param l Lista 
/// @param identidade CPF/CNPJ do nó ao qual você deseja que seja o anterior
/// @param ptr Novo nó da lista
void addChaveDepois(List *l, int identidade, No *ptr);

/// @brief Busca um valor especifico do lista
/// @param l Lista
/// @param chave CPF/CNPJ do nó buscado
/// @return Retorna o nó procurado
No* retornarValor(List *l, int chave);

/// @brief Remove um nó especifico da lista
/// @param l Lista
/// @param chave CPF/CNPJ do nó a ser removido
void removerCelula(List *l, int chave); 

/// @brief Remove o primeiro nó da lista
/// @param l Lista
void removerInicio(List *l); 

/// @brief Remove o ultimo nó da lista
/// @param l Lista
void removerFim(List *l);

/// @brief Concatena duas listas distintas
/// @param a Lista 1
/// @param b Lista 2
/// @return Lista 1 concatenada
List* concatenarListas(List *a, List *b);

/// @brief Imprimi os itens da lista
/// @param l Lista
void printLista(List *l);

/// @brief Mostra o tamanho da lista
/// @param l Lista
/// @return Número int que representa o tamanho da lista
int tamanhoLista(List *l);

/// @brief Destroi a lista já criada anteriormente
/// @param l Lista
void destruirLista(List *l); // Destroi a lista criada

#endif
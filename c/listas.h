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
/// @param chave Identidade do nó
/// @param str Itém do nó
/// @return Lista com o primeiro nó alocado
List *criarListaChave(int chave, char str[]); 

/// @brief Adiciona um nó no inicio da lista
/// @param l Lista já alocada
/// @param chave Chave de identificação do nó 
/// @param str Nova string da lista 
void addInicio(List *l, int chave, char str[]);

/// @brief Adiciona um nó no fim da lista
/// @param l Lista já alocada
/// @param chave Chave de identificação do nó 
/// @param str Nova string da lista
void addFim(List *l, int chave, char str[]);

/// @brief Adiciona um nó em uma lista ordenada
/// @param l Lista já alocada
/// @param chave Chave de identificação do nó 
/// @param str Nova string da lista
void addOrdemCres(List *l, int num, char str[]);

/// @brief Adiciona um nó antes de um especificado
/// @param l Lista já alocada
/// @param identidade Nó de referencia
/// @param novo Identificador do novo nó
/// @param str Nova string da lista
void addChaveAntes(List *l, int identidade, int novo, char str[]);

/// @brief Adiciona um nó depois do nó referenciado
/// @param l Lista 
/// @param identidade Id do nó
/// @param novo Nova string da lista
void addChaveDepois(List *l, int identidade, char novo[]);

/// @brief Busca um valor especifico do lista
/// @param l Lista
/// @param chave Identidade do nó buscado
/// @return String dentro do nó
char* retornarValor(List *l, int chave);

/// @brief Remove um nó especifico da lista
/// @param l Lista
/// @param chave Identidade do nó a ser removido
void removerCelula(List *l, int chave); 

/// @brief Remove o primeiro nó da lista
/// @param l Lista
void removerInicio(List *l); 

/// @brief Remove o ultimo nó da lista
/// @param l Lista
void removerFim(List *l);

/// @brief Função de ordenação da lista em ordem crescente
/// @param l Lista
/// @return Lista ordenada em ordem crescente
List* ordenarLista(List *l);

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
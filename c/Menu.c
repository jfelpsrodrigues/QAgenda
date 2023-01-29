#include <stdio.h>
#include <stdlib.h>

void Menu(void){
   
    int num; 
    
    printf("\n****************************************************\n");
    printf("********* M E N U   P A R A   T E S T E ************\n");
    printf("****************************************************\n");
    printf("[0] - Cadastro de Loja\n");  
    printf("[1] - Cadastro de Cliente\n");  
    printf("[2] - Realizar Agendamento\n");  
    printf("[3] - Mostrar Agendamento\n");  
    printf("[4] - Mostrar Lojas Cadastradas\n");  
    printf("[5] - Mostrar lojas ordenadas\n");  
    printf("[6] - Mostrar Clientes Ordenados\n");  
    printf("[7] - Mostrar Agendamentos Ordenados\n");  
    printf("se quiser finalizar é so dar ctrl c rsrs\n\n");
    printf("****************************************************\n");
    printf("Digite um numero: ");
    scanf("%d", &num);

    while(num != 8){
        switch(num){
            case 0: printf("[0] - Cadastrar de Loja\n");
                // dados da chamada da função aqui 
                break;
            case 1: printf("[1] - Cadastro de Cliente\n");  
                // dados da chamada da função aqui 
                break;
            case 2:printf("[2] - Realizar Agendamento\n");  
                // dados da chamada da função aqui 
                break;
            case 3:printf("[3] - Mostrar Agendamento\n"); 
                // dados da chamada da função aqui 
                break;
            case 4:printf("[4] - Mostrar Lojas Cadastradas\n");  
                // dados da chamada da função aqui 
                break;
            case 5:printf("[5] - Mostrar lojas ordenadas\n");  
                // dados da chamada da função aqui 
                break;
            case 6:printf("[6] - Mostrar Clientes Ordenados\n");  
                // dados da chamada da função aqui 
                break;
            case 7:printf("[7] - Mostrar Agendamentos Ordenados\n");  
                // dados da chamada da função aqui 
                break;
            default:
                break;
        }
        Menu();
    }   
}

from funcoes import *

limpa()

init()

while(True):

    opcao = exibirMenu()

    limpa()

    if(opcao == 1): registarProdutos()
    elif(opcao == 2): editarProdutos()
    elif(opcao == 3): apagarProdutos()
    elif(opcao == 4): listarProdutos(True)

    elif(opcao == 5): listarHistorico()

    elif(opcao == 6): venderProdutos()
    elif(opcao == 7): listarVendas()
    
    elif(opcao == 0): 
       animacao("A sair")
       break

    else: print("--- OPÇÃO INVÁLIDA ---")
    
    carregueEnter()

print("\n")
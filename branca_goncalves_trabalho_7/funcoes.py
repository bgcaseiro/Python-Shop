import os
import time
import globais

from Produto import *
from Venda import *

#Funções
def exibirMenu():
    animacao("Aguarde")
    print("=== Loja Python ===\n")
    print("1 - Registar produto.")
    print("2 - Editar produto.")
    print("3 - Apagar produto.")
    print("4 - Listar produtos.\n")
    print("5 - Ver Histórico.\n")
    print("6 - Vender.")
    print("7 - Listar Vendas.\n")
    print("0 - Sair.\n")
    return int(input("- Opção: "))

def registarProdutos():
    print("--- Registar produto ---\n")
    nome = input("- Digite o NOME do Novo Produto que deseja REGISTAR: ")
    nome = nome.title()
    if verificarNomeExiste(nome):
        print("\n--- ATENÇÂO! ESTE NOME JÁ ESTÁ ASSOCIADO A OUTRO PRODUTO. ---")
    else:
        preco = float(input("- Digite o PREÇO deste novo produto: "))
        quantidade = int(input("- Digite a QUANTIDADE em stock deste novo produto: "))
        if quantidade >= 0:
            globais.produtos.append(Produto(nome, preco, quantidade))
            globais.historico.append(f"REGISTO: O Produto ({nome}) foi Registado com SUCESSO!")
            print(f"\nO Produto ({nome}) foi Registado com SUCESSO!")
        else:
            print("\n --- ATENÇÃO! A Quantidade deve ter um valor positivo.")       

def editarProdutos():
    print("--- Editar Produto ---\n")
    listarProdutos(True)
    id = int(input("\n- Digite o ID do produto que deseja EDITAR: ")) - 1
    print()
    if(id >= 0 and id < len(globais.produtos)):
        produto = globais.produtos[id]
        produto.toString(id + 1)
        
        print("\n--- Menu de Edição ---\n")
        print("1 - Nome.")
        print("2 - Preço.")
        print("3 - Quantidade em Stock.\n")
        print("0 - Cancelar.\n")
        opcao = int(input("- Opção: "))

        print()

        if(opcao == 1):
            novo_nome = input(f"\n- Digite o Novo Nome para substituir o (Nome Antigo: {produto.nome}): ")
            novo_nome = novo_nome.title()
            if(verificarNomeExiste(novo_nome) == False):
                nome_antigo = produto.nome
                produto.setNome(novo_nome)
                print(f"\n--- O NOME do Produto foi atualizado para ({novo_nome}) com SUCESSO! ---")
                globais.historico.append(f"EDIÇÃO: O Nome do produto (Nome: {nome_antigo}) foi alterado para (NOVO NOME: {novo_nome}).")      
            else: 
                print("\n--- ATENÇÂO! ESTE NOME JÁ ESTÁ ASSOCIADO A OUTRO PRODUTO. ---")
        elif(opcao == 2):
            novo_preco = float(input(f"\n- Digite o NOVO PREÇO para o Produto ({produto.nome}): "))
            preco_antigo = produto.preco
            produto.setPreco(novo_preco)
            print(f"\n--- O PREÇO do Produto ({produto.nome}) foi atualizado para ({novo_preco:.2f} €) com SUCESSO! ---")
            globais.historico.append(f"EDIÇÃO: O Preço do produto (ID:{id + 1} {produto.nome}) foi alterado de ({preco_antigo:.2f} €) para ({novo_preco:.2f} €).")
        elif(opcao == 3):
            nova_quantidade = int(input(f"\n- Digite a NOVA QUANTIDADE para atualizar o Stock do Produto ({produto.nome}): "))
            if nova_quantidade >= 0:
                quantidade_antiga = produto.quantidade
                produto.setQuantidade(nova_quantidade)
                print(f"\n--- A Quantidade do Produto ({produto.nome}) foi atualizada para ({nova_quantidade} unidades) com SUCESSO! ---")
                globais.historico.append(f"EDIÇÃO: A Quantidade do produto (ID:{id + 1} {produto.nome}) foi alterada de ({quantidade_antiga} unidades) para ({nova_quantidade} unidades).")
            else:
                print("\n--- ATENÇÃO! A Quantidade deve ter um valor positivo.")
                
        elif(opcao == 0): print("\n--- OPERAÇÃO CANCELADA! ---")
        else:
            print("\n--- OPÇÃO INVÁLIDA! ---")
    else: print("\n--- ID INVÁLIDO! ---")

def apagarProdutos():
    print("--- Apagar Produto ---\n")
    listarProdutos(True)
    id = int(input("\n- Digite o ID do produto que deseja APAGAR: ")) - 1
    print()
    if(id >= 0 and id < len(globais.produtos)):
        produto_apagado = globais.produtos.pop(id)
        produto_apagado.toString(id + 1)
        print(f"\n--- O Produto ({produto_apagado.nome}) foi Apagado com SUCESSO! ---")
        globais.historico.append(f"EXCLUSÃO: O produto ({produto_apagado.nome}) foi apagado com SUCESSO!")
    else:
        print("\n--- ID INVÁLIDO! ---")

def listarProdutos(com_titulo):
    if(com_titulo): 
        print("--- Lista de Produtos ---\n")
        for i in range(len(globais.produtos)):
            globais.produtos[i].toString(i + 1)
       
def listarHistorico():
    print("--- Revelar Histórico ---\n")
    for i in range(len(globais.historico)):
        print(f"{i + 1} - {globais.historico[i]}")

def venderProdutos():
    print("--- Vender Produto ---\n")
    listarProdutos(True)
    id = int(input("\n- Digite o ID do produto que deseja VENDER: ")) - 1
    print()
    if(id >= 0 and id < len(globais.produtos)):
        produto = globais.produtos[id]
        produto.toString(id + 1)
        quantidade_venda = int(input("\n- Digite a QUANTIDADE do Produto que deseja VENDER: "))
        if 0 < quantidade_venda <= produto.quantidade:
            preco_total = produto.preco * quantidade_venda
            globais.vendas.append(Venda(produto.nome, produto.preco, quantidade_venda))
            produto.quantidade -= quantidade_venda
            print(f"\n--- A quantidade ({quantidade_venda} unidades) do produto ({produto.nome})foi vendida com SUCESSO! ---")
            globais.historico.append (f"VENDA: Venda de ({quantidade_venda} x {produto.nome}) foi realizada com SUCESSO!")  
        else: 
            print("\n--- QUANTIDADE INVÁLIDA! ---")
    else: print("\n--- ID INVÁLIDO! ---")

def listarVendas():
    print("--- Lista das Vendas ---\n")
    total = 0
    for i in range(len(globais.vendas)):
        globais.vendas[i].toString(i)
        total += globais.vendas[i].preco_unidade * globais.vendas[i].unidades_vendidas
    print(f"\nTotal apurado de Vendas: ({total:.2f} €)")
    globais.historico.append(f"Listagem das vendas realizadas.")


#Funções Helpers
def init():
    globais.produtos.append(Produto("Caneta Azul", 1.99, 10))
    globais.produtos.append(Produto("Caneta Preta", 1.79, 20))
    globais.produtos.append(Produto("Caneta Vermelha", 1.89, 30))


def verificarNomeExiste(nome_a_verificar):
    for p in globais.produtos:
        if(p.nome.lower() == nome_a_verificar.lower()): 
            return True
    return False

def exibirVenda(id):
    venda = globais.vendas[id]
    preco_total = venda.preco_unidade * venda.unidades_vendidas
    print(f"ID{id + 1} - {venda.nome_produto} ({venda.preco_unidade:.2f}€ x {venda.unidades_vendidas} unidades) = (Valor Total: {preco_total:.2f} €)")

#Funcoes Especiais
def limpa():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguarde(tempo):
    time.sleep(tempo)

def animacao(frase):
    tempo = 0.1
    limpa()
    print(frase, end="", flush=True)
    aguarde(tempo)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    limpa()

def carregueEnter(): input("\nCarregue <ENTER> para continuar...")
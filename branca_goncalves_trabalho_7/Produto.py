class Produto:

    #Atributos e Construtor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    #Métodos  
    def toString(self, id):
        print(f"ID: {id:<5} | Nome: {self.nome:<15} | Preço: {self.preco:.2f} € | Quantidade: {self.quantidade:>5} unidades")
    
    def setNome(self, novo_nome): 
        nome_antigo = self.nome
        self.nome = novo_nome.title()
        return nome_antigo

    def setPreco(self, novo_preco):
        preco_antigo = self.preco
        self.preco = novo_preco
        return preco_antigo

    def setQuantidade(self, nova_quantidade):
        quantidade_antiga = self.quantidade
        self.quantidade = nova_quantidade
        return quantidade_antiga





   
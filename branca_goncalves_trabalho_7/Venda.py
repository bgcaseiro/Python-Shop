class Venda:

    #Atributos e construtor
    def __init__(self,nome_produto, preco_unidade, unidades_vendidas):
        self.nome_produto = nome_produto
        self.preco_unidade = preco_unidade
        self.unidades_vendidas = unidades_vendidas

    #Métodos   
    def toString(self, id):
        preco_total = self.preco_unidade * self.unidades_vendidas
        print(f"ID{id + 1}: {self.nome_produto} (Preço: {self.preco_unidade:.2f} €) x (Quantidade Vendida: {self.unidades_vendidas}) = (Valor Total: {preco_total:.2f} €)")
    

class Produto:

    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def altera_preco(self, novo_preco):
        self.preco = novo_preco

    def adiciona_quant(self, somar_estoque):
        self.quantidade += somar_estoque

    def remover_quant(self, subtrair_estoque):
        if subtrair_estoque <= self.quantidade:
            self.quantidade -= subtrair_estoque
        else:
            print("Quantidade insuficiente em estoque")

    def __str__(self):
        return f"Nome: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade} | Código: {self.codigo}"


class Estoque:

    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        contador = 0

        for produto in self.produtos:
            print(produto)
            contador += 1

        if contador == 0:
            print("Nenhum produto cadastrado.")

    def buscar_produto(self, nome):

        for produto in self.produtos:
            if produto.nome == nome:
                return produto

    def adicionar_estoque(self, nome, quantidade):
        produto = self.buscar_produto(nome)

        if produto:
            produto.adiciona_quant(quantidade)
        else:
            print("Produto não encontrado")

    def remover_estoque(self, nome, quantidade):
        produto = self.buscar_produto(nome)

        if produto:
            produto.remover_quant(quantidade)
        else:
            print("Produto não encontrado")

    def alterar_preco(self, nome, novo_preco):
        produto = self.buscar_produto(nome)

        if produto:
            produto.altera_preco(novo_preco)
        else:
            print("Produto não encontrado")

    def calcular_valor_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco * produto.quantidade

        return total

    def remove_produto(self, nome):
        produto = self.buscar_produto(nome)

        if produto:
            self.produtos.remove(produto)
        else:
            print("Produto não encontrado")


def main():
    estoque = Estoque()

    while True:
        print()
        print("==== ESTOQUE ====")

        opcao = int(input(
            "[1] Cadastrar produto\n"
            "[2] Remover produto\n"
            "[3] Listar produtos\n"
            "[4] Buscar produto\n"
            "[5] Adicionar estoque\n"
            "[6] Remover estoque\n"
            "[7] Alterar preço\n"
            "[8] Ver valor total\n"
            "[0] Sair\n\n"
            "Escolha uma opção: "
        ))

        if opcao == 0:
            print("Encerrando...")
            break

        if opcao == 1:
            nome = input("Nome: ")
            preco = float(input("Preço: R$"))
            quantidade = int(input("Quantidade: "))
            codigo = input("Código: ")

            produto = Produto(nome, preco, quantidade, codigo)
            estoque.cadastrar_produto(produto)

        if opcao == 2:
            nome = input("Nome: ")
            estoque.remove_produto(nome)

        if opcao == 3:
            estoque.listar_produtos()

        if opcao == 4:
            nome = input("Nome: ")

            produto = estoque.buscar_produto(nome)

            if produto:
                print(produto)
            else:
                print("Produto não encontrado")

        if opcao == 5:
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))

            estoque.adicionar_estoque(nome, quantidade)

        if opcao == 6:
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))

            estoque.remover_estoque(nome, quantidade)

        if opcao == 7:
            nome = input("Nome: ")
            preco = float(input("Preço: R$"))

            estoque.alterar_preco(nome, preco)

        if opcao == 8:
            total = estoque.calcular_valor_total()
            print(f"Valor total do estoque: R${total:.2f}")


if __name__ == "__main__":
    main()

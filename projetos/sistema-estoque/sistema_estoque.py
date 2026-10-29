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
        if 0 < subtrair_estoque <= self.quantidade:
            self.quantidade -= subtrair_estoque
            return True
       
        return False

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Preço: R${self.preco:.2f} | "
            f"Quantidade: {self.quantidade} | "
            f"Código: {self.codigo}"
        )


class Estoque:

    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(produto)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto

        return None

    def adicionar_estoque(self, nome, quantidade):
        produto = self.buscar_produto(nome)

        if produto and quantidade > 0:
            produto.adiciona_quant(quantidade)
            return True

        return False

    def remover_estoque(self, nome, quantidade):
        produto = self.buscar_produto(nome)

        if produto:
            return produto.remover_quant(quantidade)

        return False

    def alterar_preco(self, nome, novo_preco):
        produto = self.buscar_produto(nome)

        if produto and novo_preco >= 0:
            produto.altera_preco(novo_preco)
            return True

        return False

    def calcular_valor_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco * produto.quantidade

        return total

    def remove_produto(self, nome):
        produto = self.buscar_produto(nome)

        if produto:
            self.produtos.remove(produto)
            return True

        return False


def main():
    estoque = Estoque()

    while True:
        print()
        print("==== ESTOQUE ====")

        try:
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
        except ValueError:
            print("Digite uma opção numérica válida.")
            continue

        if opcao == 0:
            print("Encerrando...")
            break

        elif opcao == 1:
            nome = input("Nome: ")
            codigo = input("Código: ")

            try:
                preco = float(input("Preço: R$"))
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Preço ou quantidade inválidos.")
                continue

            if preco < 0 or quantidade < 0:
                print("Preço e quantidade não podem ser negativos.")
                continue

            if estoque.buscar_produto(nome):
                print("Já existe um produto com esse nome.")
                continue

            produto = Produto(nome, preco, quantidade, codigo)
            estoque.cadastrar_produto(produto)

            print("Produto cadastrado com sucesso.")

        elif opcao == 2:
            nome = input("Nome: ")

            if estoque.remove_produto(nome):
                print("Produto removido com sucesso.")
            else:
                print("Produto não encontrado.")

        elif opcao == 3:
            estoque.listar_produtos()

        elif opcao == 4:
            nome = input("Nome: ")
            produto = estoque.buscar_produto(nome)

            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")

        elif opcao == 5:
            nome = input("Nome: ")

            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Digite uma quantidade inteira válida.")
                continue

            if estoque.adicionar_estoque(nome, quantidade):
                print("Estoque adicionado com sucesso.")
            elif not estoque.buscar_produto(nome):
                print("Produto não encontrado.")
            else:
                print("A quantidade deve ser maior que zero.")

        elif opcao == 6:
            nome = input("Nome: ")

            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Digite uma quantidade inteira válida.")
                continue

            if estoque.remover_estoque(nome, quantidade):
                print("Estoque removido com sucesso.")
            elif not estoque.buscar_produto(nome):
                print("Produto não encontrado.")
            elif quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                print("Quantidade insuficiente em estoque.")

        elif opcao == 7:
            nome = input("Nome: ")

            try:
                preco = float(input("Novo preço: R$"))
            except ValueError:
                print("Digite um preço válido.")
                continue

            if estoque.alterar_preco(nome, preco):
                print("Preço alterado com sucesso.")
            elif not estoque.buscar_produto(nome):
                print("Produto não encontrado.")
            else:
                print("O preço não pode ser negativo.")

        elif opcao == 8:
            total = estoque.calcular_valor_total()
            print(f"Valor total do estoque: R${total:.2f}")

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

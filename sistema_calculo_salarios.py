from abc import ABC, abstractmethod
from rich import print


class Funcionario(ABC):

    def __init__(self, nome, sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.salario_min = 1621

    @abstractmethod
    def calc_salario(self, imposto):
        pass

    def analisar_salario(self):
        print(
            f"[green]O salário de {self.nome}[/green] "
            f"([yellow]{type(self).__name__}[/yellow]) "
            f"[green]é de R$[bold]{self.salario:.2f}[/bold], "
            f"que corresponde a [bold cyan]"
            f"{self.salario / self.salario_min:.1f}"
            f"[/bold cyan] salários mínimos.[/green]"
        )


class Horista(Funcionario):

    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_salario(self, imposto):
        self.sal_bruto = self.valor_hora * self.horas_trab
        desconto = self.sal_bruto * imposto / 100
        self.salario = self.sal_bruto - desconto


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_salario(self, imposto):
        desconto = self.sal_bruto * imposto / 100
        self.salario = self.sal_bruto - desconto


def main():

    while True:
        print("\n[bold cyan]==== CÁLCULO DE SALÁRIO ====[/bold cyan]")
        print("[1] Funcionário horista")
        print("[2] Funcionário mensalista")
        print("[0] Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("[yellow]Encerrando...[/yellow]")
            break

        elif opcao == "1":
            nome = input("\nNome do funcionário: ")
            valor_hora = float(input("Valor da hora: R$"))
            horas_trab = float(input("Horas trabalhadas: "))

            funcionario = Horista(nome, valor_hora, horas_trab)

        elif opcao == "2":
            nome = input("\nNome do funcionário: ")
            sal_bruto = float(input("Salário bruto: R$"))

            funcionario = Mensalista(nome, sal_bruto)

        else:
            print("[red]Opção inválida.[/red]")
            continue

        imposto = float(input("Porcentagem de imposto/desconto: %"))

        funcionario.calc_salario(imposto)

        print()
        funcionario.analisar_salario()


if __name__ == "__main__":
    main()
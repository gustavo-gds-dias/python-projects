from abc import ABC, abstractmethod
from rich import print


class Funcionario(ABC):

    def __init__(self, nome, sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.salario_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        print(
            f"[green]O salario de {self.nome}[/green]([yellow]{type(self).__name__}[/yellow]) "
            f"[green]é de R$[bold]{self.salario:.2f}[/bold] que corresponde a "
            f"[bold cyan]{self.salario / self.salario_min:.1f}[/bold cyan] salarios mínimos[/green]"
        )


class Horista(Funcionario):

    def __init__(self, nome, valor_hora, horas_trab, sal_bruto=0, salario=0):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_salario(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto=0, salario=0):
        super().__init__(nome, sal_bruto, salario)

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)


def main():
    f1 = Horista("Fernando", 3, 300)
    f1.calc_salario()
    f1.analisar_salario()

    f2 = Mensalista("Gomes", 1612)
    f2.calc_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
from random import randint
from time import time
from rich import print
import threading

cont = 1
senha = ''

for c in range(4):
    senha += str(randint(0, 9))

tempo_limite = 45
tempo_esgotado = False


def cronometro():
    global tempo_esgotado

    tempo_inicio = time()

    while not tempo_esgotado:
        if time() - tempo_inicio >= tempo_limite:
            tempo_esgotado = True
            print()
            print('[bold red]KABOOM!!! A BOMBA EXPLODIU[/bold red]')
            print('[red]TEMPO ESGOTADO[/red]')
            print(f'[yellow]A senha era [bold]{senha}[/bold][/yellow]')
            break


print('[bold red]VOCÊ TEM 45 SEGUNDOS PARA ACERTAR A COMBINAÇÃO DE 4 NÚMEROS[/bold red]')
print('[yellow]É POSSÍVEL TENTAR ADIVINHAR ATÉ 5 VEZES, ENTÃO TENTE COM SABEDORIA[/yellow]')

input('PRESSIONE ENTER SE ESTIVER PRONTO: ')

thread = threading.Thread(target=cronometro)
thread.start()

while True:
    if tempo_esgotado:
        break

    print()

    tentativa = input(f'Faça a sua {cont}ª tentativa: ').strip()

    if tempo_esgotado:
        break

    if not tentativa.isdigit():
        print('[bold red]AVISO: DIGITE SOMENTE NÚMEROS.[/bold red]')
        continue

    if len(tentativa) != 4:
        print('[bold red]AVISO: DIGITE EXATAMENTE 4 NÚMEROS EM CADA TENTATIVA.[/bold red]')
        continue

    if tentativa == senha:
        tempo_esgotado = True
        print('[bold green]PARABÉNS!!! VOCÊ DESARMOU A BOMBA[/bold green]')
        print(f'[green]A SENHA REALMENTE ERA [bold]{senha}[/bold][/green]')
        break

    if tentativa[0] == senha[0]:
        print(f'[green]O número {tentativa[0]} na posição 0 está correto[/green]')

    if tentativa[1] == senha[1]:
        print(f'[green]O número {tentativa[1]} na posição 1 está correto[/green]')

    if tentativa[2] == senha[2]:
        print(f'[green]O número {tentativa[2]} na posição 2 está correto[/green]')

    if tentativa[3] == senha[3]:
        print(f'[green]O número {tentativa[3]} na posição 3 está correto[/green]')

    tentativa_num = int(tentativa)
    senha_num = int(senha)

    if tentativa_num > senha_num:
        print('[yellow]A senha é menor[/yellow]')
    elif tentativa_num < senha_num:
        print('[yellow]A senha é maior[/yellow]')

    cont += 1

    if cont > 5:
        tempo_esgotado = True
        print('[bold red]KABOOM!!! A BOMBA EXPLODIU[/bold red]')
        print('[red]TENTATIVAS ESGOTADAS[/red]')
        print(f'[yellow]A senha era [bold]{senha}[/bold][/yellow]')
        break
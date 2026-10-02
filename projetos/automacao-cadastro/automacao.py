import pyautogui
import time
pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=3164, y=367)
pyautogui.write('email') # email fictício
pyautogui.press('tab')
pyautogui.write('senhamuitosegura') # senha fictícia
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('enter')

import pandas
from pathlib import Path

caminho = Path(__file__).parent / 'produtos.csv'

tabela = pandas.read_csv(caminho)

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=3138, y=242)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')


    observacao = tabela.loc[linha, 'obs']

    if pandas.notna(observacao):
        pyautogui.write(str(observacao))

    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.press('enter')

    pyautogui.scroll(10000000)      




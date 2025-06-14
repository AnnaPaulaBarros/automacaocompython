# Logica: Passos a passos a serem seguidos para resolver um determido problema
# instalar as Bibliotecas
# Usar as bibliotecas no meu código
# Iniciar a automação
## Abrir o navegador
## Entrar no site
## Autenticar no site
## Carregar o arquivo que contem os dados aserem inseridos
## Cadastrar os alunos
##### --> Repetir os passos acima ate cadastrar todos os alunos


import pyautogui   
import pandas
import time
import keyboard


pyautogui.PAUSE = 0.6
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
time.sleep(4)
pyautogui.write('https://aula01.simplificapython.com.br')
pyautogui.press('enter')
pyautogui.press('maximizar')
time.sleep(5)
pyautogui.click(x=552, y=470)
pyautogui.write("admin")
pyautogui.press('tab')
pyautogui.write("simplificapython")
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(5)


tabela = pandas.read_csv('alunos.csv')

for linha in tabela.index:
    pyautogui.click(x=513, y=347)
    Nome = tabela.loc[linha, 'Nome']
    pyautogui.write(Nome)
    pyautogui.press('tab')
    email = tabela.loc[linha, 'Email']
    pyautogui.write(email)
    pyautogui.press('tab')
    endereco = tabela. loc [linha, 'Endereco']
    pyautogui.write(endereco)
    pyautogui.press('tab')
    telefone = tabela.loc[linha, 'Telefone']
    pyautogui.write(telefone)
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.scroll(5000)
   












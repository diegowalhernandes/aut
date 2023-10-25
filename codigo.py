# Passo a passo do projeto 

import pyautogui
import time
import pandas

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinaçao de teclas)

pyautogui.PAUSE = 1

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 1: Entrar no sistema da empresa / https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(2)

# Passo 2: Fazer login 
pyautogui.click(x=784, y=495)
pyautogui.write("email")

pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar a base de dados de produtos
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:  

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=598, y=356)   

    codigo = tabela.loc[linha, "codigo"] 
    marca = tabela.loc[linha, "marca"]   
    tipo = tabela.loc[linha, "tipo"] 
    categoria = tabela.loc[linha, "categoria"] 
    preco_unitario = tabela.loc[linha, "preco_unitario"] 
    custo = tabela.loc[linha, "custo"] 
    obs = tabela.loc[linha, "obs"] 

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
        # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

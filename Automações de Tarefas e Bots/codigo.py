# Importar bibliotecas necessárias (Se necessário)
import pyautogui
import time
import pandas

# pyautogui.click -> Clica
# pyautogui.write -> Escreve
# pyautogui.press -> Aperta uma tecla
# pyautogui.hotkey -> Aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5 # Espera 1 segundo entre cada comando 'press' "win", 'write' "chrome" ...
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
password = "123456"

# Passo a passo do programa
# Passo 1: Entrar no sistema da empresa
# pip install pyautogui
# Abrir o navegador
# Acessar sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) # Pausa maior para o site carregar (3 segundos)

# Passo 2: Fazer login
# Digitar e-mail
# Digitar senha
# Clicar em 'logar'
pyautogui.click(x=672, y=406)
pyautogui.write("andrezana@hotmail.com")
pyautogui.click(x=684, y=502)
pyautogui.write(password)
pyautogui.press("tab") # Passa para o botão 'Logar'
pyautogui.press("enter")
time.sleep(3) # Pausa maior para o site carregar (3 segundos)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl
tabela = pandas.read_csv("Automações de Tarefas e Bots/produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar todos os produtos
    # Código
    pyautogui.click(x=788, y=291) # Clica no campo 'Código'
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # Passa para o próximo campo        
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")    
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")    
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")    
    # Preço Unitário
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")    
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")    
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passa para o botão 'Enviar'
    pyautogui.press("enter") # Clicar no botão 'Enviar'        
    
    # Voltar ao início da tela para cadastrar um novo produto
    pyautogui.scroll(5000)
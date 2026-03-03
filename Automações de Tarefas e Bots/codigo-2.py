import pyautogui # Biblioteca para automação de teclado e mouse (simula ações humanas na interface)

pyautogui.PAUSE = 0.5 # Comando que insere uma pausa/um intervalo/ um break entre cada ação (comando), para acontecer mais naturalemnte, evitando erros, devido a alta velocidade da execução do sistema em cada tarefa.

# Passo 1: Abrir o navegador
pyautogui.press("win") # Clicar em Iniciar (botão Windows)
pyautogui.write("chrome") # Digitar o navegador desejado (Google Chrome)
pyautogui.press("enter") # Pressionar enter para confirmar e acessar o navegador

# Passo 2: Abrir o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Variável 'link' recebendo o link que iremos acessar como valor
pyautogui.write(link) # Digitar o site desejado
pyautogui.press("enter")

# Passo 3: Efetuar login
import time # Biblioteca para controle de tempo (pausas na execução do script)
email = "andrezana@hotmail.com" # Variável 'email' recebendo o email que iremos utilizar no login
senha = "123456" # Variável 'senha' recebendo a senha que iremos utilizar no login ( SENHA FAKE/TESTE )
pyautogui.click(x=690, y=409) # Posição onde devemos escrever o email para login
pyautogui.write(email) # Digitar o email de login
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab") # 'Tab' para mudar para o botão 'Login'
pyautogui.press("enter") # 'Enter' para clicar no botão 'Login'
time.sleep(2) # Pausa maior para o site carregar (3 segundos)

# Passo 4: Abrir base de dados
import pandas # Biblioteca para manipulação e leitura de dados (planilhas/CSV)
tabela = pandas.read_csv("Automações de Tarefas e Bots/produtos 2.csv")

# Passo 5: Cadastrar produtos no sistema
for linha in tabela.index: # Laço de repetição para rodar todas as linhas da tabela e cadastrar no sistema
    pyautogui.click(x=664, y=289) # Posição onde devemos escrever o código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs =  str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000) # Voltar ao início da tela (scroll up) para cadastrar um novo produto
    
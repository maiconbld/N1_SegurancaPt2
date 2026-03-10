# 🔐 N1 – Diffie-Hellman + Cifra de César

Segunda parte da N1 do Primeiro Bimestre de **Segurança da Informação**

Integrantes:  Maicon Dias - 082210032

              Pedro Henrike - 082210025
              
              Thiago Guedes - 082210010

---

# 📚 Objetivo do Projeto

Implementar uma comunicação segura entre cliente e servidor que:

1. Estabeleça conexão TCP entre duas aplicações
2. Realize **troca segura de chaves usando Diffie-Hellman**
3. Utilize o segredo compartilhado para gerar uma **chave de criptografia**
4. Aplique **Cifra de César para criptografar as mensagens**
5. Permita envio e recebimento de mensagens criptografadas
6. Suporte caracteres UTF-8 (acentos e pontuação)

---

# 🧠 Algoritmos Implementados

## Diffie-Hellman

Utilizado para gerar um **segredo compartilhado entre cliente e servidor** sem que a chave precise ser transmitida diretamente pela rede.

Fluxo:

1. Servidor define:
   - número primo `p`
   - base `g`

2. Servidor gera chave privada:
```
a
```

3. Cliente gera chave privada:
```
b
```

4. Chaves públicas são trocadas:

```
A = g^a mod p
B = g^b mod p
```

5. Ambos calculam o mesmo segredo:

```
segredo = B^a mod p
segredo = A^b mod p
```

Este segredo é então utilizado para gerar o **shift da Cifra de César**.

---

## Cifra de César

Algoritmo clássico de criptografia por substituição.

Cada letra é deslocada no alfabeto usando a chave gerada pelo Diffie-Hellman.

Exemplo:

```
Mensagem:  hello
Shift:     3

Resultado: khoor
```

A descriptografia aplica o deslocamento inverso.

---

# 🖥 Estrutura do Projeto

```
project/
│
├── Simple_tcpServer.py
├── Simple_tcpClient.py
└── README.md
```

### Simple_tcpServer.py
Responsável por:

- iniciar o servidor TCP
- gerar parâmetros Diffie-Hellman
- realizar o handshake criptográfico
- descriptografar mensagens recebidas
- enviar respostas criptografadas

### Simple_tcpClient.py
Responsável por:

- conectar ao servidor
- realizar troca de chaves Diffie-Hellman
- criptografar mensagens enviadas
- descriptografar respostas recebidas

---

# 🔄 Fluxo de Comunicação

1️⃣ Servidor inicia e aguarda conexão  
2️⃣ Cliente conecta ao servidor  
3️⃣ Servidor envia parâmetros Diffie-Hellman (`p`, `g`, chave pública)  
4️⃣ Cliente envia sua chave pública  
5️⃣ Ambos calculam o **segredo compartilhado**  
6️⃣ O segredo gera o **shift da Cifra de César**  
7️⃣ Mensagens passam a ser **criptografadas antes do envio**

---

# 📡 Exemplo de Execução

### Terminal 1 – Servidor

```
python Simple_tcpServer.py
```

Saída:

```
Servidor aguardando conexão...

Cliente conectado
Segredo compartilhado: 2384
Shift utilizado: 16
```

---

### Terminal 2 – Cliente

```
python Simple_tcpClient.py
```

Entrada:

```
Digite mensagem: Fabio Cabrini
```

Saída:

```
Recebido criptografado: ...
Recebido decifrado: FÁBIO CABRINI
```

---

# 🔤 Suporte a Caracteres UTF-8

A comunicação utiliza:

```
.encode("utf-8")
.decode("utf-8")
```

Isso permite transmitir corretamente:

```
á é í ó ú ç ã ê ô
```

sem perda de informação durante a criptografia.

---

# 🛠 Tecnologias Utilizadas

- **Python 3**
- **Socket TCP**
- **Diffie-Hellman Key Exchange**
- **Cifra de César**
- **Codificação UTF-8**

---

# 🎯 Resultado

O sistema demonstra:

✔ comunicação TCP funcional  
✔ troca segura de chave  
✔ criptografia de mensagens  
✔ descriptografia no destino  
✔ implementação manual dos algoritmos  

---

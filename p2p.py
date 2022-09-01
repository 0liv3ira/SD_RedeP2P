import socket  # cobexão via socket
import sys    # ags via terminal
import time
import string
import secrets

if(len(sys.argv)<3):
    print("VOCE DEVE PASSAR COMO ARGUMENTO O IP E A PORTA 192.168.1.2 80  windows|linux")
    exit()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
id = secrets.token_hex()   #Retorna uma string hexadecimal
cliente.connect((sys.argv[1], int(sys.argv[2])))
cliente.send(str.encode(id))
saldo = 10
saldoaenviar = 0
id_alvo = ""

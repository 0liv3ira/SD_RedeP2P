#!/usr/bin/python

import socket
from theads import ServerThread


def get_nos():
    global nos_da_rede
    print("get nos")
    print(nos_da_rede.values())
    return nos_da_rede


def set_nos(no):
    global nos_da_rede
    print("set nos")
    nos_da_rede.update(no)
    print(nos_da_rede.values())


global nos_da_rede
nos_da_rede = {'teste': 'Dez'}
global x
x = 20

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Definindo uma conexao TCP em python

try:
    servidor.bind(("0.0.0.0", int(2000)))  # 0.0.0.0 , Ip generico aceita qualquer IP interno ou externo
    servidor.listen(5)  # numero de conexoes consecutivas
    threads = []
    while True:
        print("Aguardando Conexao\n")
        (cliente_socket, endereco) = servidor.accept()  # Capturo Ip do cliente
        hash = cliente_socket.recv(2024)  # Recebo a Hash
        hash = hash.decode("'utf-8'")
        print(f"\nRecebido do ip : {endereco[0]} : {endereco[1]} : {hash}")
        no = {endereco[0]: hash}
        set_nos(no)
        get_nos()
        Cliente = ServerThread(endereco[0], endereco[1], cliente_socket, hash)
        Cliente.start()
        threads.append(Cliente)
        for thread in threads:
            thread.join

except Exception as erro:
    print("Erro" + str(erro))

print("FIM : ", x)
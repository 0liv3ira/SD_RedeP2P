import threading
from time import sleep

class ServerThread(threading.Thread):

    def __init__(self, ip, porta ,cliente_socket,hash ):
        threading.Thread.__init__(self)
        self.ip = ip
        self.porta = porta
        self.conexao = cliente_socket
        self.hash = hash
        print(f'[+] Novo conexão : {ip} {str(porta)} : {hash}')

    def run(self):
        while True:
            data = self.conexao.recv(2024)
            data = data.decode('utf-8')
            #print(type(data))
            from server import get_nos
            print("ENTREI NA THREAD")
            print(get_nos().values())
            sleep(1000)
            if(data =="/"):
                #As opções vão aqui, de transferência sair ou atualizar hash vão aqui .
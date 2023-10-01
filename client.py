# TP SISTER MOD 3
#ANGGOTA 1 : Muhammad Abiya Makruf - 1301213157 - MTA
#ANGGOTA 2 : Galih Akbar Nugraha - 1301213060 - AFN

# TCP Client
import socket
import threading

class Client:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        while True:
            self.host = input("Masukkan IP server: ")
            self.port = int(input("Masukkan port server: "))
            self.username = input("Masukkan username: ")
            if len(self.host.split('.')) < 4 and self.port > 0:
                continue
            break

    def serverConfig(self):
        return (self.host, self.port)

    @property
    def connect(self):
        while True:
            try:
                self.client_socket.connect(self.serverConfig())
                print("Successfully connected to server")
                return True
            except:
                print("Connection closed")
                return False

    def send(self, data):
        self.client_socket.send(data.encode())

    def receive(self):
        while True:
            try:
                print(self.client_socket.recv(1024).decode())
            except:
                break

    def join(self):
        while self.connect:
            rec = threading.Thread(target=self.receive)
            rec.daemon = True
            rec.start()

            while True:
                try:
                    msg = input()
                except KeyboardInterrupt:
                    self.client_socket.close()
                    break
                
                if msg != '!q':
                    msg = f"{self.username}: {msg}"
                    self.send(msg)
                else:
                    break

if __name__ == '__main__':
    client = Client()
    client.join()
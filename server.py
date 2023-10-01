# TP SISTER MOD 3 - Server TCP
#ANGGOTA 1 : Muhammad Abiya Makruf - 1301213157 - MTA
#ANGGOTA 2 : Galih Akbar Nugraha - 1301213060 - AFN

#Import
import socket
import threading

#Class Server
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    def createServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(10)

    def start(self):
        self.createServer()
        print("Server berhasil dijalankan! Menunggu koneksi.")
        while True: #Selama tidak ada interupsi keyboard
            conn, addr = self.server.accept()
            self.clients.append(conn)
            client = threading.Thread(target=self.handleClient, args=(conn))
            client.start()
            print(addr, "berhasil terkoneksi")

    def handleClient(self):
        pass



#Start server
#TODO host sama port mau dibikin input atau tidak?
server = Server('192.168.18.25',5000)
server.start()
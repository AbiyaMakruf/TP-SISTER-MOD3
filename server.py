#TP SISTER MOD 3 - Server TCP
#ANGGOTA 1 : Muhammad Abiya Makruf - 1301213157 - MTA
#ANGGOTA 2 : Galih Akbar Nugraha - 1301213060 - AFN

#Import
import socket
import threading
import datetime

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
            client = threading.Thread(target=self.onReceiveMessage, args=(conn,addr,))
            client.start()
            print(addr, "berhasil terkoneksi")
            print("Jumlah client saat ini: ", len(self.clients),end="\n\n")

    def onReceiveMessage(self, conn,addr):
        try:
            while True:
                message = conn.recv(1024).decode()
                if not message:
                    self.deleteClient(conn,addr)
                    break
                print(f"{datetime.datetime.now()} {message}")

                self.sendMessage(message, conn)
        except Exception as e:
            print("An error occurred while receiving messages from a client:")
            print(e)

    def sendMessage(self, message, conn):
        for client in self.clients:
            if client != conn:
                try:
                    client.send(message.encode())
                except Exception as e:
                    print("An error occurred while forwarding message to a client:")
                    print(e)
        
    def deleteClient(self, conn, addr):
        self.clients.remove(conn)
        print(addr, "terputus")
        print("Jumlah client saat ini: ", len(self.clients),end="\n\n")

#Start server
hostname = socket.gethostname()
ipv4_address = socket.gethostbyname(hostname)
server = Server(ipv4_address,5000)
server.start()
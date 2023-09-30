#TP SISTER MOD 3
#ANGGOTA 1 : Muhammad Abiya Makruf - 1301213157 - MTA
#ANGGOTA 2 : Galih Akbar Nugraha - 1301213060 - AFN

#TCP Server
import socket
TCP_IP = ''
TCP_PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind((TCP_IP, TCP_PORT))
server.listen(2)
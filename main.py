from email import message
import socket
from sqlite3 import connect

socket_creer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_creer.bind(("127.0.0.1",56001))
socket_creer.listen(5)
while True:
    connexion_client, info_client = socket_creer.accept()
    ip = info_client[0]
    port = info_client[1]
    print(f"Message reçu du client est : {ip} et le port: {port}")
    donnees=connexion_client.recv(1024).decode("utf-8")
    print(donnees)
    reponse = "Mr " + donnees + " bienvenu a vous"
    donnees=connexion_client.sendall(reponse.encode("utf-8"))
    print(donnees)    
    connexion_client.close()

    










import socket

connexion_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
adresse = "127.0.0.1"
port = 56001

connexion_server.connect((adresse,port))
print("connexion au serveur")
print("ecrivez un message ici ") 
message = input(">")
connexion_server.send(message.encode("utf-8"))
reponse  = connexion_server.recv(236).decode("utf-8")
print(message.encode("utf-8"))
print("connexion fermee")

connexion_server.close()

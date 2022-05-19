#!/usr/bin/env python

#_*_coding: utf-8-*-

from tkinter import *
import mysql.connector
fenetre = Tk()
fenetre.geometry("650x500")
fenetre.title("MySQL&Python")

button = Button(fenetre, text="Quitter",bg="red", fg="white", command=fenetre.destroy)
button.place(x=580,y=465)


fenetre.mainloop()

conn=mysql.connector.connect(host="localhost",user="terance",password="passer236",database="python")
cursor = conn.cursor()
cursor.execute("""

        CREATE TABLE IF NOT EXISTS etudiants(

                id int(5) NOT NULL AUTO_INCREMENT,

                Nom varchar(20) DEFAULT NULL,

                Prenom varchar(30) DEFAULT NULL,

                Numcompte varchar(9),

                Matiere varchar(20),

                Notes varchar(4),

                PRIMARY KEY(id)

                );
        """)
#TEG

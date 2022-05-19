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

def ajouter():

    global one

    global two

    global tree

    global four

    global five

    labelOne = Label(fenetre,text="le Nom :")

    labelOne.grid(row = 1,column = 1,sticky = "E",padx = 10)

    one = Entry (fenetre)

    labelTwo = Label(fenetre, text="Prenom :")

    labelTwo.grid(row = 2,column = 1,sticky = "E",padx = 10)

    two = Entry(fenetre)

    two.grid(row = 2,column = 2)

    labelTree = Label(fenetre,text="Numcompte :")

    labelTree.grid(row = 3,column = 1,sticky = "E",padx =10)

    tree = Entry(fenetre)

    tree.grid(row = 3,column = 2)

    labelFour = Label(fenetre,text="Matiere :")

    labelFour.grid(row = 4,column = 1,sticky = "E",padx = 10)

    four = Entry(fenetre)

    four.grid(row = 4,column = 2)

    labelfive = Label(fenetre,text="Note :")

    labelFve.grid(row = 5,column = 1,sticky = "E",padx = 10)

    five = Entry(fenetre)

    five.gride(row = 5,column = 2)

def inserer():

    conn=mysql.connector.connect(host='localhost',user='terance',password='passer236',database='python')

    one.get()

    two.get()

    tree.get()

    four.get()

    five.get()

    req = "INSERT INTO etudiants (Nom,Prenom,Numcompte,Matiere,Notes) VALUES( %s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(req,(one.get(),two.get(),tree.get(),four.get(),five.get()))
    conn.commit()
    conn.close()

def afficher():

    conn=mysql.connector.connect(host='localhost',user='terance',password='passer236',database='python')
    cursor = conn.cursor()
    cursor.execute("SELECT Nom,Prenom,Numcompte,Matiere,Notes FROM etudiants")

    for ligne in cursor.fetchall():

        print(ligne)

        conn.close()

def supprimer():

    global entreeS

    labelS = Label(fenetre,text="Le Numero du compte de la personne à supprimer :")

    labelS.grid(row = 1,column = 1,sticky = "E",padx = 10)

    entreeS = Entry (fenetre)

    entreeS.grid(row = 1,column = 2)

def execution():

    conn=mysql.connector.connect(host='localhost',user='terance',password='passer236',database='python')

    entreeS.get()

    cursor = conn.cursor()

    sql = "DELETE FROM etudiants WHERE Numcompte = %s"

    element = (entreeS.get(),)

    conn.execute(sql,element)

    conn.commit()

    print(cursor.rowcount,"élément(s)supprimé(s)")

    conn.close()

def mise1():

    global entreeM

    global entreeN

    labelM = Label(fenetre,text="Le Numero du compte de la personne :")

    labelM.grid(row = 1,column = 1,sticky = "E",padx = 5)

    entreeM = Entry(fenetre)

    entreeM.grid(row = 1,column = 2)

    labelN = Label(fenetre,text ="Sa nouvelle note :")

    labelN.grid(row = 2,column = 1,sticky = "E",padx =5)

    entreeN = Entry(fenetre)

    entreeN.grid(row = 2 column 2)

def mise2():

    conn=mysql.connector.connect(host='localhost',user='terance',password='passer236',database='python')
    entreeM.get()
    entreeN.get()
    cursor = conn.cursor
    sql = "UPDATE etudiant SET Notes = %s WHERE Numcompte = %s"
    element2 = (entreeN.get(),entreeM.get(),)
    cursor.execute(sql,element2)
    conn.commit()
    print(cursor.rowcount,"Elément(s) modifié(s)")
    conn.close()
    menubar = Menu(fenetre,fg="white",bg="black")
    menu1 = Menu(menubar,tearoff=0)
    menu1.add_command(label="créer",command=inserer)
    menu1.add_separator()
    menu1.add_command(label="Fermer",command=fenetre.destroy)
    menubar.add_cascade(label="CRÉATION",menu=menu1)
    menu2 = Menu(menubar,tearoff=0)
    menu2.add_command(label="Afficher",command=afficher)
    menu2.add_separator()
    menu2.add_command(label="Fermer",command=fenetre.destroy)
    menubar_cascade(label="AFFICHAGE",menu=menu2)
    menu3 = Menu(menubar,tearoff=0)
    menu3.add_command(label="Suppimer",command=execution)
    menu3.add_separator()
    menu3.add_command(label="Fermer",command=fenetre.destroy)
    menubar.add_cascade(label="SUPPRESSION",menu=menu3)
    menu4 = Menu(menubar,tearoff=0)
    menu4.add_command(label="Mettre à jour",command=mise2)
    menu4.add_separator()
    menu4.add_command(label="Fermer",command=fenetre.destroy)
    menubar.add_cascade(label="MODIFIER",menu=menu4)
    fenetre.config(menu=menubar)

 


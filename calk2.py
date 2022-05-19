Calculatrice = True

while Calculatrice :
    Methode = input ("Que veux-tu faire ? n-Addition n-Soustraction n-Multiplication n-Division n-Arreter n Marque sans faute et avec une majuscule ce que tu as choisie ... n= ")
Methode = str (Methode)

if str(Methode) == 'Addition':
    print ("Tu as choisie {}".format (Methode))
    x = input ("Nombre 1 = ")
    y = input("Nombre 2 = ")
    x = float(x)
    y = float(y)
    print("Le resultat de ton addition est {}".format(float(x) + float(y)))
    print("n n")
    
    if str(Methode) == 'Sosutraction':
        print ("Tu as choisie {}".format (Methode))
        x = input ("Nombre 1 = ")
        y = input("Nombre 2 = ")
        x = float(x)
        y = float(y)
        print("Le resultat de ta soustraction est {}".format(float(x) - float(y)))
        print("n n")
        
        if str(Methode) == 'Multiplication':
            print ("Tu as choisie {}".format (Methode))
            x = input ("Nombre 1 = ")
            y = input("Nombre 2 = ")
            x = float(x)
            y = float(y)
            print("Le resultat de ta multiplication est {}".format(float(x) * float(y)))
            print("n n")
            
            if str(Methode) == 'Division':
                print ("Tu as choisie {}".format (Methode))
                x = input ("Nombre 1 = ")
                y = input("Nombre 2 = ")
                x = float(x)
                y = float(y)
                print("Le resultat de ta division est {}".format(float(x) / float(y)))
                print("n n")
                
                if str(Methode) == 'Arreter':
                    
                    break

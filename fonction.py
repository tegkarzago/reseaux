def tabx(n,x,i):
    t=list(range(n))
    for j in range(n):
        if j==n-i-1:
            t[j]=x
        else:
            t[j]=0
            return(t)

def liste(n):
    t=list(range(n))
    for i in range(n):
        t[i]=tabx(n,1,i)
        return(t)

def afficher_simple(t):
	for i in range(len(t)):
	    print(t[i],"",end="")
def affiche_double(t):
    for i in range(len(t)):
        affiche_simple(t[i])
        print("")
        affiche_double(liste(20))

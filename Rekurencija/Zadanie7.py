
def horner(tekst,x):
     wynik=ord(tekst[0])-40
     n=len(tekst)
     for i in range(1,n):
         wynik=wynik*x+ord(tekst(i))-40
     return

def horner1(tekst,x):
    lista = "51842374382590"
    if(len(tekst)==1):
        return lista.find(tekst(0))
    else:
        return x*horner1(tekst[0:])
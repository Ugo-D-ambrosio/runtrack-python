import math
def nombre():
    i=2
    print(2)
    while(i<1000):
        j=2
        nombreTrouver=False
        while(j<=i//2+1) and (nombreTrouver==False):
            if (i%j==0):
                nombreTrouver=True
            j+=1
        if nombreTrouver==False:
            print(i)
        i+=1

nombre()        
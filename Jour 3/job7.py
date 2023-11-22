def signe(langage):
    javascript=5
    python=4
    java=78
    reactjs=3
    if langage==javascript:
        return "tu es un developeur web"
    if langage==python:
        return "tu es un developpeur web"
    if langage==java:
        return "tu es un developpeur logiciel"
    if langage==reactjs:
        return "tu es un developpeur mobile"
    elif langage:
        return "un jour je serais le meilleur developpeur"
    
print(signe(4))
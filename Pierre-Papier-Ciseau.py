import random
print("Bienvenu sur mon nouveau jeu de pierre/papier/ciseau.")
a=input("Qu'elle est ton nom ?:")
loul=str(list(range(1000)))
b=input("Combien de tour veux tu jouer ?:")
while b not in loul :
    if b==loul:
        break
    b=input("J'ai dit un NOMBRE!!!:")
    continue
if b=="":
    b="0"
c =int(b)
opt=["pierre","papier","ciseau"]
i=0
egal=0
perdu=0
gagne=0
while c>i:
    rdm= random.randint(0,2)
    abc= opt[rdm]
    d=input("Appui sur 'q' pour quitter, ou joue en écrivant pierre/papier/ciseau :" )
    if d=="q":
        break
    if d not in opt:
        continue
    if d==abc:
        print("ORDI:",abc)
        print("égalité")
        egal+=1
    elif d=="pierre" and abc=="papier":
        print("ORDI:",abc)
        print("perdu")
        perdu+=1
    elif d=="pierre" and abc=="ciseau":
        print("ORDI:",abc)
        print("gagné")
        gagne+=1
    elif d=="papier" and abc=="ciseau":
        print("ORDI:",abc)
        print("perdu")
        perdu+=1
    elif d=="papier" and abc=="pierre":
        print("ORDI:",abc)
        print("gagné")
        gagne+=1
    elif d=="ciseau" and abc=="pierre":
        print("ORDI:",abc)
        print("perdu")
        perdu+=1
    elif d=="ciseau" and abc=="papier":
        print("ORDI:",abc)
        print("gagné")
        gagne+=1
    i+=1
print("Nombre d'égalité:",egal)
print("Nombre de victoire de",a,":",gagne)
print("Nombre de victoire de l'ORDI :",perdu)
if gagne>perdu:
    print("Gagnant :",a)
if gagne<perdu:
    print("Gagnant: Ordi")
if gagne==perdu:
    print("Egalité")
print("Merci d'avoir joué.")
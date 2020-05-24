#Auteur : Younes Anys
#Numero d'étudiant : 300145843
print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

nbre = int(input("Entrez un nombre entier"))
if nbre % 2 == 0 and nbre % 3 == 0 :
    print(nbre, "est divisible par 2 et par 3")
elif nbre % 2 == 0 or nbre % 3 == 0 :
    print(nbre, "est divisible par 2 ou par 3")
else :
    print(nbre, "pas divisible ni par 2 ni par 3")

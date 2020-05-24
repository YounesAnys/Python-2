#Auteur : Younes Anys
#Numero d'étudiant : 300145843
#Exercice 4


print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

a = int(input("Entrez la valeur de a :"))
b = int(input("Entrez la valeur de b :"))
c = int(input("Entrez la valeur de c :"))
disc = (b^2 -4*a*c)

if disc < 0 :
    print("Pas de racines réelles")
if disc >= 0 :
    print("Deux racines réelles :")
   

#pour a = 1.3 et b = 2.6 et c = 1.3 le programme ne donne pas la bonne reponse car a = c = 0.5*b le discriminant sera donc nul

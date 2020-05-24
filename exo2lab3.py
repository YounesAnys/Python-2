#Auteur : Younes Anys
#Numero d'étudiant : 300145843
print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

temp = int(input("Quelle est la température ?"))
if temp >= 80.0 :
    numAct = 1
elif temp >= 60.0 and temp < 80.0 :
    numAct = 2
elif temp >= 40.0 and temp < 60.0 :
    numAct = 3
else:
    numAct = 4
if numAct == 1 :
    print("l'activité recommendée est la natation")
elif numAct == 2 :
    print("l'activité recommendée est le soccer")
elif numAct == 3 :
    print("l'activité recommendée est le volleyball")
else:
    print("l'activité recommendée est le ski")

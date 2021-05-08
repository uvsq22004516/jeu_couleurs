
import random as rd

#Définition Variables pour la fonction

rouge = "firebrick2"
bleu = "deep sky blue"
vert = "forest green"
rose = "HotPink1"
orange = "dark orange"
jaune = "goldenrod2"
blanc = "snow"
    
couleurs_choisies = []
couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]


#
niveau = 2
#
def fct_couleurs() :

    var_couleurs = rd.randint(1, 6)


    if niveau == 1 :
        print(couleurs[var_couleurs])
    

    else :
        for i in range(var_couleurs, 0, -1) :
            rd.shuffle(couleurs)
            couleurs_choisies.append(couleurs[i])
            print(couleurs_choisies)
            couleurs.remove(couleurs[i])
            print(couleurs)
            
        print(var_couleurs)
    


fct_couleurs()

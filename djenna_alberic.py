
import random as rd

#Définition Variables pour la fonction couleurs

rouge = "firebrick2"
bleu = "deep sky blue"
vert = "forest green"
rose = "HotPink1"
orange = "dark orange"
jaune = "goldenrod2"
blanc = "snow"
    
couleurs_choisies = []
couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]

var_couleurs = rd.randint(0, 6)


niveau = 2



def fct_couleurs() :

    
   
    if niveau == 1 :
        print(couleurs[var_couleurs])
    

    else :
        for i in range(var_couleurs, 0, -1) :
            rd.shuffle(couleurs)
            couleurs_choisies.append(couleurs[i])
            couleurs.remove(couleurs[i])

        print(couleurs_choisies)    
        print(couleurs)    
        print(var_couleurs)
    
fct_couleurs()


#Definition Variables pour la fonction mots

mots = ["rouge", "Bleu", "Vert", "Rose", "Orange", "Jaune", "Blanc"]
mots_choisis = []


def fct_mots() :

    if niveau == 1 : 

        print(mots[var_couleurs])

    else : 
        for i in range(var_couleurs, 0, -1) :
            rd.shuffle(mots)
            mots_choisis.append(mots[i])
            mots.remove(mots[i])

    print(mots_choisis)            
    print(mots)
    print(var_couleurs)


fct_mots()
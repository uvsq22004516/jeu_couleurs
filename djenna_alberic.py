
import random as rd

#Définition Variables pour la fonction couleurs

rouge = "firebrick2"
bleu = "deep sky blue"
vert = "forest green"
rose = "HotPink1"
orange = "dark orange"
jaune = "goldenrod2"
blanc = "snow"


var_couleurs = rd.randint(1, 7)


niveau = 2



def fct_couleurs() :

    global var_couleurs

    global couleurs
    couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]

    global couleurs_choisies
    couleurs_choisies = []

   
    if niveau == 1 :
        rd.shuffle(couleurs)
        couleurs_choisies = couleurs[1]

    else :

        if var_couleurs < 7 :

            for i in range(var_couleurs, 0, -1) :

                rd.shuffle(couleurs)
                couleurs_choisies.append(couleurs[i])
                couleurs.remove(couleurs[i])
            print(var_couleurs)

        else :

            rd.shuffle(couleurs)
            couleurs_choisies = couleurs 
            print(var_couleurs)

    print(couleurs_choisies)    
       
   
    
fct_couleurs()


#Definition Variables pour la fonction mots

mots = ["Rouge", "Bleu", "Vert", "Rose", "Orange", "Jaune", "Blanc"]


def fct_mots() :

    global mots_choisis
    mots_choisis = []

    if niveau == 1 :
        rd.shuffle(mots)
        mots_choisis = mots[1]


    else : 

        if var_couleurs < 7 :

            

            for i in range(var_couleurs, 0, -1) :
                rd.shuffle(mots)
                mots_choisis.append(mots[i])
                mots.remove(mots[i])

        else :

            rd.shuffle(mots)
            mots_choisis = mots
            print(var_couleurs)
            
    print(mots_choisis)

                


fct_mots()

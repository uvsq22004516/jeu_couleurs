#consignes : https://moodle.uvsq.fr/moodle2021/pluginfile.php/198168/mod_resource/content/1/jeu_couleurs.pdf
################## Informations liées au groupe #######################

# groupe DLMP 5
# BEAUSSANT Alberic 
# BODEN Alexis 
# CHAMPENOIS Gabriel 
# LEMARECHAL Lucas 
# SAVEY Lucien 
# SEDDOUGUI Djenna 

# https://github.com/uvsq22004516/jeu_couleurs

#######################################################################################################
################## Fonctionnement du programme ########################################################


 
#######################################################################################################

################## import des librairies ##############################################################
import tkinter as tk
import random as rd


################## définition des variables globales / constantes #####################################
LARGEUR = 700
HAUTEUR = 450
NIVEAU = 0
var_couleurs = rd.randint(2, 6)
score = 0

### A SUPPRIMER PLUS TARD
#SUPER DIFFICILE POULOULOU
rouge = "firebrick2"
bleu = "deep sky blue"
vert = "forest green"
rose = "HotPink1"
orange = "dark orange"
jaune = "goldenrod2"
blanc = "snow"

couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]

mots = ["Rouge", "Bleu", "Vert", "Rose", "Orange", "Jaune", "Blanc"]



#######################################################################################################
################## MENU PRINCIPAL #####################################################################
#######################################################################################################
menu_principal = tk.Tk()
menu_principal.title("Jeu de couleurs (IN200 - projet n°2 - DLMP 5)")

def niv_1():
    global NIVEAU
    NIVEAU = 1
    menu_principal.destroy()

def niv_2():
    global NIVEAU
    NIVEAU = 2
    menu_principal.destroy()

def meilleurs_scores():
    pass


def règles_du_jeu():
    def retour_menu():
        règles_du_jeu_root.destroy()
    
    règles_du_jeu_root = tk.Tk()
    règles_du_jeu_root.title("Règles du Jeu de Couleurs")
    texte_règles1 = tk.Label(règles_du_jeu_root, text="***NIVEAU 1: Le joueur clique sur le bouton correspondant "
                                                    "à la couleur du seul mot qui s'affiche.\n S'il réussit il gagne" 
                                                    "1 point, sinon son score reste inchangé et le jeu continue.\n"
                                                    , font=("Comic Sans MS", "10"))
    texte_règles2 = tk.Label(règles_du_jeu_root, text="***NIVEAU 2:Le joueur clique sur les boutons correspondants" 
                                                    "à la couleur des mots qui s'affichent.\n S'il réussit il gagne" 
                                                    "1 point, sinon son score reste inchangé et le jeu continue."
                                                    , font=("Comic Sans MS", "10"))
    bouton_retour = tk.Button(règles_du_jeu_root, text="<--", command=retour_menu, font=("Comic Sans MS", "10"), relief="ridge", bd=5, bg="gainsboro", padx=10)
    texte_règles1.grid()
    texte_règles2.grid()
    bouton_retour.grid()
    règles_du_jeu_root.mainloop()


canvas = tk.Canvas(menu_principal, width = LARGEUR, height = HAUTEUR, bg = "gray85")

####cadre:
couleurs.reverse()
for i in range(0, len(couleurs)):
    canvas.create_line(((LARGEUR/7)*i, HAUTEUR-15),((LARGEUR/7)*(i+1), HAUTEUR-15), fill=couleurs[i], width=30)
for i in range(0, len(couleurs)):
    canvas.create_line((LARGEUR-15, (HAUTEUR/7)*i),(LARGEUR-15, (HAUTEUR/7)*(i+1)), fill=couleurs[i], width=30)

couleurs.reverse()
for i in range(0, len(couleurs)):
    canvas.create_line(((LARGEUR/7)*i, 15),((LARGEUR/7)*(i+1), 15), fill=couleurs[i], width=30)
for i in range(0, len(couleurs)):
    canvas.create_line((15, (HAUTEUR/7)*i),(15, (HAUTEUR/7)*(i+1)), fill=couleurs[i], width=30)


###AUTRE VERSION DU CADRE:
"""for i in range(0, len(couleurs)):
    canvas.create_line((LARGEUR-15, (HAUTEUR/7)*i),(15, (HAUTEUR/7)*(i+1)), fill=couleurs[i], width=30)"""


canvas.create_text((LARGEUR/2, HAUTEUR/6), text="JEU DE COULEURS", font=("Comic Sans MS", "20", "bold"))

bouton_niv_1 = tk.Button(menu_principal, text="NIVEAU 1", command=niv_1, font=("Comic Sans MS", "10"), relief="raised", bd=5, bg="gainsboro", padx=10)
bouton_niv_2 = tk.Button(menu_principal, text="NIVEAU 2", command=niv_2, font=("Comic Sans MS", "10"), relief="raised", bd=5, bg="gainsboro", padx=10)
bouton_meilleurs_scores = tk.Button(menu_principal, text="Meilleurs scores", command=meilleurs_scores, font=("Comic Sans MS", "10"), relief="sunken", bd=5, bg="gainsboro", padx=10)
bouton_règles = tk.Button(menu_principal, text="Règles du jeu", command=règles_du_jeu, font=("Comic Sans MS", "10"), relief="sunken", bd=5, bg="gainsboro", padx=10)


canvas.grid(row=0, rowspan=3, column=0, columnspan=5)
bouton_niv_1.grid(row=1, column=1)
bouton_niv_2.grid(row=1, column=3)
bouton_meilleurs_scores.grid(row=2, column=0)
bouton_règles.grid(row=2, column=4)

menu_principal.mainloop()








#######################################################################################################
################## JEU ################################################################################
#######################################################################################################
jeu = tk.Tk()
if NIVEAU == 1:
    jeu.title("Jeu de couleurs - Niveau 1")
elif NIVEAU == 2:
    jeu.title("Jeu de couleurs - Niveau 2")

################## définition des fonctions ###########################################################
temps = 30

def decompte() :
    global temps
    temps -= 1

    while temps > 0 :
        jeu.after(1000, decompte(), temps)
        return temps


def start():
    global score 
    score = 0
    global couleur_clique 
    couleur_clique= []
    fct_placement()

def reset():
    pass


def fct_couleurs() :

    global var_couleurs

    global couleurs
    couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]

    global couleurs_choisies
    couleurs_choisies = []

   
    if NIVEAU == 1 :
        rd.shuffle(couleurs)
        couleurs_choisies = couleurs[1]

    else :

        if var_couleurs < 7 :

            for i in range(var_couleurs, 0, -1) :

                rd.shuffle(couleurs)
                couleurs_choisies.append(couleurs[i])
                couleurs.remove(couleurs[i])
                
            return(var_couleurs)

        else :

            rd.shuffle(couleurs)
            couleurs_choisies = couleurs 
            return(var_couleurs)

    return(couleurs_choisies)    

         


#Definition Variables pour la fonction mots




def fct_mots() :

    global mots_choisis
    mots_choisis = []

    if NIVEAU == 1 :
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
            return(var_couleurs)
            
    return(mots_choisis)

score = 0

def clique(event):
    couleur_clique = []
    if len(couleur_clique) != len(couleurs_choisies):
        if 100 <= event.x <= 175 and 285 <= event.y <= 325 :
            if "firebrick2" in couleurs_choisies : 
                couleur_clique.append("Rouge")
            else :
                couleur_clique.append("faux")
        elif 206.25 <= event.x <= 281.25 and 285 <= event.y <= 325 :
            if "deep sky blue" in couleurs_choisies : 
                couleur_clique.append("Bleu")
            else :
                couleur_clique.append("faux")
        elif 312.5 <= event.x <= 387.5 and 285 <= event.y <=325  :
            if "forest green" in couleurs_choisies :
                couleur_clique.append("Vert")
            else :
                couleur_clique.append("faux")
        elif 418.75 <= event.x <= 493.75 and 285 <= event.y <= 325 :
            if "HotPink1" in couleurs_choisies :
                couleur_clique.append("Rose")
            else :
                couleur_clique.append("faux")
        elif 525 <= event.x <= 600 and 285 <= event.y <= 325 :
            if "dark orange" in couleurs_choisies :
                couleur_clique.append("Orange")
            else :
                couleur_clique.append("faux")
        elif 225 <= event.x <= 300 and 350 <= event.y <= 390 :
            if "goldenrod2" in couleurs_choisies :
                couleur_clique.append("Jaune")
            else :
                couleur_clique.append("faux")
        elif 400 <= event.x <= 475 and 350 <= event.y <= 390 :
            if "snow" in couleurs_choisies :
                couleur_clique.append("Blanc")
            else :
                couleur_clique.append("faux")
        print(couleur_clique)

    else : 
        pass

    if "faux" in couleur_clique:
        pass
    elif couleur_clique.count("Rouge")>1 :
        pass
    elif couleur_clique.count("Bleu")>1 :
        pass
    elif couleur_clique.count("Vert")>1 :
        pass
    elif couleur_clique.count("Rose")>1 :
        pass
    elif couleur_clique.count("Orange")>1 :
        pass
    elif couleur_clique.count("Jaune")>1 :
        pass
    elif couleur_clique.count("Blanc")>1 :
        pass
    else :
        score = score + 1

    print(score)
    print(couleur_clique)
    print(couleurs_choisies)
 

################## définition des widgets #############################################################
fond = tk.Canvas(jeu, width = LARGEUR, height = HAUTEUR, bg = "gray85")

###règle, score et chronomètre:
fond.create_text(LARGEUR//2, 20, text="Tapez la couleur des mots, et pas le texte des mots!!!", font=("Comic Sans MS", "10"))
fond.create_text(LARGEUR//2, 35, text="Score : 0", font=("Comic Sans MS", "10"))
fond.create_text(LARGEUR//2, 50, text = temps, font=("Comic Sans MS", "10"))


btn_demarrer = tk.Button(jeu, text="Démarrer", command=start, font=("Comic Sans MS", "10"), relief="groove", bd=5, bg="gainsboro", padx=18)
btn_reinitialiser = tk.Button(jeu, text="Réinitialiser", command=reset, font=("Comic Sans MS", "10"), relief="groove", bd=5, bg="gainsboro", padx=10)

###boutons de couleurs:
btn_rouge =  fond.create_rectangle((100, 285), (175, 325), fill="firebrick2", outline="firebrick2")
txt_btn_rge = fond.create_text(((100+175)/2, (285+325)/2), text="Rouge", font=("Arial", "10", "bold"))
btn_bleu =  fond.create_rectangle((206.25, 285), (281.25,325), fill="deep sky blue", outline="deep sky blue")
txt_btn_bleu = fond.create_text(((206.25+281.25)/2, (285+325)/2), text="Bleu", font=("Arial", "10", "bold"))
btn_vert =  fond.create_rectangle((312.5, 285), (387.5, 325), fill="forest green", outline="forest green")
txt_btn_vert = fond.create_text(((312.5+387.5)/2, (285+325)/2), text="Vert", font=("Arial", "10", "bold"))
btn_rose =  fond.create_rectangle((418.75, 285), (493.75, 325), fill="HotPink1", outline="HotPink1")
txt_btn_rose = fond.create_text(((418.75+493.75)/2, (285+325)/2), text="Rose", font=("Arial", "10", "bold"))
btn_orange =  fond.create_rectangle((525, 285), (600, 325), fill="dark orange", outline="dark orange")
txt_btn_orange = fond.create_text(((525+600)/2, (285+325)/2), text="Orange", font=("Arial", "10", "bold"))
btn_jaune =  fond.create_rectangle((225, 350), (300, 390), fill="goldenrod2", outline="goldenrod2")
txt_btn_jaune = fond.create_text(((225+300)/2, (350+390)/2), text="Jaune", font=("Arial", "10", "bold"))
btn_blanc = fond.create_rectangle((400, 350), (475, 390), fill="snow", outline="snow")
txt_btn_blanc = fond.create_text(((400+475)/2, (350+390)/2), text="Blanc", font=("Arial", "10", "bold"))


######################## Placement des mots 



def fct_placement() :

    global activation
    activation = 0

    fct_mots()
    fct_couleurs()

    if NIVEAU == 1 :

        fond.create_text(350, 190, text = mots_choisis, fill = couleurs_choisies, font=("Sitka Small", "20", "bold"))  

    if NIVEAU == 2 :
        
        pos_mot = 0
        placement_mots = 700 // var_couleurs
        pos_mot = pos_mot - placement_mots/2

        for i in range(var_couleurs, 0, -1) :

            pos_mot = pos_mot + placement_mots
            i = i-1
            fond.create_text(pos_mot ,150, text = mots_choisis[i], fill = couleurs_choisies[i], font = ("Sitka Small", "20", "bold"))
    jeu.bind("<Button-1>", clique)



def fct_delete_mots() :
    pass





#####Never Gonna Give You Up






################## événements liés aux widgets et appel à la boucle de gestion des événements #########

btn_demarrer.grid(row=4, column=0)
btn_reinitialiser.grid(row=4, column=5)

fond.grid(row=0, rowspan= 5, columnspan=6)


jeu.mainloop()





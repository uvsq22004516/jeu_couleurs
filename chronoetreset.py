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
var_demarrer = True

score = 0
score_tot = 0

temps = 30

var_couleurs = rd.randint(2, 6)


################## Couleurs
rouge = "firebrick2"
bleu = "deep sky blue"
vert = "forest green"
rose = "HotPink1"
orange = "dark orange"
jaune = "goldenrod2"
blanc = "snow"

couleurs = ["firebrick2", "deep sky blue", "forest green", "HotPink1", "dark orange", "goldenrod2", "snow"]
couleurs_choisies = []
couleur_clique= []

mots = ["Rouge", "Bleu", "Vert", "Rose", "Orange", "Jaune", "Blanc"]
mots_choisis = []



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

################## définition et placement des widgets #############################################################
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
################## Chronomètre:
boucle_temps=0

def chrono():
    """Change l'affichage du temps restant à intervalles réguliers (1 seconde)"""
    global var_demarrer, temps, boucle_temps
    if temps > 0:
        temps-=1
        fond.itemconfigure(tps_de_jeu, text="Temps restant : " + str(temps))
        boucle_temps = fond.after(1000, chrono)
    
    else:
        var_demarrer = False

        
###############################


################## Démarrer et réinitialiser:
def start():
    """Déclenche le chronomètre et l'affichage aléatoire de mots et couleurs"""
    global score, couleur_clique, fond, var_demarrer
    chrono()
    fct_placement()
    fond.bind("<Button-1>", clique)

def reset():
    """Réinitialise le score et le chronomètre sans 
    relancer automatiquement de nouvelle partie ni stocker le score de la partie non terminée"""
    global var_demarrer, temps, score
    var_demarrer = False
    score = 0
    fond.itemconfigure(score_partie, text="Score : " + str(score))
    temps = 30
    fond.itemconfigure(tps_de_jeu, text="Temps restant : " + str(temps))
    fond.after_cancel(boucle_temps)
#############################################


################## Fonction de choix aléatoire des couleurs:
def fct_couleurs() :
    """Pour un tour, cette fonction choisit aléatoirement la couleur d'affichage des mots"""
    global var_couleurs, couleurs, couleurs_choisies

    if NIVEAU == 1 :
        rd.shuffle(couleurs)
        couleurs_choisies = couleurs[1]
    

    else :
        for i in range(var_couleurs, 0, -1) :
                rd.shuffle(couleurs)
                couleurs_choisies.append(couleurs[i])
                couleurs.remove(couleurs[i])
        return(var_couleurs)

    return(couleurs_choisies)    
############################################################



################## Fonction de choix aléatoire des mots:
def fct_mots() :
    """Pour un tour, cette fonction choisit aléatoirement les mots qui s'affichent"""
    global mots_choisis

    if NIVEAU == 1 :
        rd.shuffle(mots)
        mots_choisis = mots[1]

    else : 
        if var_couleurs < 7 :
            for i in range(var_couleurs, 0, -1) :
                rd.shuffle(mots)
                mots_choisis.append(mots[i])
                mots.remove(mots[i])
            
    return(mots_choisis)
########################################################



######################## Placement des mots :
def fct_placement() :
    """Place le(s) mot(s) aléatoirement dans les emplacements définis dans la fonction"""
    global var_demarrer
    if var_demarrer == True:
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
                i -=1
                fond.create_text(pos_mot ,150, text = mots_choisis[i], fill = couleurs_choisies[i], font = ("Sitka Small", "20", "bold"))
    
    else:
        pass
#############################################


def fct_delete_mots() :
    """Supprime l'affichage actuel des mots et couleurs"""
    pass



######################## Incrémentation du score:
def compte_point_niv1():
    """Incrémente le score de 1 si la bonne couleur est choisie"""
    global score_tot
    if couleurs_choisies in couleur_clique[0]:
        score_tot = score + 1

    else : 
        pass

    print(couleurs_choisies)
    print(couleur_clique[0])
    print(score_tot)


def compte_point_niv2() :
    """Incrémente le score de 1 si les bonnes couleurs sont choisies par le joueur"""
    global score, score_tot

    if "faux" in couleur_clique:
        score_tot = score
    elif couleur_clique.count("Rouge")>1 :
        score_tot = score
    elif couleur_clique.count("Bleu")>1 :
        score_tot = score
    elif couleur_clique.count("Vert")>1 :
        score_tot = score
    elif couleur_clique.count("Rose")>1 :
        score_tot = score
    elif couleur_clique.count("Orange")>1 :
        score_tot = score
    elif couleur_clique.count("Jaune")>1 :
        score_tot = score
    elif couleur_clique.count("Blanc")>1 :
        score_tot = score
    else :
        score_tot = score + 1

    print(score_tot)

#################################################


def clique(event):
    """docstring"""
    if NIVEAU == 1:

        if len(couleur_clique) == 0 :

            if 100 <= event.x <= 175 and 285 <= event.y <= 325 :
                "firebrick2" in couleurs_choisies
                couleur_clique.append("firebrick2")
                

            elif 206.25 <= event.x <= 281.25 and 285 <= event.y <= 325 :
                "deep sky blue" in couleurs_choisies  
                couleur_clique.append("deep sky blue")
                
                
            elif 312.5 <= event.x <= 387.5 and 285 <= event.y <=325  :
                "forest green" in couleurs_choisies 
                couleur_clique.append("forest green")
               
                
            elif 418.75 <= event.x <= 493.75 and 285 <= event.y <= 325 :
                "HotPink1" in couleurs_choisies 
                couleur_clique.append("HotPink1")
                
                
            elif 525 <= event.x <= 600 and 285 <= event.y <= 325 :
                "dark orange" in couleurs_choisies 
                couleur_clique.append("dark orange")
                
            
            elif 225 <= event.x <= 300 and 350 <= event.y <= 390 :
                "goldenrod2" in couleurs_choisies 
                couleur_clique.append("goldenrod2")
                
            
            elif 400 <= event.x <= 475 and 350 <= event.y <= 390 :
                "snow" in couleurs_choisies 
                couleur_clique.append("snow")
                

        else : 
            pass
        compte_point_niv1()
        
          
    if NIVEAU == 2:
            
        if len(couleur_clique) < len(couleurs_choisies):
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
        
        
        if len(couleur_clique) == len(couleurs_choisies):
            compte_point_niv2()

        print(couleur_clique)
        print(couleurs_choisies)

######################## Passage au tour suivant:
def tour_suivant():
    global couleurs, couleur_clique, couleurs_choisies, mots, mots_choisis
    if NIVEAU == 1:
        pass

    elif NIVEAU == 2:
        if len(couleur_clique) == var_couleurs:
            couleurs = [rouge, bleu, vert, rose, orange, jaune, blanc]
            couleurs_choisies = []
            couleur_clique= []
            mots = ["Rouge", "Bleu", "Vert", "Rose", "Orange", "Jaune", "Blanc"]
            mots_choisis = []
            fct_placement()
            
    
################## définition des widgets #############################################################
fond = tk.Canvas(jeu, width = LARGEUR, height = HAUTEUR, bg = "gray85")

################## règle, score et chronomètre:
fond.create_text(LARGEUR//2, 20, text="Tapez la couleur des mots, et pas le texte des mots!!!", font=("Comic Sans MS", "10"))
score_partie = fond.create_text(LARGEUR//2, 35, text="Score : " + str(score), font=("Comic Sans MS", "10"))
tps_de_jeu = fond.create_text(LARGEUR//2, 50, text = "Temps restant : " + str(temps), font=("Comic Sans MS", "10"))


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



################## événements liés aux widgets et appel à la boucle de gestion des événements #########

btn_demarrer.grid(row=4, column=0)
btn_reinitialiser.grid(row=4, column=5)

fond.grid(row=0, rowspan= 5, columnspan=6)

jeu.mainloop()
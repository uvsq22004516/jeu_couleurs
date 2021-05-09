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

root = tk.Tk()
root.title("Jeu de couleurs (IN200 - projet n°2 - DLMP 5)")

################## définition des variables globales / constantes #####################################
LARGEUR = 700
HAUTEUR = 450

################## définition des fonctions ###########################################################
def start():
    pass

def reset():
    pass

################## définition des widgets #############################################################
canvas = tk.Canvas(root, width = LARGEUR, height = HAUTEUR, bg = "gray85")

###règle, score et chronomètre:
canvas.create_text(LARGEUR//2, 20, text="Tapez la couleur des mots, et pas le texte des mots!!!", font=("Comic Sans MS", "10"))
canvas.create_text(LARGEUR//2, 35, text="Score : 0", font=("Comic Sans MS", "10"))
canvas.create_text(LARGEUR//2, 50, text="Temps restant : 30", font=("Comic Sans MS", "10"))


btn_demarrer = tk.Button(root, text="Démarrer", command=start, font=("Comic Sans MS", "10"), relief="groove", bd=5, bg="gainsboro", padx=18)
btn_reinitialiser = tk.Button(root, text="Réinitialiser", command=reset, font=("Comic Sans MS", "10"), relief="groove", bd=5, bg="gainsboro", padx=10)
###boutons de couleurs:
btn_rouge =  canvas.create_rectangle((100, 285), (175, 325), fill="firebrick2", outline="firebrick2")
txt_btn_rge = canvas.create_text(((100+175)/2, (285+325)/2), text="Rouge", font=("Arial", "10", "bold"))
btn_bleu =  canvas.create_rectangle((206.25, 285), (281.25,325), fill="deep sky blue", outline="deep sky blue")
txt_btn_bleu = canvas.create_text(((206.25+281.25)/2, (285+325)/2), text="Bleu", font=("Arial", "10", "bold"))
btn_vert =  canvas.create_rectangle((312.5, 285), (387.5, 325), fill="forest green", outline="forest green")
txt_btn_vert = canvas.create_text(((312.5+387.5)/2, (285+325)/2), text="Vert", font=("Arial", "10", "bold"))
btn_rose =  canvas.create_rectangle((418.75, 285), (493.75, 325), fill="HotPink1", outline="HotPink1")
txt_btn_rose = canvas.create_text(((418.75+493.75)/2, (285+325)/2), text="Rose", font=("Arial", "10", "bold"))
btn_orange =  canvas.create_rectangle((525, 285), (600, 325), fill="dark orange", outline="dark orange")
txt_btn_orange = canvas.create_text(((525+600)/2, (285+325)/2), text="Orange", font=("Arial", "10", "bold"))
btn_jaune =  canvas.create_rectangle((225, 350), (300, 390), fill="goldenrod2", outline="goldenrod2")
txt_btn_jaune = canvas.create_text(((225+300)/2, (350+390)/2), text="Jaune", font=("Arial", "10", "bold"))
btn_blanc = canvas.create_rectangle((400, 350), (475, 390), fill="snow", outline="snow")
txt_btn_blanc = canvas.create_text(((400+475)/2, (350+390)/2), text="Blanc", font=("Arial", "10", "bold"))

################## événements liés aux widgets et appel à la boucle de gestion des événements #########

btn_demarrer.grid(row=4, column=0)
btn_reinitialiser.grid(row=4, column=5)

canvas.grid(row=0, rowspan= 5, columnspan=6)


root.mainloop()
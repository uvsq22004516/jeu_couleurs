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

#######################################################################
################## Fonctionnement du programme ########################


 
#######################################################################

################## import des librairies ##############################
import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Jeu de couleurs (IN200 - projet n°2 - DLMP 5)")

################## définition des variables globales ##################


################## définition des fonctions ###########################
def start():
    pass

def reset():
    pass

################## définition des widgets #############################
label0 = tk.Label(root, text="Tapez la couleur des mots, et pas le texte des mots!!!", font=("Comic Sans MS", "10"))
label1 = tk.Label(root, text="Score : 0", font=("Comic Sans MS", "10"))
label2 = tk.Label(root, text="Temps restant : 30", font=("Comic Sans MS", "10"))
btn_demarrer = tk.Button(root, text="Démarrer", font=("Comic Sans MS", "10"), relief="flat", bg="gainsboro", command=start)
btn_reinitialiser = tk.Button(root, text="Réinitialiser", font=("Comic Sans MS", "10"), relief="flat", bg="gainsboro", command=reset)

###boutons de couleurs:
btn_rouge =  tk.Button(root, text="Rouge", relief="flat", bg="firebrick2", font=("Helvetica", "10", "bold"))
btn_bleu =  tk.Button(root, text="Bleu", relief="flat", bg="deep sky blue", font=("Helvetica", "10", "bold"))
btn_vert =  tk.Button(root, text="Vert", relief="flat", bg="forest green", font=("Helvetica", "10", "bold"))
btn_rose =  tk.Button(root, text="Rose", relief="flat", bg="HotPink1", font=("Helvetica", "10", "bold"))
btn_orange =  tk.Button(root, text="Orange", relief="flat", bg="dark orange", font=("Helvetica", "10", "bold"))
btn_jaune =  tk.Button(root, text="Jaune", relief="flat", bg="goldenrod2", font=("Helvetica", "10", "bold"))
btn_blanc = tk.Button(root, text="Blanc", relief="flat", bg="snow", font=("Helvetica", "10", "bold"))

################## événements liés aux widgets et 
#                  appel à la boucle de gestion des événements ########

btn_demarrer.grid(row=6, column=0)
btn_reinitialiser.grid(row=6, column=4)
label0.grid(row=0, columnspan=5)
label1.grid(row=1, columnspan=5)
label2.grid(row=2, columnspan=5)
btn_rouge.grid(row=4, column=0)
btn_bleu.grid(row=4, column=1)
btn_vert.grid(row=4, column=2)
btn_rose.grid(row=4, column=3)
btn_orange.grid(row=4, column=4)
btn_jaune.grid(row=5, column=1)
btn_blanc.grid(row=5, column=3)



root.mainloop()


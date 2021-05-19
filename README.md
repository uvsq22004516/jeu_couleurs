# DEUXIEME PROJET : Jeu de couleurs 

test
test3
test4
testlucas


def réinitialiser():
    jeu.destroy()
  
  
  
  
  
  
  
  
  
  
    global score
    global decompte
    score = 0
    decompte = 30
    # effacer le texte
    # laisser au bon niveau



#####################
    jeu.destroy()
    menu_principal = tk.Tk()
    menu_principal.title("Jeu de couleurs (IN200 - projet n°2 - DLMP 5)")

    canvas = tk.Canvas(menu_principal, width = LARGEUR, height = HAUTEUR, bg = "gray85")

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


    jeu = tk.Tk()
    if NIVEAU == 1:
        jeu.title("Jeu de couleurs - Niveau 1")
    elif NIVEAU == 2:
        jeu.title("Jeu de couleurs - Niveau 2")

    fond = tk.Canvas(jeu, width = LARGEUR, height = HAUTEUR, bg = "gray85")

    ###règle, score et chronomètre:
    fond.create_text(LARGEUR//2, 20, text="Tapez la couleur des mots, et pas le texte des mots!!!", font=("Comic Sans MS", "10"))
    fond.create_text(LARGEUR//2, 35, text="Score : 0", font=("Comic Sans MS", "10"))
    fond.create_text(LARGEUR//2, 50, text="Temps restant : 30", font=("Comic Sans MS", "10"))


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
    

#####


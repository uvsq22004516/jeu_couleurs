import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Dessin")

#définition des fonctions:

def cercle():
    global objets
    x=rd.randint(0, 400)
    y=rd.randint(0, 400)

    objets.append(canvas.create_oval((x, y), (x+100, y+100), fill=color))

def carre():
    global objets
    x=rd.randint(0, 400)
    y=rd.randint(0, 400)

    objets.append(canvas.create_rectangle((x,y), (x+100, y+100), fill=color))

def croix():
    global objets
    x=rd.randint(0, 350)
    y=rd.randint(0, 350)

    objets.append(canvas.create_line((x, y-50), (x, y+50), fill=color))
    objets.append(canvas.create_line((x-50, y), (x+50, y), fill=color))


#choisir la couleur des figures:

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:O2x}{:02x}'.format(r, g, b)

def couleur():
    global color
    color = input("Choisir une couleur parmi: white, black, red, green, blue, cyan, yellow:")


# fonction undo:

def undo():
    global objets
    if len(objets) != 0:
        if canvas.type(objets[-1]) == "line":
            canvas.delete(objets[-1])
            del(objets[-1])
            canvas.delete(objets[-1])
            del(objets[-1])

        else:
            canvas.delete(objets[-1])
            del(objets[-1])

objets = []

#création des widgets:
HEIGHT=500
WIDTH=500

canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
bouton_couleur = tk.Button(root, command=couleur, text="Choisir une couleur")
bouton_cercle = tk.Button(root,command=cercle, text="Cercle")
bouton_carre = tk.Button(root,command=carre, text="Carré")
bouton_croix = tk.Button(root,command=croix, text="Croix")
bouton_undo = tk.Button(root, command=undo, text="Supprimer la dernière figure")

#placement des widgets:
canvas.grid(row=1, column=1, rowspan=3, columnspan=2)
bouton_couleur.grid(row=0, column=1)
bouton_cercle.grid(row=1, column=0)
bouton_carre.grid(row=2, column=0)
bouton_croix.grid(row=3, column=0)
bouton_undo.grid(row=0, column=2)

root.mainloop()
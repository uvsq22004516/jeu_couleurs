import tkinter as tk

window = tk.Tk()

temp_img = tk.PhotoImage(file='NGGYU.gif')
background_img = temp_img

can = tk.Canvas(window, width=1000, height=1000)
can.pack()

can.create_image(400, 300, image=background_img)

window.mainloop()



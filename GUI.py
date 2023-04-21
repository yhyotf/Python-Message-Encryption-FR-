import tkinter as tk
from methodes import *
from tkinter import ttk 


        
root = tk.Tk()
root.geometry('900x650')
root.title('Projet NSI')
root.configure(background="#15202b")

# Style de la fenêtre
style = ttk.Style(root)
style.configure("TFrame", background="#15202b")
style.configure("TLabel", background="#15202b", foreground="#333")
style.configure("TRadiobutton", background="#15202b", foreground="#333")

# Création de l'entrée du message
message_frame = ttk.Frame(root)
message_frame.pack(pady=200)
message_label = ttk.Label(message_frame, text="Entrez votre message et choisissez la méthode de chiffrement souhaité ", background="#15202b", foreground="#10ccbb", font="Bold 15",)
message_label.pack(side="top")
message_entry = tk.Entry(message_frame, font="Simsun 16 bold", bg="#273340", fg="#85929f", bd=5, relief="flat", justify="center")
message_entry.pack(side="bottom")

# Création des choix de méthodes
var = tk.IntVar()
options_frame = ttk.Frame(root)
options_frame.pack(pady=10)
option1 = tk.Radiobutton(options_frame, text="Rot13", variable=var, value=1, foreground="#7856ff", background="#15202b", font="Times 15 bold", cursor="mouse")
option1.pack(side="left")
option2 = tk.Radiobutton(options_frame, text="César", variable=var, value=2, foreground="#7856ff", background="#15202b", font="Times 15 bold",  cursor="mouse")
option2.pack(side="left")
option3 = tk.Radiobutton(options_frame, text="Vigenère", variable=var, value=3, foreground="#7856ff", background="#15202b",font="Times 15 bold",  cursor="mouse")
option3.pack(side="left")
option4 = tk.Radiobutton(options_frame, text="Carré de Polybe", variable=var, value=4, foreground="#7856ff", background="#15202b",font="Times 15 bold",  cursor="mouse")
option4.pack(side="left")

# Fonction gérant les choix des méthodes et la création du résultat 
def show_message():
    choice = var.get()
    message=message_entry.get()
    if choice == 1:
        output.config(text=rot13(message), font="Gothic 14 bold")
    elif choice == 2:
        message=message.split("/")
        output.config(text=cesar(message[0],int(message[1])), font="Gothic 14 bold")
    elif choice == 3:
        message=message.split("/")
        output.config(text=vigenere(message[0],message[1]), font="Gothic 14 bold")
    elif choice == 4:
        output.config(text=polybe(message), font="Gothic 14 bold")

# Création du boutton pour afficher le message
show_button = tk.Button(root, text="Chiffrer", command=show_message, foreground="#10ccbb", background="#15202b", cursor="mouse", width=40, font="Bold 14")
show_button.pack(pady=10)


# Création de la zone de la sortie du résultat
output = tk.Label(root, text="", foreground="#10ccbb", background="#15202b")
output.pack()


root.mainloop()

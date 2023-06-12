from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from io import BytesIO
import hashlib
import requests
import time
import webbrowser
from jinja2 import Environment, FileSystemLoader

def get_input():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    num = num_entry.get()
    email = email_entry.get()
    adresse = adresse_entry.get()
    pseudo = pseudo_entry.get()

    # Désactiver le bouton "Valider"
    submit_button.config(state=DISABLED)

    # Effacer le résumé précédent
    resume_label.config(text="")

    # Créer le résumé des informations saisies
    resume = ""
    if nom:
        resume += "Nom: " + nom + "\n"
    if prenom:
        resume += "Prénom: " + prenom + "\n"
    if num:
        resume += "Numéro: " + num + "\n"
    if email:
        resume += "Email: " + email + "\n"
    if adresse:
        resume += "Adresse: " + adresse + "\n"
    if pseudo:
        resume += "Pseudo: " + pseudo

    # Afficher le résumé
    resume_label.config(text=resume)

    # Effacer la photo précédente
    photo_label.config(image="")

    # Réactiver le bouton "Valider"
    submit_button.config(state=NORMAL)

def create_report():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    num = num_entry.get()
    email = email_entry.get()
    adresse = adresse_entry.get()
    pseudo = pseudo_entry.get()

    # Récupérer les URL
    urls = []
    if nom:
        urls.append("https://github.com/" + nom)
    if prenom:
        urls.append("https://github.com/" + prenom)
    if pseudo:
        urls.append("https://github.com/" + pseudo)

    # Effacer le résumé précédent
    resume_label.config(text="")

    # Effacer la photo précédente
    photo_label.config(image="")

    # Créer le rapport HTML
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    report = template.render(nom=nom, prenom=prenom, num=num, email=email, adresse=adresse, pseudo=pseudo)

    # Enregistrer le rapport dans un fichier
    with open('rapport.html', 'w') as file:
        file.write(report)

    # Ouvrir le rapport dans le navigateur par défaut
    webbrowser.open('rapport.html')

def quitter():
    fenetre.quit()

def open_creator():
    webbrowser.open('https://github.com')

def open_osint():
    webbrowser.open('https://github.com/your-username/osint')

fenetre = Tk()

# Afficher la fenêtre en plein écran
fenetre.attributes('-fullscreen', True)

# Frame pour l'en-tête
header_frame = Frame(fenetre)
header_frame.pack(padx=20, pady=20)

# Frame pour les éléments de gauche
left_frame = Frame(fenetre)
left_frame.pack(side=LEFT, padx=20, pady=20)

# Frame pour la liste de droite
right_frame = Frame(fenetre)
right_frame.pack(side=RIGHT, padx=20, pady=20)

label = Label(header_frame, text="osint", font=('Arial', 24, 'bold'))
label.pack()


# Ajoutez des labels et des champs de saisie pour chaque variable
nom_label = Label(left_frame, text="Nom :")
nom_label.pack(anchor='w')
nom_entry = Entry(left_frame)
nom_entry.pack(pady=5, anchor='w')

prenom_label = Label(left_frame, text="Prénom :")
prenom_label.pack(anchor='w')
prenom_entry = Entry(left_frame)
prenom_entry.pack(pady=5, anchor='w')

num_label = Label(left_frame, text="Numéro :")
num_label.pack(anchor='w')
num_entry = Entry(left_frame)
num_entry.pack(pady=5, anchor='w')

email_label = Label(left_frame, text="Email :")
email_label.pack(anchor='w')
email_entry = Entry(left_frame)
email_entry.pack(pady=5, anchor='w')

adresse_label = Label(left_frame, text="Adresse :")
adresse_label.pack(anchor='w')
adresse_entry = Entry(left_frame)
adresse_entry.pack(pady=5, anchor='w')

pseudo_label = Label(left_frame, text="Pseudo :")
pseudo_label.pack(anchor='w')
pseudo_entry = Entry(left_frame)
pseudo_entry.pack(pady=5, anchor='w')

# Ajoutez un bouton pour soumettre les valeurs
submit_button = Button(left_frame, text="Valider", command=get_input)
submit_button.pack(pady=20)

# Ajoutez un bouton pour créer un rapport
report_button = Button(right_frame, text="Créer un rapport", command=create_report)
report_button.pack(pady=20)

# Ajoutez un bouton pour quitter
quitter_button = Button(left_frame, text="Quitter", command=quitter)
quitter_button.pack()

# Ajoutez un Label pour le résumé
resume_label = Label(right_frame, text="", font=('Arial', 12), justify=LEFT)
resume_label.pack(anchor='ne', padx=20, pady=20)

# Ajoutez une liste à droite
liste = Listbox(right_frame)
liste.pack(fill='both', expand=True)

fenetre.mainloop()

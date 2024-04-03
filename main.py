import csv
import os
import sys
import time
from tkinter import filedialog, messagebox


def main(target_file: str):
    # Ouvrir le fichier .txt
    with open(target_file, 'r', encoding='utf-8') as file:
        # Lire chaque ligne du fichier
        lines = file.readlines()

    # Créer une liste pour stocker les données
    data = []

    # Parcourir chaque ligne du fichier .txt
    for i in range(1, len(lines)):
        # Ignorer les lignes vides
        if lines[i] == '\n':
            continue
        # Extraire la date et l'heure
        try:
            date_time = lines[i].strip().split(" - ")[0]
        except IndexError:
            date_time = ""

        # Extraire le nom de l'expéditeur
        try:
            sender = lines[i].strip().split(" - ")[1].split(":")[0].strip()
        except IndexError:
            sender = ""
        # Extraire le message
        try:
            message = lines[i].strip().split(": ")[1].strip()
        except IndexError:
            message = ""
        # Ajouter les données à la liste
        data.append([date_time, sender, message])

    # Créer un objet CSV
    with open(f'{target_file.split(".txt")[0]}.csv', 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='|')
        # Écrire l'en-tête du fichier CSV
        csvwriter.writerow(['Date/Heure', 'Expéditeur', 'Message'])
        # Écrire les données dans le fichier CSV
        csvwriter.writerows(data)

    messagebox.showinfo("Traitement termine", "Traitement terminé !")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Model du programme : Convert Whatsapp Discussion")
        print("Usage : python main.py <mode> {-f|-r}")
        print("Mode :")
        print("  -f : Fichier <'fichier .txt'>")
        print("  -r : Repertoire")
        time.sleep(5)
        sys.exit(2)
    elif sys.argv[1] == '-f':
        filename = sys.argv[2]
        main(filename)
    elif sys.argv[1] == '-r':
        target_folder = filedialog.askdirectory(title="Choisissez le dossier contenant les fichiers .txt")
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                if file.endswith('.txt'):
                    main(os.path.join(root, file))
    else:
        print("Mode invalide")

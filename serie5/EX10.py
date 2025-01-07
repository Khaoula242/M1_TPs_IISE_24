'''Exercice 10 : Application Finale
1. Créez une application simple qui combine plusieurs fonctionnalités :
 - L'utilisateur peut ajouter des contacts à un fichier CSV.
 - L'utilisateur peut afficher tous les contacts.
 - L'utilisateur peut rechercher un contact par nom.
 - L'utilisateur peut supprimer un contact'''

import csv

Contacts = "contacts.csv"

#####################################################""
def Create_contact_File():
    try:
        with open(Contacts, mode='x', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["Nom", "Prénom", "Téléphone", "Email"])
    except FileExistsError:
        pass  # File already exists, no action needed


######################################################""
def Ajouter_contact():
    print("\n=== Ajouter un Contact ===")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    telephone = input("Téléphone: ")
    email = input("Email: ")
    
    with open(Contacts, mode='a', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, prenom, telephone, email])
    print("Contact ajouté avec succès!")



################################################################""
def Afficher_contacts():
    print("\n=== Liste des Contacts ===")
    try:
        with open(Contacts, mode='r') as fichier:
            reader = csv.reader(fichier)
            contacts = list(reader)
            
            if len(contacts) <= 1:  
                print("Aucun contact trouvé.")
                return
            else: 
                for row in contacts:
                    print("\t\t".join(row))
    except FileNotFoundError:
        print("Le fichier de contacts n'existe pas encore.")


####################################################################
def Chercher_contact():
    print("\n=== Rechercher un Contact ===")
    NOM = input("Entrez le nom à rechercher: ").lower()
    T = False

    try:
        with open(Contacts, mode='r') as fichier:
            reader = csv.reader(fichier)
            for row in reader:
                if row[0].lower() == NOM:  
                    print("Contact trouvé:")
                    print(f"Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}, Email: {row[3]}")
                    T = True
                    break
            
            if not T:
                print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier de contacts n'existe pas encore.")



########################################################################
def Supprimer_contact():
    print("\n=== Supprimer un Contact ===")
    NOM = input("Entrez le nom du contact à supprimer: ").lower()
    new_contacts = []
    T = False

    try:
        with open(Contacts, mode='r') as fichier:
            reader = csv.reader(fichier)
            new_contacts = list(reader)
        
        # Check for the contact to delete
        for row in new_contacts[1:]:  # Skip header row
            if row[0].lower() == NOM:
                new_contacts.remove(row)
                T = True
                break
        if not T:
            print("Aucun contact trouvé avec ce nom.")
            return

        # Rewrite the updated contacts list to the file
        with open(Contacts, mode='w', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerows(new_contacts)
        
        print("Contact supprimé avec succès!")

    except FileNotFoundError:
        print("Le fichier de contacts n'existe pas encore.")





###########################################################################
if __name__ == '__main__':
    Create_contact_File()
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact par nom")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choice = input("Entrez votre choix: ")
        
        if choice == '1':
            Ajouter_contact()
        elif choice == '2':
            Afficher_contacts()
        elif choice == '3':
            Chercher_contact()
        elif choice == '4':
            Supprimer_contact()
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")



import contacts

def main():
    while True:
        print("\n--- Gestionnaire de Contacts ---")
        print("1. Ajouter un contact")
        print("2. Lister les contacts")
        print("3. Quitter")
        
        choix = input("Choisissez une option: ")
        
        if choix == "1":
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            email = input("Email: ")
            telephone = input("Téléphone: ")
            # Création d'un dictionnaire simple pour le contact
            contact = {
                "nom": nom,
                "prenom": prenom,
                "email": email,
                "telephone": telephone
            }
            contacts.ajouter_contact(contact)
            print("Contact ajouté avec succès !")
        elif choix == "2":
            print("\n--- Liste des contacts ---")
            contacts.lister_contacts()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()

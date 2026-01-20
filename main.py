import contacts

def main():
    while True:
        print("\n--- Gestionnaire de Contacts ---")
        print("1. Ajouter un contact")
        print("2. Lister les contacts")
        print("3. Supprimer un contact")
        print("4. Générer QR Code pour un contact")
        print("5. Quitter")
        
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
            print("\n--- Supprimer un contact ---")
            try:
                import json
                with open("contacts.json", "r") as f:
                    liste_contacts = json.load(f)
            except FileNotFoundError:
                print("Aucun contact trouvé.")
                continue

            if not liste_contacts:
                print("La liste est vide.")
                continue

            for idx, c in enumerate(liste_contacts):
                print(f"{idx + 1}. {c.get('prenom')} {c.get('nom')}")
            
            try:
                idx_choix = int(input("Entrez le numéro du contact à supprimer: ")) - 1
                if 0 <= idx_choix < len(liste_contacts):
                    contact_a_supprimer = liste_contacts[idx_choix]
                    contacts.supprimer_contact(
                        contact_a_supprimer.get('nom'),
                        contact_a_supprimer.get('prenom')
                    )
                else:
                    print("Numéro invalide.")
            except ValueError:
                print("Entrée invalide.")
        
        elif choix == "4":
            print("\n--- Sélectionner un contact pour le QR Code ---")
            # On doit d'abord charger les contacts pour les lister avec un index
            try:
                import json
                with open("contacts.json", "r") as f:
                    liste_contacts = json.load(f)
            except FileNotFoundError:
                print("Aucun contact trouvé.")
                continue

            if not liste_contacts:
                print("La liste est vide.")
                continue

            for idx, c in enumerate(liste_contacts):
                print(f"{idx + 1}. {c.get('prenom')} {c.get('nom')}")
            
            try:
                idx_choix = int(input("Entrez le numéro du contact: ")) - 1
                if 0 <= idx_choix < len(liste_contacts):
                    import vcard_generator
                    vcard_generator.display_qrcode(liste_contacts[idx_choix])
                else:
                    print("Numéro invalide.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()

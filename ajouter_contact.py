"""
Module pour l'ajout de contacts
Gère l'interface utilisateur pour ajouter un nouveau contact
"""
import contacts


def ajouter_contact_interface():
    """Interface utilisateur pour ajouter un contact"""
    print("\n--- Ajouter un contact ---")
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    email = input("Email: ")
    telephone = input("Téléphone: ")
    
    # Création d'un dictionnaire pour le contact
    contact = {
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "telephone": telephone
    }
    
    contacts.ajouter_contact(contact)
    print("✅ Contact ajouté avec succès !")

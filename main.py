"""
Gestionnaire de Contacts - Application CLI
Point d'entrée principal de l'application
"""
import json
import contacts
import ajouter_contact
import supprimer_contact
import vcard_generator


def lister_contacts_interface():
    """Interface pour lister les contacts"""
    print("\n--- Liste des contacts ---")
    contacts.lister_contacts()


def generer_qrcode_interface():
    """Interface pour générer un QR Code vCard"""
    print("\n--- Générer QR Code vCard ---")
    
    try:
        with open("contacts.json", "r") as f:
            liste_contacts = json.load(f)
    except FileNotFoundError:
        print("❌ Aucun contact trouvé.")
        return

    if not liste_contacts:
        print("❌ La liste est vide.")
        return

    # Affichage de la liste
    print("\nContacts disponibles :")
    for idx, c in enumerate(liste_contacts):
        print(f"  {idx + 1}. {c.get('prenom')} {c.get('nom')}")
    
    # Sélection du contact
    try:
        idx_choix = int(input("\nEntrez le numéro du contact: ")) - 1
        if 0 <= idx_choix < len(liste_contacts):
            vcard_generator.display_qrcode(liste_contacts[idx_choix])
        else:
            print("❌ Numéro invalide.")
    except ValueError:
        print("❌ Entrée invalide.")


def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("       GESTIONNAIRE DE CONTACTS")
    print("="*50)
    print("1. 📝 Ajouter un contact")
    print("2. 📋 Lister les contacts")
    print("3. 🗑️  Supprimer un contact")
    print("4. 📱 Générer QR Code vCard")
    print("5. 🚪 Quitter")
    print("="*50)


def main():
    """Fonction principale"""
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (1-5): ").strip()
        
        if choix == "1":
            ajouter_contact.ajouter_contact_interface()
        elif choix == "2":
            lister_contacts_interface()
        elif choix == "3":
            supprimer_contact.supprimer_contact_interface()
        elif choix == "4":
            generer_qrcode_interface()
        elif choix == "5":
            print("\n👋 Au revoir !")
            break
        else:
            print("\n❌ Option invalide. Veuillez choisir entre 1 et 5.")


if __name__ == "__main__":
    main()

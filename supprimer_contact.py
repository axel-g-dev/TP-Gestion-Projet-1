"""
Module pour la suppression de contacts
Gère l'interface utilisateur pour supprimer un contact existant
"""
import json
import contacts


def supprimer_contact_interface():
    """Interface utilisateur pour supprimer un contact"""
    print("\n--- Supprimer un contact ---")
    
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
        print(f"  {idx + 1}. {c.get('prenom')} {c.get('nom')} - {c.get('email')}")
    
    # Sélection du contact à supprimer
    try:
        idx_choix = int(input("\nEntrez le numéro du contact à supprimer: ")) - 1
        if 0 <= idx_choix < len(liste_contacts):
            contact_a_supprimer = liste_contacts[idx_choix]
            contacts.supprimer_contact(
                contact_a_supprimer.get('nom'),
                contact_a_supprimer.get('prenom')
            )
        else:
            print("❌ Numéro invalide.")
    except ValueError:
        print("❌ Entrée invalide.")

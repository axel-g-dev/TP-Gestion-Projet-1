import json

def ajouter_contact(contact, fichier="contacts.json"):
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    contacts.append(contact)
    with open(fichier, "w") as f:
        json.dump(contacts, f, indent=4)

def lister_contacts(fichier="contacts.json"):
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
        for c in contacts:
            print(c)
    except FileNotFoundError:
        print("Aucun contact trouvé.")

def supprimer_contact(nom, prenom, fichier="contacts.json"):
    """Supprime un contact basé sur le nom et le prénom."""
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print("Aucun contact trouvé.")
        return False
    
    contacts_filtres = [c for c in contacts if not (c.get('nom') == nom and c.get('prenom') == prenom)]
    
    if len(contacts) == len(contacts_filtres):
        print(f"Contact {prenom} {nom} non trouvé.")
        return False
    
    with open(fichier, "w") as f:
        json.dump(contacts_filtres, f, indent=4)
    
    print(f"Contact {prenom} {nom} supprimé avec succès.")
    return True
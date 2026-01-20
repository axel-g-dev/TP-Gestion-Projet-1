import qrcode
import sys

def generate_vcard_content(contact):
    """Génère le contenu textuel d'une vCard."""
    vcard = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{contact.get('nom', '')};{contact.get('prenom', '')};;;",
        f"FN:{contact.get('prenom', '')} {contact.get('nom', '')}",
        f"TEL;TYPE=CELL:{contact.get('telephone', '')}",
        f"EMAIL:{contact.get('email', '')}",
        "END:VCARD"
    ]
    return "\n".join(vcard)

def display_qrcode(contact):
    """Génère et affiche le QR Code pour un contact donné."""
    vcard_data = generate_vcard_content(contact)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)
    
    print(f"\n--- QR Code pour {contact.get('prenom')} {contact.get('nom')} ---")
    print("Scannez ce code pour ajouter le contact :")
    # print_ascii avec invert=True pour un meilleur contraste dans certains terminaux, 
    # ou standard. tty=True force l'output.
    try:
        qr.print_ascii(tty=True)
    except Exception as e:
        print(f"Erreur lors de l'affichage du QR Code: {e}")

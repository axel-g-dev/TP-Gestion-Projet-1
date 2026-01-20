import qrcode
import io

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
    """Génère et affiche une carte de visite professionnelle avec QR Code intégré."""
    vcard_data = generate_vcard_content(contact)
    
    # Configuration du QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1, # Bordure minimale car on va ajouter notre propre cadre
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)
    
    # Capture du QR code ASCII
    f = io.StringIO()
    qr.print_ascii(out=f, invert=True)
    f.seek(0)
    qr_lines = [line.rstrip() for line in f.readlines()]
    
    # Calcul de la largeur
    qr_width = len(qr_lines[0]) if qr_lines else 0
    # Largeur minimale pour le texte (environ 40-50 chars) ou largeur du QR code si plus grand
    card_width = max(50, qr_width + 8) 
    
    # Définition des éléments de bordure
    TL, TR, BL, BR = "╔", "╗", "╚", "╝"
    H, V = "═", "║"
    
    # Données du contact
    nom_complet = f"{contact.get('prenom', '')} {contact.get('nom', '')}".upper()
    email = contact.get('email', '')
    tel = fmt_tel = contact.get('telephone', '')
    
    # Fonction pour centrer le texte avec remplissage
    def center_text(text, width, border_char=V):
        pad_len = width - 2 - len(text)
        left_pad = pad_len // 2
        right_pad = pad_len - left_pad
        return f"{border_char}{' ' * left_pad}{text}{' ' * right_pad}{border_char}"

    # Construction de la carte
    print("\n")
    print(f"{TL}{H * (card_width - 2)}{TR}")
    print(center_text("", card_width))
    print(center_text("PROFESSIONAL  CONTACT", card_width))
    print(center_text("", card_width))
    print(center_text(nom_complet, card_width))
    print(center_text("-" * (len(nom_complet) + 4), card_width))
    print(center_text("", card_width))
    
    # Contact info
    print(center_text(f"Email : {email}", card_width))
    print(center_text(f"Tél   : {tel}", card_width))
    print(center_text("", card_width))
    print(f"{V}{H * (card_width - 2)}{V}")
    
    # Insertion du QR Code centré
    # On doit s'assurer que le QR code est centré dans la largeur de la carte
    for line in qr_lines:
        # Le QR code contient des caractères spéciaux, la longueur visuelle compte
        # print_ascii utilise des blocs qui font 1 char de large.
        # on centre la ligne brute dans l'espace disponible
        padding_total = card_width - 2 - len(line)
        if padding_total > 0:
            pad_l = padding_total // 2
            pad_r = padding_total - pad_l
            print(f"{V}{' ' * pad_l}{line}{' ' * pad_r}{V}")
        else:
            # Si le QR est plus large (peu probable vu le max() au début), on tronque ou on affiche tel quel
            print(f"{V} {line} {V}")

    print(f"{BL}{H * (card_width - 2)}{BR}")
    print("\n")

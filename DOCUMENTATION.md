# Documentation Technique - Gestionnaire de Contacts

## Table des matières

1. [Introduction](#introduction)
2. [Architecture du projet](#architecture-du-projet)
3. [Modules et fonctions](#modules-et-fonctions)
4. [Guide d'installation](#guide-dinstallation)
5. [Guide d'utilisation](#guide-dutilisation)
6. [Format des données](#format-des-données)
7. [Gestion des erreurs](#gestion-des-erreurs)
8. [Maintenance et évolution](#maintenance-et-évolution)

---

## Introduction

Le **Gestionnaire de Contacts** est une application CLI (Command Line Interface) développée en Python permettant de gérer une base de contacts locale. L'application offre des fonctionnalités CRUD complètes avec génération de cartes vCard au format QR Code.

### Objectifs du projet

- Gérer une liste de contacts de manière simple et efficace
- Stocker les données localement au format JSON
- Générer des QR Codes vCard pour partage rapide
- Démontrer une architecture modulaire propre

---

## Architecture du projet

### Principe de séparation des responsabilités

Le projet suit une architecture en couches :

```
┌─────────────────────────────────────┐
│      main.py (Orchestrateur)       │
├─────────────────────────────────────┤
│  Couche Présentation (Interfaces)  │
│  - ajouter_contact.py               │
│  - supprimer_contact.py             │
├─────────────────────────────────────┤
│  Couche Données (CRUD)              │
│  - contacts.py                      │
├─────────────────────────────────────┤
│  Couche Utilitaires                 │
│  - vcard_generator.py               │
├─────────────────────────────────────┤
│  Stockage (JSON)                    │
│  - contacts.json                    │
└─────────────────────────────────────┘
```

### Avantages de cette architecture

- **Maintenabilité** : Chaque module a une responsabilité unique
- **Réutilisabilité** : Les fonctions peuvent être appelées indépendamment
- **Testabilité** : Les modules peuvent être testés individuellement
- **Évolutivité** : Facile d'ajouter de nouvelles fonctionnalités

---

## Modules et fonctions

### contacts.py - Module de gestion des données

**Responsabilité** : Opérations CRUD sur le fichier JSON

#### Fonctions

##### `ajouter_contact(contact, fichier="contacts.json")`

Ajoute un nouveau contact au fichier JSON.

**Paramètres** :
- `contact` (dict) : Dictionnaire contenant les informations du contact
- `fichier` (str) : Chemin du fichier JSON (par défaut : "contacts.json")

**Retour** : Aucun

**Exemple** :
```python
contact = {
    "nom": "Dupont",
    "prenom": "Jean",
    "email": "jean.dupont@example.com",
    "telephone": "0601020304"
}
contacts.ajouter_contact(contact)
```

##### `lister_contacts(fichier="contacts.json")`

Affiche tous les contacts enregistrés.

**Paramètres** :
- `fichier` (str) : Chemin du fichier JSON

**Retour** : Aucun (affichage console)

##### `supprimer_contact(nom, prenom, fichier="contacts.json")`

Supprime un contact basé sur le nom et le prénom.

**Paramètres** :
- `nom` (str) : Nom de famille du contact
- `prenom` (str) : Prénom du contact
- `fichier` (str) : Chemin du fichier JSON

**Retour** : 
- `True` si la suppression a réussi
- `False` si le contact n'a pas été trouvé

---

### ajouter_contact.py - Interface d'ajout

**Responsabilité** : Gérer l'interaction utilisateur pour l'ajout de contacts

#### Fonction principale

##### `ajouter_contact_interface()`

Affiche un formulaire interactif pour saisir un nouveau contact.

**Paramètres** : Aucun

**Retour** : Aucun

**Comportement** :
1. Demande à l'utilisateur de saisir : nom, prénom, email, téléphone
2. Crée un dictionnaire avec les données
3. Appelle `contacts.ajouter_contact()` pour sauvegarder
4. Affiche un message de confirmation

---

### supprimer_contact.py - Interface de suppression

**Responsabilité** : Gérer l'interaction utilisateur pour la suppression de contacts

#### Fonction principale

##### `supprimer_contact_interface()`

Affiche la liste des contacts et permet d'en supprimer un.

**Paramètres** : Aucun

**Retour** : Aucun

**Comportement** :
1. Charge et affiche la liste des contacts
2. Demande à l'utilisateur de choisir un numéro
3. Appelle `contacts.supprimer_contact()` avec les informations du contact sélectionné
4. Gère les erreurs (liste vide, numéro invalide)

---

### vcard_generator.py - Générateur de QR Code

**Responsabilité** : Générer et afficher des cartes vCard au format QR Code

#### Fonctions

##### `generate_vcard_content(contact)`

Génère le contenu textuel d'une vCard au format vCard 3.0.

**Paramètres** :
- `contact` (dict) : Dictionnaire contenant les informations du contact

**Retour** : 
- `str` : Contenu de la vCard formaté

**Format vCard 3.0** :
```
BEGIN:VCARD
VERSION:3.0
N:Nom;Prenom;;;
FN:Prenom Nom
TEL;TYPE=CELL:0601020304
EMAIL:email@example.com
END:VCARD
```

##### `display_qrcode(contact)`

Génère et affiche une carte de visite professionnelle avec QR Code.

**Paramètres** :
- `contact` (dict) : Dictionnaire contenant les informations du contact

**Retour** : Aucun (affichage console)

**Caractéristiques** :
- Cadre ASCII élégant
- Informations du contact formatées
- QR Code scannable directement dans le terminal

---

### main.py - Point d'entrée principal

**Responsabilité** : Orchestrer l'application et gérer le menu principal

#### Fonctions

##### `afficher_menu()`

Affiche le menu principal de l'application.

##### `lister_contacts_interface()`

Wrapper pour afficher la liste des contacts.

##### `generer_qrcode_interface()`

Gère l'interaction utilisateur pour la génération de QR Code.

##### `main()`

Boucle principale de l'application.

**Workflow** :
1. Affichage du menu
2. Lecture du choix utilisateur
3. Appel du module correspondant
4. Retour au menu (ou sortie si option 5)

---

## Guide d'installation

### Prérequis

- Python 3.x installé
- pip (gestionnaire de paquets Python)
- Git (optionnel pour cloner le projet)

### Étapes d'installation

1. **Cloner le dépôt** (ou télécharger les fichiers)
   ```bash
   git clone https://github.com/axel-g-dev/TP-Gestion-Projet-1.git
   cd TP-Gestion-Projet-1
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python3 -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Linux/Mac :
     ```bash
     source venv/bin/activate
     ```
   - Windows :
     ```bash
     venv\Scripts\activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install qrcode
   ```

5. **Vérifier l'installation**
   ```bash
   python3 -m py_compile main.py contacts.py ajouter_contact.py supprimer_contact.py vcard_generator.py
   ```

---

## Guide d'utilisation

### Lancer l'application

```bash
python3 main.py
```

### Menu principal

```
==================================================
       GESTIONNAIRE DE CONTACTS
==================================================
1. Ajouter un contact
2. Lister les contacts
3. Supprimer un contact
4. Générer QR Code vCard
5. Quitter
==================================================
```

### Cas d'utilisation

#### 1. Ajouter un contact

1. Sélectionner l'option `1`
2. Saisir les informations demandées :
   - Nom
   - Prénom
   - Email
   - Téléphone
3. Le contact est automatiquement sauvegardé

#### 2. Lister les contacts

1. Sélectionner l'option `2`
2. Tous les contacts sont affichés au format dictionnaire

#### 3. Supprimer un contact

1. Sélectionner l'option `3`
2. La liste des contacts est affichée avec des numéros
3. Saisir le numéro du contact à supprimer
4. Confirmation de suppression

#### 4. Générer un QR Code

1. Sélectionner l'option `4`
2. Choisir un contact dans la liste
3. Une carte de visite professionnelle s'affiche avec le QR Code
4. Scanner le QR Code avec un smartphone pour ajouter le contact

---

## Format des données

### Structure du fichier contacts.json

```json
[
    {
        "nom": "Dupont",
        "prenom": "Jean",
        "email": "jean.dupont@example.com",
        "telephone": "0601020304"
    },
    {
        "nom": "Martin",
        "prenom": "Marie",
        "email": "marie.martin@example.com",
        "telephone": "0605060708"
    }
]
```

### Schéma d'un contact

| Champ      | Type   | Obligatoire | Description                |
|------------|--------|-------------|----------------------------|
| nom        | string | Oui         | Nom de famille             |
| prenom     | string | Oui         | Prénom                     |
| email      | string | Oui         | Adresse email              |
| telephone  | string | Oui         | Numéro de téléphone        |

**Note** : Aucune validation n'est effectuée sur le format des données. Il est de la responsabilité de l'utilisateur de saisir des informations correctes.

---

## Gestion des erreurs

### Fichier contacts.json inexistant

**Comportement** : Le fichier est automatiquement créé lors du premier ajout de contact.

### Liste de contacts vide

**Comportement** : Message informatif affiché à l'utilisateur.

### Saisie utilisateur invalide

**Comportement** : 
- Pour les choix de menu : Message "Option invalide"
- Pour les index de sélection : Message "Numéro invalide" ou "Entrée invalide"

### Exceptions gérées

- `FileNotFoundError` : Fichier contacts.json inexistant
- `ValueError` : Conversion de chaîne en entier échouée
- `json.JSONDecodeError` : Fichier JSON corrompu (non géré actuellement)

---

## Maintenance et évolution

### Bonnes pratiques

1. **Sauvegarde régulière** : Faire des copies du fichier `contacts.json`
2. **Environnement virtuel** : Toujours utiliser venv pour isoler les dépendances
3. **Version Control** : Utiliser Git pour suivre les modifications du code

### Améliorations possibles

#### Fonctionnalités

- [ ] Recherche de contacts par nom, email ou téléphone
- [ ] Modification de contacts existants
- [ ] Export/Import CSV
- [ ] Validation des formats (email, téléphone)
- [ ] Interface graphique (GUI)
- [ ] Base de données SQLite

#### Technique

- [ ] Tests unitaires (pytest)
- [ ] Gestion des doublons
- [ ] Logging des opérations
- [ ] Configuration externe (config.json)
- [ ] Internationalisation (i18n)

### Structure de test recommandée

```
TP-Gestion-Projet-1/
├── tests/
│   ├── test_contacts.py
│   ├── test_vcard_generator.py
│   └── fixtures/
│       └── sample_contacts.json
├── docs/
│   └── DOCUMENTATION.md
└── ...
```

---

## Dépannage

### Le QR Code ne s'affiche pas correctement

**Solution** : Vérifier que le terminal supporte l'affichage ASCII. Essayer avec un autre terminal.

### Erreur d'import de modules

**Solution** : Vérifier que l'environnement virtuel est activé et que qrcode est installé.

### Fichier JSON corrompu

**Solution** : Supprimer le fichier `contacts.json` (sauvegarde recommandée) et redémarrer l'application.

---

## Informations complémentaires

**Version** : 1.0.0  
**Langage** : Python 3.x  
**Dépendances** : qrcode  
**Licence** : Non spécifiée  
**Support** : GitHub Issues

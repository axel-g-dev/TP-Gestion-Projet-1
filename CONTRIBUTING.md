# Guide de contribution

Merci de votre intérêt pour contribuer au projet TP-Gestion-Projet-1.

## Processus de contribution

### 1. Fork et Clone

```bash
git clone https://github.com/axel-g-dev/TP-Gestion-Projet-1.git
cd TP-Gestion-Projet-1
```

### 2. Créer une branche

Utilisez une convention de nommage claire :

```bash
git checkout -b feature/nom-de-la-fonctionnalite
# ou
git checkout -b fix/description-du-bug
```

### 3. Configuration de l'environnement

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install qrcode
```

### 4. Développement

- Respectez l'architecture modulaire existante
- Suivez les conventions de code Python (PEP 8)
- Testez vos modifications localement
- Supprimez tous les emojis du code et des commentaires

### 5. Commits

Utilisez des messages de commit clairs et descriptifs :

```bash
git add .
git commit -m "Description claire des modifications"
```

Format recommandé :
- `Add` : Ajout de nouvelles fonctionnalités
- `Fix` : Correction de bugs
- `Update` : Mise à jour de fonctionnalités existantes
- `Remove` : Suppression de code obsolète
- `Refactor` : Restructuration du code

### 6. Push et Pull Request

```bash
git push origin feature/nom-de-la-fonctionnalite
```

Créez ensuite une Pull Request sur GitHub avec :
- Une description détaillée des modifications
- Le numéro de l'issue associée (si applicable)
- Les tests effectués

## Standards de code

### Style Python

- Suivre PEP 8
- Utiliser des noms de variables explicites en français
- Documenter les fonctions complexes
- Pas d'emojis dans le code ou les commentaires

### Structure des fichiers

Respectez l'architecture modulaire :

```
TP-Gestion-Projet-1/
├── contacts.py             # Couche de données (CRUD)
├── ajouter_contact.py      # Interface d'ajout
├── supprimer_contact.py    # Interface de suppression
├── vcard_generator.py      # Génération de QR Codes
└── main.py                 # Menu principal
```

### Gestion des issues

- Créez une issue avant de commencer le développement
- Assignez-vous l'issue
- Utilisez les labels appropriés : `feature`, `bug`, `documentation`, `test`
- Associez l'issue à un milestone (Sprint)
- Ajoutez une date d'échéance

### Tests

Avant de soumettre une Pull Request :

1. Testez toutes les fonctionnalités modifiées
2. Vérifiez que l'application démarre sans erreur : `python3 main.py`
3. Testez chaque option du menu
4. Vérifiez le fichier `contacts.json` après chaque opération

## Workflow Git

```
main
  └─ feature/nouvelle-fonctionnalite
       └─ Développement
            └─ Tests
                 └─ Pull Request
                      └─ Review
                           └─ Merge vers main
```

## Labels disponibles

- `feature` : Nouvelle fonctionnalité
- `bug` : Correction de bug
- `documentation` : Mise à jour de la documentation
- `test` : Ajout ou modification de tests
- `enhancement` : Amélioration d'une fonctionnalité existante

## Milestones (Sprints)

- **Sprint 1** : Développement des fonctionnalités principales
- **Sprint 2** : Tests et documentation

## Code de conduite

- Respectez les autres contributeurs
- Soyez constructif dans vos commentaires
- Restez professionnel dans vos échanges
- Acceptez les critiques constructives

## Questions

Pour toute question, ouvrez une issue avec le label `question` ou contactez l'équipe du projet.

## Licence

En contribuant à ce projet, vous acceptez que vos contributions soient sous licence MIT.

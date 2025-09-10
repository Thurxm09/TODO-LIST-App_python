# TODO-LIST-App_python

## Auteur : Thurxm09

## Date : 2024-06-10

## Description : Une application de gestion de tâches (TODO List) développée en Python avec une interface graphique moderne.

## Installation

1. Clonez le dépôt: `git clone https://github.com/votre-utilisateur/TODO-LIST-App_python.git`
2. Allez dans le dossier: `cd TODO-LIST-App_python`
3. Installez les dépendances: `pip install -r requirements.txt`

## Utilisation

Lancez l'application avec: `python app/main.py`

## Contribuer

Les contributions sont les bienvenues! Veuillez lire [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

# TODO-LIST-App_python

## Résumé

TODO-LIST-App_python est une application de gestion de tâches (TODO list) écrite en Python avec une interface graphique légère. Elle vise à fournir une base claire et testable pour une application de productivité personnelle, avec une architecture modulaire (models/controllers/storage/ui) et des outils de qualité (linters, tests, CI).

Points forts

- Architecture simple et modulaire (MVC-like).
- Tests unitaires et workflows CI configurés.
- Scripts utilitaires pour validation de configuration.
- Conception pensée pour être extensible (stockage, UI, contrôleurs).

## Table des matières

1. Installation rapide
2. Prérequis
3. Installation détaillée
4. Lancer l'application
5. Tests et linters
6. Structure du projet
7. Développement et contribution
8. Recommandations de sécurité
9. Déploiement
10. FAQ et dépannage
11. Licence
12. Contact

1) Installation rapide

---

Ouvrez un terminal, clonez le dépôt et installez les dépendances :

```powershell
git clone https://github.com/Thurxm09/TODO-LIST-App_python.git
cd TODO-LIST-App_python
C:/Users/Admin/anaconda3/python.exe -m pip install --user -r requirements.txt
```

Remarque: remplacez la commande Python par l'exécutable approprié de votre environnement (venv, conda...).

2. Prérequis

---

- Python 3.10+ (testé avec 3.11)
- pip
- (optionnel) virtualenv ou conda pour isoler l'environnement

3. Installation détaillée

---

Recommandé : créer un environnement virtuel pour le projet.

Windows (cmd.exe) :

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Conda :

```bash
conda create -n todo-app python=3.11
conda activate todo-app
python -m pip install -r requirements.txt
```

4. Lancer l'application

---

Depuis la racine du projet :

```cmd
python app\main.py
```

Si vous utilisez un environnement virtuel, assurez‑vous de l'activer avant d'exécuter la commande.

5. Tests et linters

---

Le projet intègre des outils de qualité : black, isort, flake8, pytest et safety (scans de dépendances). Exécutez-les localement comme suit :

```cmd
C:/Users/Admin/anaconda3/python.exe -m pip install --user -r requirements.txt
C:/Users/Admin/anaconda3/python.exe -m black --check .
C:/Users/Admin/anaconda3/python.exe -m isort --check-only .
C:/Users/Admin/anaconda3/python.exe -m flake8
C:/Users/Admin/anaconda3/python.exe -m pytest -q
```

Notes :

- `black --check` vérifie le formatage ; pour reformater, exécutez `black .`.
- `isort --check-only` vérifie l'ordre des imports ; pour appliquer : `isort .`.

6. Structure du projet

---

Arborescence clé (extraits) :

- `app/` : code applicatif (controllers, models, storage, ui)
- `tests/` : tests unitaires et d'intégration
- `.github/` : workflows CI, templates, scripts de validation
- `requirements.txt`, `pyproject.toml` : dépendances et config dev

Fichiers importants :

- `app/main.py` : point d'entrée de l'application
- `app/controllers/task_controller.py` : logique de gestion des tâches
- `app/storage/storage.py` : interface de stockage (JSON par défaut)

7. Développement et contribution

---

Avant de soumettre une pull request :

1. Créez une branche à partir de `main` :

```cmd
git checkout -b feature/ma-nouvelle-fonction
```

2. Implémentez et ajoutez des tests unitaires pour toute logique non triviale.
3. Exécutez les linters et tests localement (voir section 5).
4. Ouvrez une Pull Request décrivant le changement et les raisons.

Conventions de commit recommandées : suivez le format "type: description" (ex. `feat: add due date support`, `fix: handle empty storage file`).

Voir `CONTRIBUTING.md` pour plus de détails sur le processus de revue.

8. Recommandations de sécurité

---

- Ne commitez jamais de secrets (tokens, clés privées). Utilisez GitHub Secrets pour CI.
- Activez la protection de la branche `main` (PR obligatoire, checks requis). Voir `.github` pour les workflows CI requis.
- Activez CodeQL et dependency scanning dans GitHub pour détecter vulnérabilités.

9. Déploiement

---

Cette application est conçue pour usage local (desktop). Pour déploiement en conteneur ou sur serveur :

- Containerisation : ajoutez un Dockerfile qui installe Python et copie le projet.
- Services : si vous transformez l'app en service web, séparez l'UI et l'API, puis exposez l'API via un serveur ASGI/WSGI.

10. FAQ & dépannage

---

Q : `python app/main.py` ne démarre pas, message d'erreur sur des imports.
A : Activez l'environnement virtuel et vérifiez que `requirements.txt` est installé avec l'exécutable Python que vous utilisez.

Q : Les linters signalent des fichiers dans `.venv`.
A : Assurez-vous que `.venv` est listé dans `.gitignore` et dans la configuration de `flake8`/`pyproject.toml`.

Q : CI échoue sur GitHub Actions mais passe localement.
A : Vérifiez les versions de Python utilisées par la matrice CI ; assurez-vous que les caches et installations de dépendances sont correctes.

11. Licence

---

Ce projet est distribué sous licence GPL-3.0. Voir le fichier `LICENSE` pour le texte complet.

12. Contact

---

Pour toute question ou signalement de bug, ouvrez une issue sur GitHub : https://github.com/Thurxm09/TODO-LIST-App_python/issues

Merci d'utiliser et de contribuer à ce projet — les retours sont les bienvenus !

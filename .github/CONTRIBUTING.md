# Guide de contribution

Merci pour votre intérêt à contribuer au projet TODO List.

Ce document décrit les règles et outils pour contribuer proprement (tests, style, PRs).

Branches

- `main` : branche de production (protected)
- `dev` : intégration et tests
- features : `feature/<sujet>`
- bugs : `fix/<sujet>`

Commits

- Utilisez Conventional Commits : `feat:`, `fix:`, `docs:`, `chore:` etc.
- Écrivez un message clair et descriptif.

Pré-requis locaux

- Python 3.10+ (recommandé)
- Créez un venv : `python -m venv .venv`
- Activez : Windows `.\.venv\\Scripts\\activate` | Unix `source .venv/bin/activate`
- Installez les dépendances : `pip install -r requirements.txt`

Style et qualité

- Formatage : `black .`
- Imports : `isort .`
- Lint : `flake8 .`

Tests

- Lancer : `pytest -q`
- Couverture attendue : tests pour la logique métier dans `app/` et stockage dans `data/`.

Pull Requests

- Ouvrez une PR depuis une branche feature vers `dev` ou `main` selon contexte.
- Remplissez le template de PR.
- Inclure tests et mises à jour de documentation si nécessaire.

Sécurité

- Ne pas committer de secrets. Utilisez GitHub Secrets pour CI.

Merci !

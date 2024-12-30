# Sliding Puzzle Solver

Ce projet implémente un solveur pour le puzzle sliding décrit dans le cours LINGI2261.

## Structure du projet

```
sliding-puzzle/
├── src/
│   ├── puzzle.py          # Classe principale PuzzleProblem
│   └── utils.py           # Fonctions utilitaires
├── tests/
│   └── test_puzzle.py     # Tests unitaires
├── data/
│   ├── init/             # États initiaux
│   └── goal/             # États objectifs
└── requirements.txt
```

## Installation

1. Cloner le repository
```bash
git clone [url-du-repo]
cd sliding-puzzle
```

2. Créer un environnement virtuel (optionnel mais recommandé)
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix
# ou
venv\Scripts\activate     # Sur Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation

Le programme peut être utilisé comme suit :

```python
from src.puzzle import PuzzleProblem
from src.utils import read_puzzle_file

# Charger les états initial et objectif
initial_state = read_puzzle_file('data/init/init1.txt')
goal_state = read_puzzle_file('data/goal/goal1.txt')

# Créer une instance du puzzle
puzzle = PuzzleProblem(initial_state, goal_state)

# Obtenir les successeurs d'un état
successors = puzzle.get_successors(initial_state)

# Vérifier si un état est l'état objectif
is_goal = puzzle.is_goal_state(some_state)
```

## Tests

Pour exécuter les tests unitaires :

```bash
python -m unittest discover tests
```

## Fonctionnalités

- Chargement des états depuis des fichiers
- Validation des mouvements
- Génération des états successeurs
- Vérification de l'état objectif
- Tests unitaires complets

## Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Créer une Pull Request

## Licence

Ce projet est sous licence MIT.
from src.puzzle import PuzzleProblem
from src.utils import read_puzzle_file

# Charger les états
initial = read_puzzle_file('data/init/init1.txt')
goal = read_puzzle_file('data/goal/goal1.txt')

# Créer le puzzle
puzzle = PuzzleProblem(initial, goal)

# Afficher l'état initial
print("État initial :")
puzzle.print_state(puzzle.initial_state)
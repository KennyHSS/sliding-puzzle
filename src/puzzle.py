'''NAMES OF THE AUTHOR(S):HOUESSOU Kenny'''
from .search import Problem

import sys

class PuzzleProblem(Problem):
    """Implémentation du Sliding Puzzle comme un problème de recherche."""
    
    def __init__(self, init_file, goal_file):
        """Initialize le problème avec les fichiers d'états initial et final."""
        self.initial = self.load_state(init_file)
        self.goal = self.load_state(goal_file)
        self.height = 5
        self.width = 4
        
    def load_state(self, filename):
        """Charge un état depuis un fichier."""
        with open(filename, 'r') as f:
            return [line.strip().split() for line in f]
            
    def get_piece_coordinates(self, state, piece):
        """Retourne les coordonnées d'une pièce donnée."""
        coords = []
        for i in range(self.height):
            for j in range(self.width):
                if state[i][j] == piece:
                    coords.append((i, j))
        return coords
        
    def is_valid_move(self, state, piece, direction):
        """Vérifie si un mouvement est valide."""
        coords = self.get_piece_coordinates(state, piece)
        di, dj = direction
        
        for i, j in coords:
            new_i, new_j = i + di, j + dj
            if not (0 <= new_i < self.height and 0 <= new_j < self.width):
                return False
            if state[new_i][new_j] != '0' and (new_i, new_j) not in coords:
                return False
        return True
        
    def move_piece(self, state, piece, direction):
        """Déplace une pièce dans une direction donnée."""
        if not self.is_valid_move(state, piece, direction):
            return None
            
        new_state = [row[:] for row in state]
        coords = self.get_piece_coordinates(state, piece)
        di, dj = direction
        
        for i, j in coords:
            new_state[i][j] = '0'
        
        for i, j in coords:
            new_state[i + di][j + dj] = piece
            
        return new_state
        
    def successor(self, state):
        """Génère les successeurs selon le format AIMA Python."""
        successors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # droite, gauche, bas, haut
        pieces = set()
        
        for row in state:
            for cell in row:
                if cell != '0':
                    pieces.add(cell)
                    
        for piece in pieces:
            for direction in directions:
                new_state = self.move_piece(state, piece, direction)
                if new_state:
                    move_name = f"Déplacer {piece} vers {['droite', 'gauche', 'bas', 'haut'][directions.index(direction)]}"
                    successors.append((move_name, new_state))
                    
        return successors
        
    def goal_test(self, state):
        """Vérifie si l'état actuel est l'état objectif."""
        for i in range(self.height):
            for j in range(self.width):
                if self.goal[i][j] == '1' and state[i][j] != '1':
                    return False
        return True
        
    def __str__(self):
        """Représentation string de l'état pour l'affichage."""
        return '\n'.join(' '.join(row) for row in self.initial)

def state_to_string(state):
    """Convertit un état en chaîne de caractères formatée."""
    return '\n'.join(' '.join(row) for row in state)

def main(argv):
    if len(argv) != 2:
        print("Usage: python puzzle.py <init_file> <goal_file>")
        sys.exit(1)
        
    problem = PuzzleProblem(argv[0], argv[1])
    
    # Utilisation de l'algorithme de recherche en largeur (BFS)
    node = breadth_first_graph_search(problem)
    
    if node is None:
        print("Pas de solution trouvée")
        return
        
    # Affichage de la solution selon le format requis
    path = node.path()
    path.reverse()
    
    # Afficher les états avec une ligne vide entre chaque état
    for i, n in enumerate(path):
        print(state_to_string(n.state))
        if i < len(path) - 1:  # Ne pas ajouter de ligne vide après le dernier état
            print()

if __name__ == "__main__":
    main(sys.argv[1:])
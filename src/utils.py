# src/utils.py
def read_puzzle_file(filepath):
    """Lit un fichier de puzzle et retourne la matrice correspondante"""
    try:
        with open(filepath, 'r') as f:
            return [line.strip().split() for line in f]
    except FileNotFoundError:
        raise Exception(f"Le fichier {filepath} n'a pas été trouvé")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture du fichier: {str(e)}")

def validate_puzzle_state(state):
    """Valide la structure d'un état de puzzle"""
    if not state:
        return False
    
    height = len(state)
    if height != 5:  # La hauteur doit être de 5
        return False
        
    width = len(state[0])
    if width != 4:  # La largeur doit être de 4
        return False
    
    # Vérifier que toutes les lignes ont la même largeur
    return all(len(row) == width for row in state)

def get_piece_size(piece_type):
    """Retourne la taille d'une pièce en fonction de son type"""
    if piece_type == '1':  # Pièce rouge
        return (2, 2)
    elif piece_type.isalpha():  # Pièce horizontale
        return (1, 2)
    elif piece_type.isdigit() and piece_type != '1':  # Pièce verticale
        return (2, 1)
    else:
        return (1, 1)  # Case vide ou autre
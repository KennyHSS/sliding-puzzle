# tests/test_puzzle.py
import unittest
from src.puzzle import PuzzleProblem
from src.utils import read_puzzle_file, validate_puzzle_state

class TestPuzzleProblem(unittest.TestCase):
    def setUp(self):
        self.initial_state = [
            ['2', '1', '1', '3'],
            ['2', '1', '1', '3'],
            ['0', 'A', 'A', '0'],
            ['4', '6', '7', '5'],
            ['4', '8', '9', '5']
        ]
        self.goal_state = [
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '1', '1', '.'],
            ['.', '1', '1', '.']
        ]
        self.puzzle = PuzzleProblem(self.initial_state, self.goal_state)

    def test_initialization(self):
        self.assertEqual(self.puzzle.height, 5)
        self.assertEqual(self.puzzle.width, 4)
        self.assertEqual(self.puzzle.initial_state, self.initial_state)
        self.assertEqual(self.puzzle.goal_state, self.goal_state)

    def test_get_piece_coordinates(self):
        coords = self.puzzle.get_piece_coordinates(self.initial_state, '1')
        expected = [(0, 1), (0, 2), (1, 1), (1, 2)]
        self.assertEqual(sorted(coords), sorted(expected))

    def test_is_valid_move(self):
        # Test mouvement invalide (hors limites)
        self.assertFalse(self.puzzle.is_valid_move(self.initial_state, '1', (-1, 0)))
        
        # Test mouvement valide
        self.assertTrue(self.puzzle.is_valid_move(self.initial_state, 'A', (0, -1)))

    def test_move_piece(self):
        # Test déplacement de la pièce 'A' vers la gauche
        new_state = self.puzzle.move_piece(self.initial_state, 'A', (0, -1))
        self.assertIsNotNone(new_state)
        self.assertEqual(new_state[2][0:2], ['A', 'A'])

    def test_is_goal_state(self):
        # Test état non final
        self.assertFalse(self.puzzle.is_goal_state(self.initial_state))
        
        # Test état final
        final_state = [
            ['2', '3', '4', '5'],
            ['2', '3', '4', '5'],
            ['A', 'B', 'C', 'D'],
            ['6', '1', '1', '7'],
            ['6', '1', '1', '7']
        ]
        self.assertTrue(self.puzzle.is_goal_state(final_state))

if __name__ == '__main__':
    unittest.main()
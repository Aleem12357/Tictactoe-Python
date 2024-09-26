# test_project.py

import pytest
from project import board, is_victory, player_move

@pytest.fixture(autouse=True)
def reset_board():
    """Reset the board before each test."""
    global board
    board[:] = [' ' for _ in range(9)]

def test_initial_board():
    assert board == [' ' for _ in range(9)]

def test_player_move():
    result = player_move('X', 1)  # Simulate player X making a move
    assert result is True  # Check if the move was successful
    assert board[0] == 'X'  # Check if X is in the right position
    
    result = player_move('O', 5)  # Simulate player O making a move
    assert result is True  # Check if the move was successful
    assert board[4] == 'O'  # Check if O is in the right position

def test_invalid_move():
    player_move('X', 1)  # X moves to position 1
    result = player_move('O', 1)  # O tries to move to the same position
    assert result is False  # Should return False on invalid move
    assert board[0] == 'X'  # X should still be in position 1

def test_victory_conditions(reset_board):    # Test horizontal victory
    board[0] = board[1] = board[2] = 'X'
    assert is_victory('X') is True

    # Reset and test vertical victory
    board[0] = board[3] = board[6] = 'O'
    assert is_victory('O') is True

    # Reset and test diagonal victory
    board[0] = board[4] = board[8] = 'X'
    assert is_victory('X') is True

def test_tie_condition():
    board[:] = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
    assert is_victory('X') is False
    assert is_victory('O') is False
    assert ' ' not in board  # Should be a tie

if __name__ == '__main__':
    pytest.main()
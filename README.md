# Tic Tac Toe Game

#### Video Demo: [https://youtu.be/kA4p8rfALxs?feature=shared]

#### Description:
The Tic Tac Toe game is a classic two-player game that allows players to compete against each other on a 3x3 grid. The game is designed to be simple yet engaging, making it suitable for users of all ages. This project implements the game in Python, utilizing a console-based interface for user interaction.

## Project Files

### 1. `tictactoe.py`
This is the main file that contains the game logic and user interface. The key components of this file include:

- **Game Board Representation**: The board is represented as a single list of 9 elements (initialized to spaces) to simulate the 3x3 grid.
- **Main Game Loop**: The `main()` function contains the core game loop, which continues until a player wins or there is a tie. It alternates turns between two players, 'X' and 'O'.
- **Move Functionality**: The `move(icon)` function prompts the current player for their move and validates the input. If the input is invalid, it requests the player to enter a valid move.
- **Victory Conditions**: The `is_victory(icon)` function checks if the current player has met any of the winning conditions after each move.
- **Print Board Function**: The `print_board()` function displays the current state of the board in a user-friendly format.

### 2. `test_project.py`
This file contains unit tests written using the pytest framework to ensure the game logic functions correctly. The tests cover various aspects of the game:

- **Fixture for Resetting the Board**: The `reset_board` fixture automatically resets the game board before each test to ensure a clean state.
- **Tests for Initial Conditions**: The `test_initial_board()` function checks that the board is empty at the start of the game.
- **Player Move Validation**: The `test_player_move()` function tests that players can successfully place their marks on the board.
- **Invalid Move Handling**: The `test_invalid_move()` function ensures that the game correctly handles attempts to place a mark in an already occupied spot.
- **Victory Conditions**: The `test_victory_conditions()` function tests both horizontal, vertical, and diagonal winning scenarios.
- **Tie Condition**: The `test_tie_condition()` function checks that the game recognizes a tie when the board is full without any winners.

## Design Choices
The decision to use a list for the board representation allows for easy indexing and manipulation of the game state. Each player's input is validated to ensure a smooth user experience, and the game logic is structured to provide clear feedback for valid and invalid moves.

The use of pytest for testing ensures that the game functions correctly and maintains reliability as new features are added or changes are made. The automated tests provide confidence in the code's behavior, making it easier to catch bugs early in the development process.

Overall, this Tic Tac Toe project showcases fundamental programming concepts such as loops, conditionals, and functions, while also emphasizing the importance of testing in software development. The project is designed to be easily extendable, allowing for potential features such as an AI opponent or a graphical user interface in the future.

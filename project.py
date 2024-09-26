# tictactoe.py

board = [' ' for _ in range(9)]  # We will use a single list to represent the 3x3 board

def main():
    while True:
        print_board()
        if not move('X'):
            continue  # If move is invalid, prompt again
        if is_victory('X'):
            print_board()
            print("Player 1 wins! Congratulations!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break
        
        print_board()
        if not move('O'):
            continue  # If move is invalid, prompt again
        if is_victory('O'):
            print_board()
            print("Player 2 wins! Congratulations!")
            break

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    
    print("_____________")
    print(row1)
    print("|___________|")
    print(row2)
    print("|___________|")
    print(row3)
    print("|___________|")

def move(icon):
    number = 1 if icon == 'X' else 2
    print("Your turn player {}".format(number))
    try:
        choice = int(input("Enter your move (1-9): ").strip())
        return player_move(icon, choice)
    except (ValueError, IndexError):
        print("Invalid input! Please enter a number between 1 and 9.")
        return False  # Return False if the move is invalid

def player_move(icon, choice):
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
        return True  # Successful move
    else:
        return False  # Move failed

def is_victory(icon):
    winning_conditions = [
        (board[0], board[1], board[2]),
        (board[3], board[4], board[5]),
        (board[6], board[7], board[8]),
        (board[0], board[3], board[6]),
        (board[1], board[4], board[7]),
        (board[2], board[5], board[8]),
        (board[0], board[4], board[8]),
        (board[2], board[4], board[6])
    ]
    return any(all(cell == icon for cell in condition) for condition in winning_conditions)

if __name__ == "__main__":
    main()
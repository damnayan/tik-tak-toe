# tik-tak-toe
This repository contains a simple yet engaging Tic-Tac-Toe game implemented in Python, playable in the command line interface (CLI). The game features a basic AI opponent that makes moves randomly.

Interactive Gameplay: Players can interact with the game using the console, entering numbers to place their "X" on a 3x3 grid.
Simple AI Opponent: The game includes a basic AI that randomly selects spots on the board to place its "O", providing a fun challenge for the player.
Game State Management: The implementation includes checks for game-winning conditions, a tie condition, and alternates turns between the human player and the computer.
Console Output: The board is printed out in the console window after each move, allowing players to see the current state of the game dynamically.
How It Works
The game runs in a loop until a win or a tie occurs. It starts with an empty board and alternates turns between the player and the computer. The player inputs their move by entering a number that corresponds to the position on the board they wish to take, with checks to prevent invalid inputs or moves. The computer (AI) makes moves randomly. After each move, the game checks for a winner or if all spots are filled, resulting in a tie. The gameplay continues until one of these conditions is met.

Technologies Used
Python: The entire game is written in Python, utilizing basic control structures like loops, conditionals, and functions to handle the game's logic and flow.
Getting Started
To play the game, clone this repository and run the Python script in your terminal or command prompt:

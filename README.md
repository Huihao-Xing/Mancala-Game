# Mancala-Game
implementation of the game Mancala

In this project, you will implement the game Mancala through Python. To familiarize yourself with the game you can
play Mancala online at https://www.mathplayground.com/mancala.html. Note that the board size and the number of gems at each position may be different for you than in the online version. There
are many rule variants for Mancala, but you will use the rules below in this project.

-------------------------------------------------------------------------------------------------------------------------
The Mancala Board
Mancala is played with a board that contains several positions, as shown in the figure below. Each position
can contain zero or more gems. There are two players: player 0, and player 1.
• The large positions on left and right are called mancalas.
• The small positions on top and bottom are called pits.
• The pits on bottom and mancala on right belong to player 0.
• The pits on top and mancala on left belong to player 1.
• The positions are numbered 0 through 11 as shown in the figure, starting from the lower-left pit and
increasing counter-clockwise around the board.
• A pair of adjacent pits on top and bottom are called opposite from each other. For example, the
opposite pit from position 1 is position 9, and vice versa.
• At the beginning of the game, 2 gems are placed in each pit, and 0 gems in each mancala.

In your implementation, the board is represented using the Python list data-type. The list contains the
number of gems at each position, from 0 to 11. For example, if board[1]==2, that means that 2 gems are
at position 1. The players are represented using the Python int data-type: 0 for player 0, and 1 for player 1.

![image](https://github.com/Huihao-Xing/Mancala-Game/assets/119607601/91154f16-43e6-45b9-8b37-e929a2eefea4)

-------------------------------------------------------------------------------------------------------------------------
The Rules of Mancala
This assignment uses the same game rules as the online version linked above, except for the size of the board
and initial number of gems at each position. Those rules are as follows:
• The objective of the game is to maximize the number of gems in your mancala at the end of the game.
• On your turn, you choose one of your non-empty pits (on your side of the board) and pick up all gems
from that pit. Then you move your hand counter-clockwise around the board, dropping one gem in
each subsequent position, until your hand is empty. The one exception is that you skip your opponent’s
mancala instead of dropping a gem in it. You start dropping gems at the position immediately
following the pit that you picked up. For example, if you pick up from position 1, you drop your first
gem at position 2. If you get to position 11 and your hand is not empty, you wrap around to position
0 and continue.
• If the last gem in your hand is dropped in your own mancala, your opponent’s next turn is skipped
and you go again.
• If the last gem in your hand is dropped in an empty pit on your own side, and your opponent has at
least one gem in the opposite pit, then you move all gems from both pits to your own mancala.
• The game ends when either your pits are all empty, or your opponent’s pits are all empty. If yours
are empty first, then the opponent gets to move all remaining gems in their pits to their mancala.
Likewise, if your opponent’s pits are empty first, then you get to move all remaining gems in your pits
to your mancala. This is called clearing pits.
• The player who has more gems in their mancala after clearing pits is the winner.

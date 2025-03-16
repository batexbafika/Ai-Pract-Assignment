This is the Data structure for our first practical assignment in AI. In the Game.py file, the following has been done.

class Node:
In this node, we have created the template for all our game nodes for both the root node and also the child nodes. 

class Game_state:
This is for the Game state class which will show all the parameters characterising the game state
and the players turn.

class GameTree:
The gameTree which is actually root nodes and child nodes where every node has the game state at a given moment in the game course.

class player:
This step will now create the player class which will track every player 
be it the computer or the human player. itb will also have a boolean data
member which will tell us if the current player is a human or not and current score for the player.

class Moves: 
We now try to define moves according to our game rules, what player moves are valide and which player moves are invalid.

Main function:
Here we tested the game tree with a divition by either 2 or 3 to see if all our classes are well defined and also if the 
game tree is successfully generated as expected.

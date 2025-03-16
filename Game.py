from ast import main
from asyncio import current_task
import random
import time
import sys

#This is class for the game nodes which represents the state of the game at any given time
#This Node is a template for all the nodes in the game tree and it will store all the data
#required for for each game state. It will also store the parent node and the children nodes
#together with weights for each node. useful for the hueristic function.

class Node:     # Node class for the linked list
    def __init__(self, Game_state, parent=None):
        self.Game_state = Game_state
        self.parent = parent
        self.children = [] # List of children nodes
        self.value = [] # List of weights for each child node


#This will be for the Game state class which will show all the parameters characterising the game state
#and the players turn.

class Game_state:
    def __init__(self, initial_number, player_score=0, computer_score=0, bank_score=0, is_player_turn = True):
        self.initial_number = initial_number
        self.player_score = player_score
        self.computer_score = computer_score
        self.bank_score = bank_score
        self.is_player_turn = is_player_turn
       

#Now we will create the gameTree which actually root nodes and child nodes 
#where every node has the game state at a given moment in the game course.

class GameTree:
    def __init__(self, root: Node ):
        self.root = root

    #This function will generate the children nodes for a given node
    def Add_child(self, parent:Node, child: Game_state ):
        child_Node = Node(child, parent)
        parent.children.append(child)
        return child_Node
    
    #This step will now create the player class which will track every player 
    #be it the computer or the human player. itb will also have a boolean data
    #member which will tell us if the current player is a human or not and current score for the player.

class Player:
    def __init__(self, name, is_human = True):
        self.name = name
        self.is_human = is_human
        self.score = 0


#We now try to define according to our game rules, what player moves are valide and which player moves are invalid.

class Moves:
    def __init__(self, divisor):
        self.divisor = divisor # The divisor for the game can either be 2 or 3

        #this function check for validity of the operation.
    def is_valid(self, initial_number):
        return initial_number % self.divisor == 0
           
    def apply_move(self, current_state: Game_state):
        if not self.is_valid(current_state.initial_number):
            return None # If the move is invalid, return None
        new_number = current_state.initial_number // self.divisor
        return Game_state(
            initial_number=new_number,
            player_score=current_state.player_score,
            computer_score=current_state.computer_score,
            bank_score=current_state.bank_score,
            is_player_turn=not current_state.is_player_turn
        )
    

def main():
    print("Game script is running...")

    # Step 1: Initialize the root state
    initial_state = Game_state(initial_number=13000)
    print(f"Initial state created with number: {initial_state.initial_number}")

    # Step 2: Create a game tree
    root_node = Node(Game_state=initial_state)
    game_tree = GameTree(root=root_node)
    print("Game tree created successfully.")

    # Step 3: Apply a move (divide by 2)
    move = Moves(3)
    new_state = move.apply_move(initial_state)
    if new_state:
        print(f"Move applied successfully. New number: {new_state.initial_number}")
        game_tree.Add_child(root_node, new_state)
        print(f"Child node added. Total children of root: {len(root_node.children)}")
    else:
        print("Move was invalid.")

    print("Game script completed execution.")

if __name__ == "__main__":
    main()



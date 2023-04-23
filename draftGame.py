import random

# Define the maze as a 2D array
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

# Define the starting position of the player
player_pos = [1, 1]

# Define the hints and clues
hints = [
    "Look for a hidden door in the maze walls",
    "The way forward is not always obvious",
    "Listen carefully for clues",
    "Check the walls for hidden markings",
    "The answer lies in the stars",
]

clues = [
    "The first clue is hidden in the room with a statue",
    "To find the key, you must first solve the riddle",
    "The map is useless without the compass",
    "The combination to the safe is hidden in the painting",
    "To unlock the door, you must find the hidden lever",
]

# Define a function to print the maze and player position
def print_maze():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if player_pos == [i, j]:
                print('P', end=' ')
            else:
                print(maze[i][j], end=' ')
        print()

# Define a function to check if the player has reached the end
def is_game_over():
    return player_pos == [5, 8]

# Define the main game loop
def game_loop():
    print_maze()
    while not is_game_over():
        # Get player input
        move = input("Enter your move (up, down, left, right): ")

        # Move the player
        if move == "up" and maze[player_pos[0]-1][player_pos[1]] != "#":
            player_pos[0] -= 1
        elif move == "down" and maze[player_pos[0]+1][player_pos[1]] != "#":
            player_pos[0] += 1
        elif move == "left" and maze[player_pos[0]][player_pos[1]-1] != "#":
            player_pos[1] -= 1
        elif move == "right" and maze[player_pos[0]][player_pos[1]+1] != "#":
            player_pos[1] += 1
        else:
            print("Invalid move, try again.")
            continue

        # Give a random hint or clue
        if random.randint(0, 1):
            print("Hint:", random.choice(hints))
        else:
            print("Clue:", random.choice(clues))

        # Print the updated maze and player position
        print_maze()

    # Print the game over message
    print("Congratulations, you have reached the end of the maze!")

# Start the game
game_loop()
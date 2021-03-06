# Add triple/double score functionality
# Add ability to score multiple words in one play
# Make max rounds == tile quantity/number of players
# Add ability to manually end game
import sys

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", ""]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = {letter: point for letter, point in zip(letters, points)}
player_to_words = {}
player_to_points = {}
play_list = []


def score_word(word):
    new_word = word.upper()
    point_total = 0
    for letter in new_word:
        if letter in letter_to_points:
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total


def game_start(start):
    magic_word = start
    if magic_word == "start":
        print("Enter the number of players.")
        try:
            player_count = int(input())
        except ValueError:
            print("You need to enter a number, not a word.")
            game_start("start")
        for i in range(player_count):
            print("Player " + str(i + 1) +
                  ", please enter your name. No dirty words, you foul thing.")
            name = input()
            print("Thanks, " + name + "!")
            print()
            play_list.append(name)
        for player in play_list:
            player_to_words[player] = []
        wordplay(1)
        return player_to_points
    else:
        print("Ahhh, you didn't say the magic word!\nIt's start, by the way.\nThe magic word is: start.")
        game_start(input())


def point_calculator(plays):
    for player, words in plays.items():
        player_points = 0
        for word in words:
            word_score = score_word(word)
            player_points += word_score
            player_to_points[player] = player_points
        print(player + " has " + str(player_points) + " points.")
    return player_to_points


def play_word(player, word):
    played_word = word
    if played_word == "I want to get off this ride.":
        print("Are you sure?")
        sure = input()
        if sure == "yes":
            plays = player_to_words
            point_calculator(plays)
            sys.exit()
    else:
        pass
    word_list = player_to_words[player]
    word_list.append(word)
    print("The word \"" + word + "\" has been played by " + player + ".")
    print()
    return player_to_words


def wordplay(round):
    game_length = range(100 // len(play_list))
    for round in game_length:
        print("Round " + str(round) +
              ": FIGHT! \nWith your words, please. We're not savages.")
        for name in play_list:
            player = name
            print(
                player + " please enter a word.\nType \"I want to get off this ride.\" to finish the game.")
            word = input()
            play_word(player, word)
        plays = player_to_words
        point_calculator(plays)
        print()
    return


print("IT BEGINS!!!!!!!")
game_start("start")

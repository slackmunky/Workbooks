player_to_words = {"cody": [], "mic": [], "connor": [], "emma": []}

def play_word(player, word):
    word_list = player_to_words[player]
    word_list.append(word)
    print("The word \"" + word + "\" has been played by " + player + ".")
    return player_to_words

play_word("cody", "strange")

print(player_to_words)

play_word("cody", "obvious")

print(player_to_words)
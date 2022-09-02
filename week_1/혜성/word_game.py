# C. Word Game

import sys

class Player:
    words: list()
    score: int = 0

    def __init__(self, words: list()):
        self.words = words

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    distinct_words = dict()
    score = list()
    players = list()
    for _ in range(3):
        player = Player(words=sys.stdin.readline().split("\n")[0].split(" "))
        for word in player.words:
            distinct_words[word] = distinct_words.get(word, 0) + 1
        players.append(player)
    for player in players:
        for word in player.words:
            if distinct_words.get(word, 0) == 1:
                player.score += 3
            elif distinct_words.get(word, 0) == 2:
                player.score += 1
        print(player.score, end=" ")
    print("")

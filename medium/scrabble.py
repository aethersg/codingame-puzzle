import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

DICT_WORDS = []
WORD_POSSIBLE = []
WORD_POINTS = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
    "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
    "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
    "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
    "y": 4, "z": 10
}

n = int(raw_input())
for i in xrange(n):
    w = raw_input()
    DICT_WORDS.append(w)
letters = raw_input()


def scrabble_points(word):
    total = 0
    for w in word:
        total = total + WORD_POINTS[w.lower()]
    return total


def check_word_possible(word_array, letter_array):
    for word in word_array:
        temp_letter_array = list(letter_array)
        temp_word = ""
        # filter out words which is bigger then letter combination
        if len(word) <= len(temp_letter_array):
            for w in word:
                if w in temp_letter_array:
                    temp_letter_array.remove(w)
                    temp_word += w
            if temp_word == word:
                WORD_POSSIBLE.append(word)


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
check_word_possible(DICT_WORDS, letters)

return_word = ""
max_point = 0

for wp in WORD_POSSIBLE:
    score = scrabble_points(wp)
    if score > max_point:
        max_point = score
        return_word = wp

print return_word

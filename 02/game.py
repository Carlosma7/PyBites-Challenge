#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
	return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
	word = input(f'Your current letters are {draw}. \nPlease choose your word: ').upper()
	return _validation(word, draw)

def _validation(word, draw):
	if word in get_possible_dict_words(list(draw)):
		return word
	else:
		raise ValueError

def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def get_possible_dict_words(draw):
	permutations = _get_permutations_draw(draw)
	words = [word for word in permutations if word.lower() in DICTIONARY]
	return words

def _get_permutations_draw(draw):
	permutations = [list(itertools.permutations(draw, n)) for n in range(1, NUM_LETTERS + 1)]
	return ["".join(word) for words in permutations for word in words]

def max_word_value(words):
	return max(words, key=calc_word_value)

def main():
	"""Main game interface calling the previously defined methods"""
	draw = draw_letters()
	print('Letters drawn: {}'.format(', '.join(draw)))

	word = input_word(draw)
	word_score = calc_word_value(word)
	print('Word chosen: {} (value: {})'.format(word, word_score))

	possible_words = get_possible_dict_words(draw)

	max_word = max_word_value(possible_words)
	max_word_score = calc_word_value(max_word)
	print('Optimal word possible: {} (value: {})'.format(
		max_word, max_word_score))

	game_score = word_score / max_word_score * 100
	print('You scored: {:.1f}'.format(game_score))

if __name__ == "__main__":
    main()

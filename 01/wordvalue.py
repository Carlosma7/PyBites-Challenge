from data import DICTIONARY, LETTER_SCORES
import numpy as np

def load_words():
	# Read file
	with open(DICTIONARY) as f:
		# Read line by line and store it in a list
		content = f.readlines()
		content = [x.strip() for x in content]
	return content

def calc_word_value(word):
	# Get scores for each character from the word
	word = word.upper()
	values = [LETTER_SCORES.get(char) for char in word]
	values = [i for i in values if i] 
	# Sum up al letter scores
	score = sum(values)
	return score

def max_word_value(words=load_words()):
	# Check if list of words is empty and use default
	if words == None:
		words = load_words(DICTIONARY)
	# Calculate scores for each word
	scores = [calc_word_value(word) for word in words]
	# Get index of maximum
	index = np.argmax(scores)
	# Return max
	return words[index]

if __name__ == "__main__":
	# Read dictionary
	words_list = load_words()
	# Calculate value of words in dictionary
	max_word, max_score = max_word_value(words_list)
	# Print results
	print(max_word)
	print(max_score)

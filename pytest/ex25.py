def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
#what stuff has function split ; i guess change words
#not change word change sentence, put word in stack separate words with ' '

def sort_word(words):
	"""Sorts the words."""
	return sorted(words)
#what is sorted?  means find the two kind of char,' ' and word, in the sentence
#only one stack? puzzle

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print (word)
#word is a stack pop for the first one!

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print (word)
#smart way use -1 ,I want to caculate the length of the words, then use len-1

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_word(words)
#break_words in there
#then find the sortest word!

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
#no main()?

import random
#from urllib import urlopen
import sys

r'''
there are 3 package import
1\random for what?
2\url lib  for URL
3\sys   we used exits
'''
#WORD_URL = "http://learncodethehardway.org/words.txt"
WORD_URL = "words.txt"
#initialize url
currentfile = open(WORD_URL)
WORDS = []
# a empty list
resu = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

#what is that phrases? a piece of words?

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
#for word in urlopen(WORD_URL).readlines():
for word in currentfile.readlines():
    WORDS.append(word.strip())
print (WORDS)
currentfile.close()

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    print ("count@@@:",snippet.count("@@@"))
    print ("count%%%:",snippet.count("%%%"))
    print ("count***:",snippet.count("***"))
    print ("class_names:",class_names)
    print ("other_names:",other_names)
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    print ("param_names:",param_names)

    for sentence in snippet, phrase:
        result = sentence[:]
#result [snippet:pharas]?
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        print("result class:",result)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        print("result other:",result)
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        print("result para:",result)
        results.append(result)

        print("result end:",result)
    return results


# keep going until they hit CTRL-D
try:
	while True:
		snippets  = PHRASES.keys()
		print("snippets:",snippets)
		random.shuffle(list(snippets))

		for snippet in snippets:
			phrase = PHRASES[snippet]
#			print( "convert returen is:",convert(snippet, phrase),"\n\n")
# ['class Cough(object):\n\tdef __init__(self, airport)', 'class Cough has-a __init__ that takes self and airport parameters.']	
			question, answer = convert(snippet, phrase)
		#	resu = convert(snippet,phrase)
		#	question = resu[0]
		#	answer = resu[1]
		#	print( "question is %s\nanswer is %s:"%(question,answer))
			if PHRASE_FIRST:
		#		question= resu[1] 
		#		answer = resu[0] 
				question,answer = answer,question
			print (question)
			i=input('>')
			print ("ANSWER:  %s \n\n" % answer)
except EOFError:
	print ("\nBye")

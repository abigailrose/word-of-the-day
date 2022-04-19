import random
import sys
import os
from PyDictionary import PyDictionary

dictionary=PyDictionary()

words = open("words.txt", 'r')

word_list = words.readlines()
index = random.randint(0, len(word_list))

print("\nThe word of the day is: {}".format(word_list[index]))
#print(dictionary.meaning(word_list[index]))

old_stdout = sys.stdout # backup current stdout
sys.stdout = open(os.devnull, "w")

definitions = dictionary.meaning(word_list[index])

sys.stdout = old_stdout # reset old stdout

count = 1
if bool(definitions):
	for definition in definitions:
		for i, repeat in enumerate(definitions[definition]):
			if definitions[definition][i][0] == '(':
				continue
			print("{}. ({}) Definition: {}\n".format(count, definition, definitions[definition][i]))
			count += 1
else:
	print("Definition not found, try https://www.merriam-webster.com/dictionary/{}".format(word_list[index]))


# Resources:
# https://stackoverflow.com/questions/8447185/to-prevent-a-function-from-printing-in-the-batch-console-in-python
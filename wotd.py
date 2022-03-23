import random

words = open("words.txt", 'r')

word_list = words.readlines()
index = random.randint(0, len(word_list))

print("The word of the day is: {}".format(word_list[index]))
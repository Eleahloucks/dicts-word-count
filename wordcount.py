"""Count words in file."""
import sys

def word_counter(filename):
  # open the text file
  poem = open(sys.argv[2])
  #create empty dict
  count_words = {}
  # iterate over lines and split by word
  for line in poem:
    #word = line.split('').rstrip('')
    words = line.rstrip().split()
    #iterate through each word in file
    for word in words:
        #set the each word as a key
        #search for each word
        count_words[word] = count_words.get(word, 0) + 1

  for key, value in count_words.items():
    print(key, value)









def print_upper_words(words, must_start_with={}):
  """ Takes a list of words
  checks if the first letter of the word is in the set the user provides
  if it does, make the whole word uppercase
  """
  for word in words:
    if word[0] in must_start_with:
      print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"y"})

print_upper_words(["picture", "hey", "song", "yo", "yes", "album", "year"],
                   must_start_with={"y", "h"})
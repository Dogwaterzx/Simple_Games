# Helper functions 

# updatedashes() fn fills in dashes with the correctly guessed letter  
# Parameters: secret - string (secret word)
#             dashes - string (current dashes)
#             letter - string (guess letter inputted by user)
# Returns updated dashes string 

def updatedashes(secret, dashes, letter): 
  dashes = list(dashes)          # change string to list of characters
  for i in range(len(secret)):   # repeat for each letter in secret word 
    if secret[i] == letter:      # if there is a match    
      dashes[i] = letter        # update same index of dashes
  dashes = "".join(dashes)   # change list back to string
  return dashes



# Lists of words that can be used for Hangman game.

nouns = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]

animals = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

advanced_words = ['awkward', 'bagpipes', 'banjo', 'bungler', 'croquet', 'crypt', 'dwarves', 'fervid', 'fishhook', 'fjord', 'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'ivory', 'jazzy', 'jiffy', 'jinx', 'jukebox', 'kayak', 'kiosk', 'klutz', 'memento', 'mystify', 'numbskull', 'ostracize', 'oxygen', 'pajama', 'phlegm', 'pixel', 'polka', 'quad', 'quip', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'swivel', 'toady', 'twelfth', 'unzip', 'waxy', 'wildebeest', 'yacht', 'zealous', 'zigzag', 'zippy', 'zombie']

games = ['minecraft', 'roblox', 'xbox', 'playstation', 'nintendo']

coding_languages = ['java', 'javascript', 'python', 'css', 'html']

from helper import get_keys

fn = 'twinkle'

with open(fn + '.txt', 'r') as file:
    temp = file.read()

keys = get_keys(temp)
# print(keys)

choices = {}


for key in keys:
    value = input("Give me a {}: ".format(key))
    choices[key] = value
    
print(choices)

story = temp.format(**choices)

with open(fn + '_out.txt', 'w') as f:
    f.write(story)

print(story)

# temp = 'I went to {subject} class today and saw {name}.  {name} loves {subject}'
# subj = input('Subject: ')
# nm = input('Name: ')

# choices = {'subject' : subj, 'name' : nm}

# story = temp.format(**choices)
# print(story)

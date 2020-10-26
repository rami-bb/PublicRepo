
def word_count(my_string):
    previous_space = True
    words = 1
    try:
        for i in my_string:
            if i == " ":
                if previous_space == False:
                    previous_space = True
                    words += 1
            elif not (i == " "):
                previous_space = False
        return words
    except:
        return "Not a string"

def word_length(my_string):
    previous_space = False
    char = 0
    if len(my_string) > 0:
        for i in my_string:
            if i == " ":
                if previous_space == False:
                    previous_space = True
                    char += 0
            elif i in ",.?/!@#$%^&*()-_=+{[}]": 
              #So function doesn't count special characters
              char += 0
            elif not (i == " "):
                previous_space = False
                char += 1
        if char == 0:
            return "No words"
    return char



def average_word_length(my_string):
  if word_count(my_string) == "Not a string":
    return "Not a string"
  elif word_length(my_string) == "No words":
    return "No words"
  else:
    avg = word_length(my_string) / word_count(my_string)
    return avg



print(average_word_length("Hello, hey, testing only"))
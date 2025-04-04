import __main__
def getspan(s, r):
    count = 0
    spans = []
    start = 0
    while True:
        start = s.find(r, start)
        if start == -1:
            break
        end = start + len(r)
        spans.append((start, end))
        count += 1
        start += 1
    return count, spans

def reverse_words(sent):
    words = sent.split()
    list_of_strings = list(words)
    print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence

def removePunctuation(sent):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    translator = str.maketrans('', '', punctuation_chars)
    return sent.translate(translator)

def countWords(s):
    words = s.split()
    list_of_words = list(words)
    print(list_of_words)
    wordcount = len(list_of_words)
    return wordcount
def characterMap(s):
    return {char: s.count(char) for char in set(s)}

def makeTitle(str1):
     if(str1.istitle()):
        print("The given string is already a Title")
        return str1
     word_list = str1.split()
     new_word = [word.capitalize() for word in word_list]
     capitalised_string = ' '.join(new_word)
     return capitalised_string
def normalizeSpaces(input):
    new_list = []
    space = False
    for item in input:
        if(item != ' '):
            new_list.append(item)
            space = False
        elif not space:
            new_list.append(' ')
            space = True
    converted_sentence = ''.join(new_list)
    return converted_sentence

def transform(string):
    list_of_strings = list(string)
    print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = "".join(reversed_list)
    new_sentence = reversed_sentence.swapcase()
    return new_sentence

def get_permutations(user_input, step=0):
    if step == len(user_input):
        print("".join(user_input))  # Print each permutation
        return
 
    for i in range(step, len(user_input)):
        s_list = list(user_input)
        s_list[step], s_list[i] = s_list[i], s_list[step]  # Swap characters
        get_permutations(s_list, step + 1)
         


if __name__=="__main__":
    s= str(input("Enter a word :"))
    r=str(input("Enter a Substring :"))
    sent=str(input("Enter a sentence :"))
    input=str(input("Enter a sentence with spaces: "))
    str1="This is my codes"
    string="I have 7 apples, 2 pineapples and 9 oranges"
    count, spans = getspan(s, r)

    print(f"({count},{spans})")
    print("Reversed sentence: ", reverse_words(sent))
    print("Removes punctuation characters:",removePunctuation(sent))
    print("Word count = ",countWords(s))
    print("Character map:",characterMap(s))
    print("Title changed: ",makeTitle(str1))
    print("Converted sentence:", normalizeSpaces(input))
    print("Translated/transformed sentence is:- ",transform(string))
    get_permutations("abc",0)

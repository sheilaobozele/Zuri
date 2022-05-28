# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}


with open('/Users/user/Desktop/Reading-Text-Files/story.txt') as file:
    print(file.readlines())

    file = open('/Users/user/Desktop/Reading-Text-Files/story.txt', "rt")
    data = file.read()
    words = data.split()

    print('Number of words in text file :', len(words))
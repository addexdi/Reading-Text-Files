# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    text = open("story.txt", "r")
    file = text.read()

    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.strip("/n, .r")
    words = file
    text.close()
    return words #"Hello World"
print(read_file_content("./story.txt"))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    spliced = text.split()
    d = {}
    for word in spliced:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])
    return  d #{"as": 10, "would": 20}
print(count_words())

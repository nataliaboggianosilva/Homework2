from urllib.request import urlopen

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
local_name = "PRIDEANDPREJUDICE.txt"

def save_locally():

    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words
#Defining the number of total of unique words

save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break

retList = []
for x in unique_words:
    if len(x) >= 7:
        retList.append(x)
print("The number of words over 7 characters is",retList)
print('Number of words in text file :', len(unique_words))

total_words = 0
with open(local_name) as fp:
    for line in fp:
        words = line.split()
        total_words += len(words)
print("The number of words is", total_words)

ratio=len(unique_words)/total_words
print("The ratio of unique words per total words is", ratio)

from urllib.request import urlopen

url = "https://www.gutenberg.org/files/161/161-0.txt"
local_name = "SENSEANDSENSIBILITY.txt"

def save_locally():

    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words
#Defining the number of total of unique words

save_locally()
unique_words1 = get_unique_words()
most_frequent1 = list(unique_words1.values())
most_frequent1.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent1[:10]:
    for unique_word, value in unique_words1.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break

retList = []
for x in unique_words1:
    if len(x) >= 7:
        retList.append(x)
print("The number of words over 7 characters is",retList)
print('Number of words in text file :', len(unique_words1))

total_words1 = 0
with open(local_name) as fp:
    for line in fp:
        words1 = line.split()
        total_words1 += len(words1)
print("The number of words is", total_words1)

ratio1=len(unique_words1)/total_words1
print("The ratio of unique words per total words is", ratio1)

if ratio > ratio1:
    print("Pride and Prejudice has a wider vocabulary of words")
elif ratio < ratio1:
    print("Sense and Sensibility has a wider vocabulary of words")
else:
    print("Both books have the same variety of words")




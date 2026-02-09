# Word Frequency

# Input a sentence and count frequency of each word.

s = list(input("Enter a sentence:").split())

words = {}
for wrd in s:
    words[wrd] = words.get(wrd,0)+1    # the count increases everytime same word is repeated

print(words) 

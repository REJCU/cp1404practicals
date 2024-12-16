"""
Word Occurrences
Estimate: 35 minutes
Actual:   26 minutes
"""

collection_of_words = {}

sentence_of_words = input("Text: ")
words = sentence_of_words.split()

for word in words:
    frequency_of_words = collection_of_words.get(word, 0)
    collection_of_words[word] = frequency_of_words + 1

words = list(collection_of_words.keys())
words.sort()
length = max((len(word) for word in words))
for word in words:
    print(f"{word:{length}} = {collection_of_words[word]}")

# COLOUR = {"absolute zero": "#0048ba", "cerulean": "#007ba7", "egyptian blue": "#1034a6", "electric blue": "#7df9ff"
#     , "ultramarine": "#3f00ff", "lightslateblue":"#8470ff", "lilac":"#c8a2c8", "little boy blue":"#6ca0dc", "macaroni and cheese":"#ffbd88", "sapphire":"#0f52ba"}
#
# name_of_colour = input("Name: ").lower()
# while name_of_colour != "":
#     if name_of_colour in HEX_COLOUR:
#         print(name_of_colour, "is", HEX_COLOUR[name_of_colour])
#         name_of_colour = input("Name: ")
#     else:
#         print("Invalid Name")
#         name_of_colour = input("Name
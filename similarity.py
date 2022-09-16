# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Defining the documents
doc1 = "Soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "I support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document matrix
# [soccer, my, favorite, sport, I, like, one, support, olympic, game]

def word_count(words, doc):
    result = []
    doc_list = list(map(str.lower, doc.replace(',' , ' ').split(' ')))

    for i in words:
        count = doc_list.count(i.lower())
        counts = doc_list.count(i +'s'.lower())
        result.append(count + counts)
    return np.array([result])
	

words = ['soccer', 'my', 'favorite', 'sport', 'I', 
         'like', 'one', 'support', 'olympic', 'game']

	

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
word_count_list = [word_count(words, doc1), 
                   word_count(words, doc2),
                   word_count(words, doc3),
                   word_count(words, doc4)]

max_num = 0
x = 0
y = 0
for i, w1 in enumerate(word_count_list):
    for j, w2 in enumerate(word_count_list):
        ans = cosine_similarity(w1,w2)
        if i != j and ans[0] > max_num:
            max_num = ans[0]
            x = i
            y = j
        else:
            continue
        

# Print the highest cosine similarity following the template below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
print(f'The most similar documents are: doc{x+1} and doc{y+1} with cosine similarity = {max_num}')

# poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

with open('FileObjects/Exercise/poem.txt','r') as f:
    poem = f.read()
    print(poem)
    
# Counting Words / Characters
word_count = len(poem.split())
print(word_count)   

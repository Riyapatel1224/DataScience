# poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

# This dictionary will store words as keys and their occurrence count as values.
words={}

# Open the file 'poem.txt' read mode. The 'with' statement is used for exception handling and ensures that the file is closed after use.
with open('Exercise/poem.txt','r') as f:
   
   # Loop through each line in the file.
   for  line in f:
       
       # Split the line into individual words and store them in a list.
       wordss=line.split()
       
       # Loop through each word in the list.
       for word in wordss:
           
           # If the word is already in the dictionary, increment its count by 1.
           if word in words:
               words[word]+=1
           # If the word is not in the dictionary, add it with a count of 1.
           else:
               words[word]=1

# Find the maximum occurrence value in the dictionary.
max_occurenceWord = max(list(words.values()))

# Print the maximum occurring word(s).
print("max occurening word is ",max_occurenceWord)

for item,value in words.items():
   # If the word count matches the maximum count, print the word.
   if  value==max_occurenceWord :
       print(item+" occurs most")

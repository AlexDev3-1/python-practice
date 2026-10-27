with open("Story.text", "r") as f :
    story = f.read()
  
words = set()
start_of_word = -1

tartget_start = "<" 
tartget_end = ">"

 
for i, char in enumerate(story):
    if char == tartget_start:
        start_of_word = i
    
    if char == tartget_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
        
answers = {}
    
for word in words :
    answer = input("enter word for  " + word + ":" )
    answers[word] = answer

for word in words :
    story = story.replace(word, answers[word])
    
print(story)   
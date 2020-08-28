def count(word, specific_letter):
    count = 0
    for letter in word:
        if letter == str(specific_letter):
            count = count + 1
            
    print(count)
    
    
    
word = 'banana'
count(word, 'a')
def disemvowel(string):
    splitString = list(string)
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    
    for letter in splitString:
       for vowel in vowels: 
           if vowel == letter:
               splitString.remove(letter)
    return "".join(splitString)
        
disemvowel("This website is for losers LOL!")
    
    
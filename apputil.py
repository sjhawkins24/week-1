

# Exercise 1
def palindrome(word):
    '''Function that takes a string and returns true or false if the string is a palindrome'''
    #Clean up the characters
    word = word.replace(",", "").replace(".", "").replace(" ", "").replace("?", "").replace("!","").lower()
    #create new var to hold the reverse of the clean word 
    rev_word = word[::-1]
    #Check for equivanence 
    check = rev_word == word 
    return(check)

# Exercise 2 
def parentheses(sequence):
    '''Function that accepts a string and returns whether the parentheses are balanced. 
    Also returns which side is unbalanced and by how many '''
    n_open = sequence.count("(")
    n_close = sequence.count(")")
    if n_open == n_close :
        return("True")
    else :
        return("False")


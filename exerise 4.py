def starts_with_a(word):
    if word[0] == "A":
        return True
    else:
        return False


#main routine
word = input("enter the word: ").title()

print(starts_with_a(word))





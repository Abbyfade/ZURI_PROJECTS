# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code herelist_of_word = list(word)
    list_of_word = list(word)
    list_of_anagram = list(anagram)
    if len(word) != len(anagram):
        print("The word and the anagram do not have the same number of characters")
    elif sorted(list_of_word) == sorted(list_of_anagram):
        return("Hurray {0} and {1} are anagrams!".format(word,anagram))
    else:
        return("{0} and {1} are not anagrams!".format(word,anagram))

   

print("This program helps identify if two words are anagrams.")
word = input("Input your first word: ")
anagram = input("Input your second word: ")
print(find_anagram(word, anagram))


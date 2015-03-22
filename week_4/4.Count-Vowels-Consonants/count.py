word = input("Write a word: ")
def count_vowels_consonants(word):
    vowels_list = "aeiouyAEIOUY"
    consonants_list = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    number_vowels = 0
    number_consonants = 0
    result = {}
    for ch in word:
        if ch in vowels_list:
            number_vowels += 1
        if ch in consonants_list:
            number_consonants +=1
    result["vowels"] = number_vowels
    result["consonants"] = number_consonants
    return result

print(count_vowels_consonants(word))
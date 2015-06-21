def word_to_list(encrypted_word):
    result = []
    for ch in encrypted_word:
        result += [ch]
    return result

def decode_word(encrypted_word, cipher):
    encrypted_word_list = word_to_list(encrypted_word)
    result = []
    for index in encrypted_word_list:
        for key in cipher:
            value = cipher[key]
            if value == index:
                result += [key]
    return ''.join(result)



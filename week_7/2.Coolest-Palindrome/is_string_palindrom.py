string = input("Write something: ")
def is_string_palindrom(string):
    string = string.lower()
    string = string.replace(" ","")
    string = string.replace(",","")
    string = string.replace(".","")
    string = string.replace("!","")
    string = string.replace("?","")
    reversed_string = string
    reversed_string = reversed_string [::-1]
    if string == reversed_string:
        return True
    else:
        return False
print(is_string_palindrom(string))
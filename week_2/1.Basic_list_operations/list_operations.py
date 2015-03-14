list_one = [1]
list_two = [1, 2, 3]
list_empty = []
list_true = [True, True, True]
list_names = ["Python", "Django"]
list_other = ["C", "C#", "Python", "PHP"]


languages = ["Python", "Ruby"]
languages += ["C++"]
languages += ["Java"]
languages += ["C#"]
languages = ["Haskell"] + languages
languages += ["Go"]
print(languages)
print(languages[0])
print(languages[1])
print(languages[3])
languages[5] = "F#"
print(languages)

n = len(languages)
print(languages[n - 1])

a = [1, 2, 3]
b = [4, 5, 6]
c = [1]
d = [8, 8, 10]
all = a + b + c + d
print(all)

ab = a + b
print(ab)

cd = c + d
print(cd)

aa = a + a
print(aa)
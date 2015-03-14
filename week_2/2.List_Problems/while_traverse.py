books = ["Learn You a Haskell", "The Healthy Programmer",
         "Code Complete", "The Pragmatic Programmer",
         "Pro Git", "Introduction to Algorithms", "Concrete Mathematics"]
n = len(books) - 1
index = 0
while index <= n:
    book = books[index]
    index += 1
    print(book)
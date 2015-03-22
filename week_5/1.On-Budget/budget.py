books = [0, 10, 100, 5, 3, 8, 25]
budget = 35
budget = int(budget)

def on_budget(books, budget):
    result = {"books_on_budget": 0, "loan": 0}
    count = 0
    total_price = sum(books)
    books = sorted(books)

    for book in books:
        if budget - book < 0:
            break
        budget -= book # От бюджета вадим книгата
        total_price -= book # От сумата на всички книги вадим сумата на книгата
        count += 1
# Записваме резултатите в речника
    result["books_on_budget"] = count
    loan = total_price - budget
    result["loan"] = loan

    return result
print(on_budget(books, budget))
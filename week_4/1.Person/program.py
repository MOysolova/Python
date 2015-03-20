first_name = input("First name: ")
second_name = input("Second name: ")
third_name = input("Third name: ")
birth_year = input("Birth year: ")
birth_year = int(birth_year)
result = {}

result["first_name"] = first_name
result["second_name"] = second_name
result["third_name"] = third_name
result["birth_year"] = birth_year
result["current_age"] = 2015 - birth_year

print(result)
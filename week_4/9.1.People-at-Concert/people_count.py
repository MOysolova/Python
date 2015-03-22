activity = ["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]
def get_people_count(activity):
    counted_people = []
    for person in activity:
        if person not in counted_people:
            counted_people += [person]
    return len(counted_people)
print(get_people_count(activity))

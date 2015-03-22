students = [{"name": "RadoRado", "status": "not_finalized"}, {"name": "Ivo", "status": "finalized"}, {"name": "Genadi", "status": "finalized"}]

def status_count(students):
    result = {"finalized": [], "not_finalized": []}
    for student in students:
        if student["status"] == "finalized":
            result["finalized"] += [student["name"]]
        elif student["status"] == "not_finalized":
            result["not_finalized"] += [student["name"]]
    return result
print(status_count(students))
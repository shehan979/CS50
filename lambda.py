people = [
    {"name": "Harry", "house": "Colombo"},
    {"name": "Shehan", "house": "Matara"},
    {"name": "Daniel", "house": "Kandy"}
    ]

def f(person):
    return person["name"]

# people.sort(key=f) #sort by function on f
#or other way sort
people.sort(key=lambda person: person["name"])
print(people)
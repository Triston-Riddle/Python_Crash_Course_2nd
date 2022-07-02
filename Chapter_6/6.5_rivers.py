# dictionary of 3 major rivers and their associated county

rivers = {
    'nile': "Africa",
    'congo': "South America",
    'mississippi': "North America"
}

# for loop printing a statement about each river

for river, country in rivers.items():
    print(f"The {river.title()} is a major river in {country}.")

# print each key in the dictionary

for river in rivers:
    print(river)

# print each value in the dictionary

for country in rivers.values():
    print(country)
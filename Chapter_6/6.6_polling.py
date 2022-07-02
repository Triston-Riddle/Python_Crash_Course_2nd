# favorite languages dictionary

favorite_languages = {
    'jen': "python",
    'sarah': "",
    'edward': "C++",
    'phil': "Rust",
    'kaleb': "",
}

# loop thruogh the list to check if the user has taken the favoite languages poll
# if user has a stored value for the language poll, print, "thank you for participating"
# if user has no vlaue stored for the langauge poll, print, "take the fuckin poll you fat fcuk"
for result in favorite_languages.values():
    if result == "":
        print("take the fuckin poll you fat fcuk")
    else:
        print("thanks for taking the survery!")
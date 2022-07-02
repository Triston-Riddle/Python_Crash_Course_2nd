#create a list of random items to work through 
from typing import final


random_items = ["bikes ", "cats ", "weed ", "computers ", "cybersecurity ", "good habits ", "your mom"]

#slice the first three items of the list
print("\nThe first three items of the list are- ")

for first_three in random_items[ :3]:
    print(first_three)

# OUTPUT - bikes  cats  weed

# slice the middle three items of the list
print("\nthe three items in the middle of the list are- ")

for middle_three in random_items[2:5]:
    print(middle_three)

# OUTPUT - weed  computers  cybersecurity

#slice the final three items from the list
print("\nThe final three items of the list are- ")

for last_three in random_items[4:7]:
    print(last_three)


# OUTPUT - your mom  good habits  cybersecurity
# list 1 - 9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# adding "th" to the end of each number
for numbers in numbers:
    if numbers == 1:
        print(f"{numbers}st")
    elif numbers == 2:
        print(f"{numbers}nd")
    elif numbers == 3:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")

# OUTPUT  1st 2nd 3rd 4th 5th 6th 7th 8th 9th
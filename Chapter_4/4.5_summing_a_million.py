#make a list of one to one million


for numbers in list(range(1, 1000001)):
    print(numbers)


#use min() and max() to ensure the list begins at 1 and ends at one million


print(min(numbers))
print(max(numbers))


#use the sum function to see how quickly python can add a million numbers


print(sum(numbers))
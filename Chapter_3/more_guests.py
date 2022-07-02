#adding three new guests to the invite list 
#send out a message to all the people on the list informing them of the larger table and added guests

guest_list = ["Kaleb ", "Whitney ", "Erin "]
guest_list[2] = "Shawn "

print(f"Hey {guest_list} I just wanted to let you all know that we just secured a new, larger table so I have added some new people to the guest list!")

#use the insert() method to add a new guest to the begginning, middle, and end of the guest list

guest_list.insert(0, "Alyssa ")
guest_list[1] = "Anakin Skywalker "
guest_list.append("R2D2 ")

#print new invitation messages for all the guests on the list

print(f"Greetings {guest_list} we will all be metting Friday at 7pm for dinner and drinks!")
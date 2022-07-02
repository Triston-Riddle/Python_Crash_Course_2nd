#define guest list var

guest_list = ["Kaleb ", "Whitney ", "Shawn ", "Anakin Skywalker ", "R2-D2 "]

#apology message to guest list apologizing to everyone on guest_list

message = (f"hey {guest_list}, I am sorry to inform you all that our large table has been canceled due to overflow, I will be shortening the guest list to only two people, please do not he too angry with me!")

print(message)

#remove guests from the list using the pop() method
#print a message to the removed guests apologizing to them

removed_guests = guest_list.pop(4)
print(f"Hey {removed_guests}sorry to have to uninvite you guys, there will always be next time, much love!")

removed_guests = guest_list.pop(3)
print(f"Hey {removed_guests}sorry to have to uninvite you guys, there will always be next time, much love!")

removed_guests = guest_list.pop(2)
print(f"Hey {removed_guests}sorry to have to uninvite you guys, there will always be next time, much love!")

#print a message to the remaining guests letting them know they are still invited

print(f"Good news {guest_list}you two are still invited to dinner!")

#delete the final two names from the list

del guest_list[1]
del guest_list[0]

print(guest_list)



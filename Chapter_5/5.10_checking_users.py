# list of users

from hashlib import new


current_users = ["admin", "slappynutz", "phant0m", "scoop", "sizedquasar"]

# list of new users

new_users = ["your mom", "admin", "bing bong", "pussy", "im horny"]

# call the new users group in a for loop
# check to see weather the new users' selected name(s) is present among the current users
# print "username already in use" if the username is already taken

for new_users in new_users:
    if new_users in current_users:
        print("sorry this name is already taken, try another!")
    else:
        print("Username available!")
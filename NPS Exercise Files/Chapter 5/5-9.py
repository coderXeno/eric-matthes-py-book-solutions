usernames = ["rx","bb123","admin","helloooo","lolbro","uvvv"]

del usernames[:]
if(len(usernames)==0):
    print("We need to find some users!")

for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+name+", thank you for logging in again.")
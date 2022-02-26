current_users = ["rx","bb123","admin","helloooo","lolbro","uvvv"]
new_users = ["bb123","lolbro","rohanrockzzz","fomo","wanderlust45"]

for user in new_users:
    if user.lower() in current_users:
        print("Hello "+user+". You need to enter a new username")
    else:
        print("Username "+user+" available")
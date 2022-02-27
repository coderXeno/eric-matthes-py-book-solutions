def build_profile(first, last, **user_info):
    profile = {}
    
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_profile = build_profile('Universal', 'xeno',
                    location='Kolkata',
                    field='Full Stack Dev',
                    hobby = 'listening to music'
                )

print(user_profile)
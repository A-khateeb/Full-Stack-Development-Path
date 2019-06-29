def make_profile(first, last, **user_profile):
    profile={}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_profile.items():
        profile[key] = value.title()
    return profile

user_profile = make_profile('afeef','khateeb',location='jerusalem',field='IT', age = str(27))
print(user_profile)

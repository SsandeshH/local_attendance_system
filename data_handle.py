user_details ={}

def append_user_details(name,email,phone,semester):
    user_id = len(user_details) + 1
    user_details[user_id] = {
        'name': name,
        'email': email,
        'phone': phone,
        'semester': semester
    }   
    return user_details
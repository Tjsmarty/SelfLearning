def password_controller(password):
    control = password
    if len(control) > 8:
        return "success"
    else:
        return "password entered not longer than 8"


check = password_controller("cus")
print(check)

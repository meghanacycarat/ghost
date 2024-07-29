import re
def password_strength(password):
    if len(password)<8 :
        return "weak password is short"

    has_lowercase= any(char.islower() for char in password)
    has_uppercase= any(char.isupper() for char in password)
    has_digit= any(char.isdigit() for char in password)
    has_special=any(char in '!@#$%^&*()_+{}|:"<>,./?~`' for char in password)

    complexity = sum[has_digit,has_special,has_lowercase,has_uppercase];
    if complexity<3:
        return "Weak : password lacks complexity"
    common_pattern=[r'123',r'password',r'abc',r'qwerty',r'12345678',r'admin']
    for pattern in common_pattern :
        if re.search(pattern,password,re.IGNORECASE):
            return "wEAK : PASSWORD CONTAINS COMMON PATTErn"
    return "Strong password: meets criteria for strength"

password = input("enter the password")
print(password_strength(password))

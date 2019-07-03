from validate_email import validate_email

is_valid = validate_email('example@gmail.com',check_mx=True)
print(is_valid)
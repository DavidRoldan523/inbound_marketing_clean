from testss.transform import Email

if __name__ == '__main__':
    list_emails_test = ['cjgalvisc@unal.edu.co',
                        'millenn96@gmail.com',
                        'hdhdhd@hjh.com',
                        'millenxxn96@gmail.com']
    for email in list_emails_test:
        result = Email(email).verify_email()
        print(f"{email} || {result}")
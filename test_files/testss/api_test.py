import requests

if __name__ == '__main__':
    list_emails_test = ['cjgalvisc@unal.edu.co',
                        'millenn96@gmail.com',
                        'hdhdhd@hjh.com',
                        'millenxxn96@gmail.com',
                        'cristian@yopmail.com',
                        'xzkgkfkfkrrkr@yopmail.com']
    for email in list_emails_test:
        url = f'https://emailverification.whoisxmlapi.com/api/v1' \
              f'?apiKey=at_qutWRadV4EGYuHotdJgEt9keSKIic' \
              f'&emailAddress={email}'
        response = requests.get(url)
        print(f"{email} || {response.json()['smtpCheck']}")
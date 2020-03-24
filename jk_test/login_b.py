url_login = '/login'
username = 'xiaoming'
password = '123456'
patload = 'username=' + username + 'password=' + password
comm = Common()
response_login = requests.post(url_login,data=payload)
print("Response内容：" + response_login.text)
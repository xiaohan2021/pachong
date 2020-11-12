import requests

payload = {'username':'xx', 'password':'xx'}
s = requests.session()
print(s.get('http://127.0.0.1:8080/user/6').content)
r = s.post('http://127.0.0.0:8080/login/', data=payload)
# print(s.get('http://127.0.0.1/user/6').content)
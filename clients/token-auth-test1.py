import requests

def client():
    # credentials = {"username": "ganavi123", "password": "ganavi123"}
    # response = requests.post("http://127.0.0.1:9008/api/rest-auth/login/", data=credentials)
    response = requests.get("http://127.0.0.1:9008/api/profiles/")
    print("status code :", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client() 
    
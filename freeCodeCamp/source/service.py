import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    responce = requests.get("http://jsonplaceholder.typicode.com/users")
    if responce.status_code == 200:
        return responce.json()

    raise requests.HTTPError

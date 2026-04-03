import requests

def fetch_github_user(username: str) -> dict:
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.json()

def display_user(user: dict) -> None:
    print(f"Name:         {user.get('name', 'N/A')}")
    print(f"Username:     {user['login']}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers:    {user['followers']}")
    print(f"Profile:      {user['html_url']}")

user = fetch_github_user("torvalds")
display_user(user)
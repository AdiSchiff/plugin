import requests

BASE_URL = "https://dummyjson.com"
USERNAME = "emilys"
PASSWORD = "emilyspass"

def login():
    url = f"{BASE_URL}/auth/login"
    payload = {"username": USERNAME, "password": PASSWORD}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("connection established")
        return data["accessToken"]
    else:
        print(f"connection failed: {response.status_code}, {response.text}")
        return None

def fetch_user_details(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"failed to fetch user details: {response.status_code}")
        return None

def fetch_posts(limit=60):
    response = requests.get(f"{BASE_URL}/posts?limit={limit}")
    
    if response.status_code == 200:
        return response.json()["posts"]
    else:
        print(f"failed to fetch the posts: {response.status_code}")
        return None

def fetch_posts_with_comments(limit=60):
    posts = fetch_posts(limit)
    
    if not posts:
        print(f"failed to fetch the posts without comments: {response.status_code}")
        return None
    
    for post in posts:
        post_id = post["id"]
        response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")

        if response.status_code == 200:
            post["comments"] = response.json()["comments"]
        else:
            post["comments"] = []
    
    return posts

if __name__ == "__main__":
    token = login()
    
    if token:
        user = fetch_user_details(token)
        posts = fetch_posts()
        posts_with_comments = fetch_posts_with_comments()
        
        print("\n E1 - user details:")
        print(user)
        
        print("\n E2 - 60 posts:")
        print(posts)
        
        print("\n E3 - 60 posts with connebts:")
        print(posts_with_comments)
    else:
        print("not able to connect")
import requests, re

def main():
    post_id = 1
    post_url = "https://idol.sankakucomplex.com/post/show/%s"%post_id
    response = requests.get(post_url, timeout=None)
    with open('response.txt', 'w') as response_f:
        response_f.write(response.text)

main()

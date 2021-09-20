import requests
import os

def main():
    resp = requests.get('https://ru.hexlet.io/courses')
    print(resp.text)

if __name__ == '__main__':
    main()
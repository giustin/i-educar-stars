import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def get_stars_github():
    r = requests.get('https://api.github.com/repos/portabilis/i-educar')

    content = r.json()
    stars = content['stargazers_count']

    return stars

def main():
    

if __name__ == "__main__":
    app.run()
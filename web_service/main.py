import os
import json
from collections import defaultdict
from flask import Flask, render_template, request

app = Flask(__name__)

logo_dict = defaultdict(int)

@app.route('/', methods=["POST", "GET"])
def hello_world():  # put application's code here
        global logo_dict
        if request.method == "POST":
                logo_number = request.form.get("logo_number")
                print(type(logo_dict), logo_dict)
                logo_dict[logo_number] += 1
        return render_template('index.html')

def main():
        global logo_dict
        if os.path.exists("data.json"):
             with open('data.json', 'r') as file:
                    logo_dict = defaultdict(int, json.loads(file.read()))
        app.run()
        with open('data.json', 'w+') as file:
                json.dump(logo_dict, file)

if __name__ == '__main__':
        main()

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():  # put application's code here
    if request.method == "POST":
        logo_number = request.form.get("logo_number")
        print(logo_number)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

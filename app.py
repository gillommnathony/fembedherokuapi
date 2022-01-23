from flask import Flask

app = Flask(__name__)

@app.rote('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(deburg=True)
import flask
import time
app = flask.Flask("test")

@app.route("/")
def home():
    return "OK"

@app.route("/ping")
def ping():
    return "OK"

@app.route("/message/<int:wait>/<int:size>")
def message(wait, size):
    time.sleep(wait)
    msg = "OK" * size
    return msg

if __name__ == '__main__':
    app.run("0.0.0.0", 8081)
    

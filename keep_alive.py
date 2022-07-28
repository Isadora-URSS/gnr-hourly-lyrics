from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def inicio():
    return "Hello Word!"
def iniciar():
    app.run(host = "0.0.0.0", port = 8090)

def keep_alive():
    t = Thread(target = iniciar)
    t.start()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/avi")
def avi():
	return "Hello Avi!"

@app.route("/website")
def website():
	return "<html><head><title>Hi Avi</title></head><body><h1>Hello Avi!</h1></body></html>"
	
if __name__ == "__main__":
    app.run()
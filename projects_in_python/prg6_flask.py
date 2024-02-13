from flask import Flask

app = Flask(__name__)
def home():
	return "prg1.html"

if __name__ == "__main__":
	app.run()

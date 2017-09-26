from flask import Flask, render_template,redirect,request,url_for,session
from database import *

app = Flask(__name__)

app.secret_key = "my secret key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
	error = None
	if request.method == "POST":
		if checkUser(request.form["username"],request.form["password"]) == False:
			error = "Invalid login credentials"
		else:
			session["logged_in"] = True
			session["username"] = request.form["username"]
			return redirect(url_for("dashboard"))
	return render_template("login.html",error=error)

@app.route("/dashboard")
def dashboard():
	if not session.get("logged_in"):
		return redirect(url_for("login"))
	else:
		return render_template("dashboard.html")

@app.route("/lamp", methods=["POST"])
def led_hadler():
	if request.form["lamp"] == "ON":
		# TODO: add function call to relay
		print("light on")
	elif request.form["lamp"] == "OFF":
		# TODO: add function call to relay
		print("light off")
	else:
		print("something wrong")
	return render_template("dashboard.html")



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")

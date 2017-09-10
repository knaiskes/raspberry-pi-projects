from flask import Flask, render_template,redirect,request,url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
	error = None
	if request.method == "POST":
		# testing username and password
		if request.form["username"] != "kiriakos" or request.form["password"] != "test":
			error = "Invalid login credentials"
		else:
			return redirect(url_for("index"))
	return render_template("login.html",error=error)



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")

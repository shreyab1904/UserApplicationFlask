from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def UserApp():
    return render_template("login.html")

@app.route("/register")
def userregister():
    return render_template("register.html")



if __name__=="__main__":
    app.run()
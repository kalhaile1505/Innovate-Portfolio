from flask import Flask, Blueprint, render_template, url_for, redirect

views = Blueprint(__name__, "views")

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

#linking pages

####################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/contact")
def home():
    return render_template("contact.html")

@app.route("/adminstration")
def home():
    return render_template("admin.html")

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

####################################

# 404 page link

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

####################################

# activiate debugging

if __name__ == "__main__":
    app.run(debug=True, port=8000)

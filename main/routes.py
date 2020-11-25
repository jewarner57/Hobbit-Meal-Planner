from flask import Blueprint, render_template

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/feedback")
def contact():
    return render_template("feedback.html")

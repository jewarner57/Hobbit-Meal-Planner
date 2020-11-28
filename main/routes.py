from flask import Blueprint, render_template, abort, request, redirect, url_for

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/feedback", methods=["GET", "POST"])
def contact():
    if(request.method == "POST"):

        # send email with feedback

        return redirect(url_for("main.home"))
    else:
        abort(404)

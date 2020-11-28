from flask import Blueprint, render_template, request

plan = Blueprint("plan", __name__, template_folder="templates")


@plan.route("/createPlan", methods=["GET", "POST"])
def createPlan():
    if request.method == "GET":
        return render_template("createPlan.html")
    else:
        return "post recieved"


@plan.route("/viewPlan")
def viewPlan():
    return render_template("view-plan.html")

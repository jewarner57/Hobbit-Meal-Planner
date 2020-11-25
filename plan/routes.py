from flask import Blueprint, render_template

plan = Blueprint("plan", __name__, template_folder="templates")


@plan.route("/createPlan")
def createPlan():
    return render_template("createPlan.html")


@plan.route("/viewPlan")
def viewPlan():
    return render_template("view-plan.html")

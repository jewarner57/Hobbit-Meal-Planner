from flask import Blueprint, render_template, request, redirect, url_for
import requests


plan = Blueprint("plan", __name__, template_folder="templates")


@plan.route("/createPlan", methods=["GET", "POST"])
def createPlan():
    if request.method == "GET":
        return render_template("createPlan.html")
    else:
        return redirect(url_for("plan.viewPlan"))


@plan.route("/viewPlan")
def viewPlan():

    # url = "http://api.openweathermap.org/data/2.5/weather"
    # params = {"appid": API_KEY, "q": city, "units": units}

    # result_json = requests.get(url, params=params).json()

    return render_template("viewPlan.html")

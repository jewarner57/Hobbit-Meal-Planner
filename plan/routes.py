from flask import Blueprint, render_template, request, redirect, url_for
import requests
import os
import json

plan = Blueprint("plan", __name__, template_folder="templates")


@plan.route("/createPlan", methods=["GET", "POST"])
def createPlan():
    if request.method == "GET":
        return render_template("createPlan.html")
    else:
        return redirect(url_for("plan.viewPlan"))


@plan.route("/viewPlan")
def viewPlan():

    mealTitles = {}
    with open('./static/mealinfo.json') as json_file:
        mealTitles = json.load(json_file)

    url = "https://api.spoonacular.com/recipes/random"
    params = {"apiKey": os.getenv(
        "SPOONACULAR_API_KEY"), "number": 7}

    result_json = requests.get(url, params=params).json()

    meals = result_json
    if result_json.get("recipes") is not None:
        meals = result_json.get("recipes")

    context = {
        "response": meals,
        "mealNames": mealTitles.get('meals')
    }

    return render_template("viewPlan.html", **context)

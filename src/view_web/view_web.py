from flask import Blueprint, render_template, request

blueprint = Blueprint( "view_web" , __name__, "templates")

import sys
sys.path.append('src')

import controller.ControllerRegistros as ControllerRegistros

@blueprint.route("/")
def Home():
    return render_template("home_template/home.html")

@blueprint.route("/result_tax")
def Home_result():
    return render_template("result_tax_template/result_tax.html")

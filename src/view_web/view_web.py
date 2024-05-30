from flask import Blueprint, render_template, request

blueprint = Blueprint( "view_web" , __name__, "templates")

import sys
sys.path.append('src')

from view_web.view_web_logic import *
import controller.ControllerRegistros as ControllerRegistros

@blueprint.route("/")
def Home():
    return render_template("home_template/home.html")

@blueprint.route("/result_tax")
def Home_result():
    valores = {
                "cedula" : request.args["cedula"],
                "salario" : request.args["salary"],
                "salarioGravable" : request.args["graval_salary"],
                "salarioNoGravable" : request.args["no_graval_salary"],
                "retencionFuente" : request.args["withholding_tax"],
                "pagoHipotecario" : request.args["mortgage_loan_payment"],
                "donaciones" : request.args["donations"],
                "gastosEducacion" : request.args["education_expenses"]
            }
    
    taxObject = calculate_fee( valores )

    return render_template("result_tax_template/result_tax.html", tax = taxObject)

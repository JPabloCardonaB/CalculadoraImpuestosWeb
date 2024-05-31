from flask import Blueprint, render_template, request

blueprint = Blueprint( "view_web" , __name__, "templates")

import sys
sys.path.append('src')

from view_web.view_web_logic import *
import controller.ControllerRegistros as ControllerRegistros

# Ruta principal
@blueprint.route("/")
def Home():
    return render_template("home_template/home.html")

# Ruta para los resultados
@blueprint.route("/result_tax")
def Home_result():
    # valores es un diccionario que contiene los parametros que result tax recibio del Home

    valores = {
                "cedula" : request.args["cedula"],
                "salario" : request.args["salary"],
                "salarioGravable" : request.args["graval_salary"],
                "salarioNoGravable" : request.args["no_graval_salary"],
                "retencionFuente" : request.args["withholding_tax"],
                "pagoHipotecario" : request.args["mortgage_loan_payment"],
                "donaciones" : request.args["donations"],
                "gastosEducacion" : request.args["education_expenses"],
                "guardar_tax" : request.args["save_tax"]
            }
    
    taxObject = calculate_fee( valores )

    return render_template("result_tax_template/result_tax.html", tax = taxObject)

# Ruta para obtener la informacion de la declaracion de renta asociada a esa persona
@blueprint.route("/result_research")
def Home_search():
    # Recibe la cedula de la persona y busca los datos de la declaracion de impuestos

    cedula = request.args["cedula"]

    taxObject = search_record_by_id(cedula)

    return render_template("home_template/home.html", tax = taxObject)

# Ruta para eliminar la informacion de la declaracion de renta asociada a esa persona
@blueprint.route("/delete_cedula")
def Home_delete():
    # Recibe la cedula de la persona y elimina los datos de la declaracion de impuestos

    cedula = request.args["cedula"]

    delete_record(cedula)

    return render_template("home_template/home.html")

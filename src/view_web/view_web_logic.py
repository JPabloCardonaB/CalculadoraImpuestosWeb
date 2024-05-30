from model import TaxLogic

from controller import ControllerRegistros

from model.TaxLogic import calculateTax

ControllerRegistros.CreateTable()

import sys
sys.path.append('src')

#Actualizar registro actual
def update_record_current(valores):
    try:
        id = int( id.text )
        total_labor_income_per_year = int( total_labor_income_per_year.text )
        other_taxable_income_per_year = int( other_taxable_income_per_year.text )
        other_non_taxable_income_per_year = int( other_non_taxable_income_per_year.text )
        source_retention_value_per_year = int( source_retention_value_per_year.text )
        mortgage_loan_payment_per_year = int( mortgage_loan_payment_per_year.text )
        donation_value_per_year = int( donation_value_per_year.text )
        educational_expenses_per_year = int( educational_expenses_per_year.text )

        TaxInformation = TaxLogic.TaxInformation(
            id,
            total_labor_income_per_year, 
            other_taxable_income_per_year, 
            other_non_taxable_income_per_year, 
            source_retention_value_per_year, 
            mortgage_loan_payment_per_year, 
            donation_value_per_year, 
            educational_expenses_per_year)

        ControllerRegistros.UpdateRecord( TaxInformation )

        #show_Notification("Registro actualizado con exito.")

    except Exception as e:
        print("Error: ", e)
        #show_error("Error: {}".format(e)) 

"""
#Buscar registro por cedula
def search_record_by_id(cedula):
    try:
        id = int( id.text )

        result = ControllerRegistros.SearchRecordByID( id )

        id.text = str(result.id)
        total_labor_income_per_year.text = str(result.total_labor_income_per_year)
        other_taxable_income_per_year.text = str(result.other_taxable_income_per_year)
        other_non_taxable_income_per_year.text = str(result.other_non_taxable_income_per_year)
        source_retention_value_per_year.text = str(result.source_retention_value_per_year)
        mortgage_loan_payment_per_year.text = str(result.mortgage_loan_payment_per_year)
        donation_value_per_year.text = str(result.donation_value_per_year)
        educational_expenses_per_year.text = str(result.educational_expenses_per_year)
        result.text = ''
    
    except Exception as e:
        show_error("Error: {}".format(e)) 
"""

#Borrar registro
def delete_record(cedula):
    try:
        id = int( id.text )

        ControllerRegistros.DeleteRecord( id )

        #show_Notification("Registro borrado con exito.")
    
    except Exception as e:
        print("Error:", e)
        #show_error("Error: {}".format(e)) 


#Calcular cuota
def calculate_fee(valores):
    try:
        id = int( valores["cedula"] )
        total_labor_income_per_year = int( valores["salario"] )
        other_taxable_income_per_year = int( valores["salarioGravable"] )
        other_non_taxable_income_per_year = int( valores["salarioNoGravable"])
        source_retention_value_per_year = int( valores["retencionFuente"])
        mortgage_loan_payment_per_year = int( valores["pagoHipotecario"])
        donation_value_per_year = int( valores["donaciones"])
        educational_expenses_per_year = int( valores["gastosEducacion"])

        TaxInformation = TaxLogic.TaxInformation(
            id,
            total_labor_income_per_year, 
            other_taxable_income_per_year, 
            other_non_taxable_income_per_year, 
            source_retention_value_per_year, 
            mortgage_loan_payment_per_year, 
            donation_value_per_year, 
            educational_expenses_per_year)

        result = calculateTax( TaxInformation )

        ControllerRegistros.InsertRecord( TaxInformation )

        return result

    except Exception as e:
        print("Error:", e)
        #show_error("Error: {}".format(e))
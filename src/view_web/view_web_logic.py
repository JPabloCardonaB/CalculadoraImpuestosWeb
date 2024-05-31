from model import TaxLogic

from controller import ControllerRegistros

from model.TaxLogic import calculateTax

import sys
sys.path.append('src')

#Actualizar registro actual
def update_record_current(valores):
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

        ControllerRegistros.UpdateRecord( TaxInformation )


    except Exception as e:
        print("Error: ", e)


#Buscar registro por cedula
def search_record_by_id(cedula):
    try:
        result = ControllerRegistros.SearchRecordByID( cedula )

        valores = {
                    "cedula" : result.id,
                    "salario" : result.total_labor_income_per_year,
                    "salarioGravable" : result.other_taxable_income_per_year,
                    "salarioNoGravable" : result.other_non_taxable_income_per_year,
                    "retencionFuente" : result.source_retention_value_per_year,
                    "pagoHipotecario" : result.mortgage_loan_payment_per_year,
                    "donaciones" : result.donation_value_per_year,
                    "gastosEducacion" : result.educational_expenses_per_year
                }
        
        return valores
    
    except Exception as e:
        print("Error:", e)


#Borrar registro
def delete_record(cedula):
    try:
        ControllerRegistros.DeleteRecord( cedula )
    
    except Exception as e:
        print("Error:", e)


#Calcular cuota
def calculate_fee(valores):
    ControllerRegistros.CreateTable()

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

        if valores["guardar_tax"] == 'true':

            ControllerRegistros.InsertRecord( TaxInformation )

        return result

    except Exception as e:
        print("Error:", e)